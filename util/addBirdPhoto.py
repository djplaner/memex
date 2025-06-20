"""
Add a photo from my iPhotos library for a bird to the relevant image folder for a bird identified in my LIFE_LIST_DATA_FILE

addBirdPhoto.py [--photo <photoName> | --uuid <uuid>] --submission <submissionId> | --bird <bird name> 

use one of the following to identify the photo in the Photos app:
--photo: Name of the photo in the Photos app
--uuid: Name of the file in the Photos app

to identify the photo to be added. 
--submission specify the submission ID from eBird matching LIFE_LIST_DATA_FILE
TODO --bird: Name of the bird matching the common name in the LIST_LIST_DATA_FILE

Process

- Bird
    - Read LIFE_LIST_DATA_FILE (CSV) into a data frame
    - Check if the bird name exists in the data frame, if not, error
    - save the folder to {BIRD_ASSETS_HOME}/images/{birdCamelCaseName}/
Photo
    - Check the photo exists in the Photos app
    - export the photo from the Photos app and make other changes
    - copy photo
    

"""

import argparse
import os
from pathlib import Path
import pandas as pd

import osxphotos
from osxphotos.cli import query_command, verbose

import markdown
import frontmatter

from PIL import Image, ImageOps

from pprint import pprint

MEMEX_HOME="/Users/davidjones/memex/"
ASSETS_URL="https://djon.es/"
ASSETS_FOLDER="/Users/davidjones"
ASSETS_HOME=f"{ASSETS_FOLDER}/assets/memex/"
BIRD_ASSETS_HOME= Path(f"{ASSETS_HOME}/sense/birdwatching/")
LIFE_LIST_FOLDER = Path(f"{MEMEX_HOME}/docs/sense/birdwatching/")
LIFE_LIST_DOCS_FOLDER = Path(f"sense/birdwatching")
LIFE_LIST_DATA_FILE = Path(LIFE_LIST_FOLDER / "ebirdData.csv")
LIFE_LIST_IMAGE_FOLDER = Path(BIRD_ASSETS_HOME / "images")


TMP_DIR="/Users/davidjones/downloads/"
TMP_FILENAME="testing-small"
IMAGE_SCALE=0.3333
PHOTO_YAML_FIELDS = [ "title", "filename", "latitude", "longitude", "description", "date"  ]

def showFoundPhotos( photos):
    """Show summary of key details of a list of photos. 
    Used when findPhoto finds multiple photos.

    Parameters:
    photos (list): List of osxphotos.PhotoInfo objects
    """

    print("---------- Photos found ")
    for photo in photos:
        print("--")
        pDict = photo.asdict()
        fields = PHOTO_YAML_FIELDS
        fields.append( "uuid")
        for field in fields:
            print(f"{field}: {pDict[field]}")
        
def findPhoto(args: argparse.Namespace) -> osxphotos.PhotoInfo:
    """Extract photo matching the name from Photos app library
    Error if num photos found is 0 or more than 1
    Photos can be searched for by other filename of photo

    Parameters:
    args (argparse.Namespace): Command line arguments
    Returns:
    osxphotos.PhotoInfo: PhotoInfo object for the single photo
    """

    photosData = osxphotos.PhotosDB()

    if args.uuid:
        options = osxphotos.QueryOptions(uuid=[args.uuid])
    elif args.photo:
        options = osxphotos.QueryOptions(name=[args.photo])
    photos = photosData.query(options)

    if len(photos) == 0:
        raise ValueError(f"No photo found in Photos app with name matching {args.photo}")
    if len(photos) > 1:
        showFoundPhotos(photos)
        raise ValueError(f"Multiple photos found in Photos app with name matching {args.photo}")

    return photos[0]

def generateBirdImagePhotoDetails(birdObservation: dict) -> dict:
    """
    Given details about a bird observation, generate relevant data for the new photo

    {LIFE_LIST_IMAGE_FOLDER}/{birdCamelCaseName}/<sessionId><photoNum>.jpeg

    Parameters:
    - birdObservation (dict): Dictionary containing the bird observation data
    Returns:
    - {
        "path": Path to the folder where images will be saved,
        "birdCamelCaseName": CamelCase name of the bird observation
        "photoNum": <str> # empty if no <sessionId>*.jpeg files exist, otherwise _<number>
    }
    """

    #-- generate the birdCamelCaseName from the bird observation
    birdCamelCaseName = birdObservation['Common Name'].replace(" ", "")
    birdCamelCaseName = birdCamelCaseName.replace("-", "")
    # lower case the first letter
    birdCamelCaseName = birdCamelCaseName[0].lower() + birdCamelCaseName[1:]

    photoPath = LIFE_LIST_IMAGE_FOLDER / birdCamelCaseName 

    if not os.path.exists(photoPath):
        os.makedirs(photoPath)

    # check the photoPath to see how many photos with <sessionId>*.jpeg exist 
    sessionId = birdObservation['Submission ID']
    photoNum = 0
    for file in os.listdir(photoPath):
        if file.startswith(sessionId) and file.endswith('.jpeg'):
            photoNum += 1

    photoNum = "" if photoNum == 0 else f"_{photoNum}"

    return { "path": photoPath, "birdCamelCaseName": birdCamelCaseName,
            "photoNum": photoNum}


def exportPhoto(photo: osxphotos.PhotoInfo, birdObservation: dict ) -> bool:
    """Export the photo out of Photos app and resize it, saving it to the relevant direction
    - extract the photos from the Photos library
    - reduce the size by 1/3
    - save to the relevant folder

    {LIFE_LIST_IMAGE_FOLDER}/{birdCamelCaseName}/{sessionId}.jpeg
    {LIFE_LIST_IMAGE_FOLDER}/{birdCamelCaseName}/{sessionId}_1.jpeg
    {LIFE_LIST_IMAGE_FOLDER}/{birdCamelCaseName}/{sessionId}_2.jpeg

    Parameters:
    - photo (osxphotos.PhotoInfo): PhotoInfo object for the photo
    - birdObservation (dict): Dictionary containing the bird observation data
    Returns:
    - bool: True if successful, False otherwise
    
    """

    details = generateBirdImagePhotoDetails( birdObservation )
    photoPath = details["path"]
    #birdCamelCaseName = details["birdCamelCaseName"]
    photoNum = details["photoNum"]
    submissionId = birdObservation['Submission ID']
    fileName = f"{submissionId}{photoNum}.jpeg"

    # TODO work on which options should be set, perhaps parameterise
    exportOptions = osxphotos.ExportOptions(
       convert_to_jpeg=True, 
       jpeg_quality=1, 
       update=True, 
       overwrite=True,
       location=False, 
       exiftool=True,
       use_photos_export=True
    )
    exporter = osxphotos.PhotoExporter( photo )
    exporter.export( dest=photoPath, 
                    filename=fileName, options=exportOptions )
                    #filename=str(photoNum), options=exportOptions )

    if not os.path.exists(f"{photoPath}/{fileName}"):
        raise ValueError(f"Failed to export photo to {photoPath}/{fileName}")
    with Image.open(f"{photoPath}/{fileName}") as img:
        #-- ensure photo orientation is correct
        img = ImageOps.exif_transpose(img)
        (width, height) = (img.width*IMAGE_SCALE, img.height*IMAGE_SCALE)
        img_resized = img.resize((int(width), int(height)))
        img.close()

        ## Save the image into individual plant/images/plant/<number>.jpeg
        img_resized.save(f"{photoPath}/{fileName}")

        return True

    return False


def retrieveBirdObservation(submissionId: str) -> dict:
    """
    Retrieve the bird observation from the LIFE_LIST_DATA_FILE matching the submissionId

    Parameters:
    - submissionId (str): Submission ID from eBird matching LIFE_LIST_DATA_FILE
    Returns:
    dict: Dictionary containing the bird observation data
    """

    if not LIFE_LIST_DATA_FILE.exists():
        raise ValueError(f"No such file {LIFE_LIST_DATA_FILE}")

    df = pd.read_csv(LIFE_LIST_DATA_FILE, encoding="utf-8-sig")
    
    #-- check if submissionId exists in the dataframe
    if submissionId not in df['Submission ID'].values:
        raise ValueError(f"No submission found with id {submissionId} in {LIFE_LIST_DATA_FILE}")

    #-- get the row matching the submissionId
    row = df[df['Submission ID'] == submissionId].iloc[0]
    
    return row.to_dict()

def parseArgs():
    """Parse out command line args
    --photo "Photo name"
      Matching the photo's name in the Photos app
    --plant "Plant name"
      Matching the individual plant's markdown file name in Memex
    """

    parser = argparse.ArgumentParser(description="Add a photo for an individual plant from the Photos library into Memex")
    parser.add_argument("--photo", help="Photo name - matching Photos app name", required=False)
    parser.add_argument("--submission", help="Submission id from eBird" )
    parser.add_argument("--uuid", help="Uuid of the photo in the Photos app", required=False)
    args = parser.parse_args()

    if not args.photo and not args.uuid:
        parser.error("Please provide either a photo name (--photo) or a uuid (--uuid) matching a photo in the Photos app")
    if not args.submission:
        parser.error("Please provide a submission id (--submission) matching eBird submission")
    return args

if __name__ == "__main__":

    #-- grab command line arguments
    args = parseArgs()

    #-- Find single photo in Photos app matching name
    photo = findPhoto(args)

    #-- get the content of the markdown file, including YAML
    # - { markdown: full content, yaml: YAML front matter }
#    plantMemex = retrievePlantFile(args.plant, args.species)

    birdObservation = retrieveBirdObservation(args.submission)
    pprint(birdObservation)

    exportPhoto( photo, birdObservation )

    #-- update the YAML front matter and export the image
#    updateMemex(args.plant, plantMemex, photo, args.species)

