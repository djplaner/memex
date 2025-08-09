"""
Add a photo for an individual plant or plant species from the Photos library into Memex, including:

1. Add metadata information into the YAML frontmatter of the individual plant's page
2. Add the photo to the relevant images directory (within the separate assets folder)

addPlantPhoto.py --photo <photoName> | --uuid <uuid> --plant <plantName> --species

use one of the following to identify the photo in the Photos app:
--photo: Name of the photo in the Photos app
--uuid: Name of the file in the Photos app

to identify the photo to be added. And following to nominate plant in Memex
--plant: Name of the plant (matching the markdown filename - minus the .md)
--species: Boolean flag to indicate if the photo is for a species, without it assume
       an individual plant photo

YAML frontmatter fields for photos to be added to the individual plant's page take the form of an array of dictionaries

photos:
    1:
        date: <timedate photo taken>
        description: <description from photo metadata>
        latitude: <latitude from photo metadata>
        longitude: <longitude from photo metadata>
        title: <title from photo metadata>
        memexFilename: <originally page within memex, now full URL>
    2:
        ...
"""

import argparse
import os

import osxphotos
from osxphotos.cli import query_command, verbose

import markdown
import frontmatter

from PIL import Image, ImageOps

from pprint import pprint

SINGLE_PLANT_DIR="/Users/davidjones/memex/docs/sense/landscape-garden/individual-plants/"
PLANTS_DIR="/Users/davidjones/memex/docs/sense/landscape-garden/plants/"
SINGLE_PLANT_IMAGES_DIR="/Users/davidjones/assets/memex/sense/landscape-garden/individual-plants/"
SINGLE_PLANT_IMAGES_URL="https://djon.es/assets/memex/docs/sense/landscape-garden/individual-plants/images/"
PLANTS_IMAGES_DIR="/Users/davidjones/assets/memex/sense/landscape-garden/plants/"
PLANTS_IMAGES_URL="https://djon.es/assets/memex/sense/landscape-garden/plants/images/"
#PLANT_IMAGES_PATH="images/"
PLANT_IMAGES_PATH="https://djon.es/assets/memex/docs/sense/landscape-garden/plants/images/"
SINGLE_PLANT_IMAGES_PATH="https://djon.es/assetsimages/"
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

def exportPhoto(photo: osxphotos.PhotoInfo, plant: str, photoNum : int, species : bool) -> bool:
    """Export the photo out of Photos app and resize it, saving it to the relevant direction
    - extract the photos from the Photos library
    - reduce the size by 1/3
    - save to the relevant folder

    {SINGLE_PLANT_IMAGES_DIR}/images/{plant}/{photoNum}.jpeg

    Parameters:
    - photo (osxphotos.PhotoInfo): PhotoInfo object for the photo
    - plant (str): Name of the plant (matching the markdown filename)
    - photoNum (int): Which number has been allocated to this photo
    - species (bool): Boolean flag to indicate if the photo is for a species or not
    Returns:
    - bool: True if successful, False otherwise
    
    """

    #-- create the path for the photo both as a string and as a directory
    if species:
        photoPath = f"{PLANTS_IMAGES_DIR}images/{plant}/"
    else:
        photoPath = f"{SINGLE_PLANT_IMAGES_DIR}images/{plant}/"
    if not os.path.exists(photoPath):
        os.makedirs(photoPath)

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
                    filename=str(photoNum), options=exportOptions )

    if not os.path.exists(f"{photoPath}{photoNum}.jpeg"):
        raise ValueError(f"Failed to export photo to {photoPath}{photoNum}.jpeg")
    with Image.open(f"{photoPath}{photoNum}.jpeg") as img:
        #-- ensure photo orientation is correct
        img = ImageOps.exif_transpose(img)
        (width, height) = (img.width*IMAGE_SCALE, img.height*IMAGE_SCALE)
        img_resized = img.resize((int(width), int(height)))
        img.close()

        ## Save the image into individual plant/images/plant/<number>.jpeg
        img_resized.save(f"{photoPath}{photoNum}.jpeg")

        return True

    return False

def extractPlantYAML(path):
    """
    Given path local to DOCS_FOLDER for a markdown file, extract the front matter
    and return it"""

    with open(path, "r") as f:
        content = f.read()
        fMatter = frontmatter.loads(content)
        return fMatter.metadata

    return None

def extractPlantMarkdown(path):
    """
    Given path local to DOCS_FOLDER for a markdown file, extract the front matter and return it"""

    md = markdown.Markdown(extensions = ['meta'])
    pageData = {}
    with open(path, encoding="utf-8-sig") as f:
        pageData["content"] = f.read()
        html = md.convert(pageData["content"])
        pageData['yaml'] = md.Meta
        pageData['html'] = html

        for key in pageData['yaml'].keys():
            pageData['yaml'][key] = pageData['yaml'][key][0]
            # remove any quotes surrounding the value
            pageData['yaml'][key] = pageData['yaml'][key].lstrip('\"').rstrip('\"')

        return pageData

    return None

def retrievePlantFile(plant: str, species: bool = False) -> dict:
    """Return data extract from the markdown file for an individual plant

    Parameters:
    - plant (str): Name of the plant (matching the markdown filename)
    - species (bool): Boolean flag to indicate if the photo is for a species or not
    Returns:
    - dict: { markdown: full content, yaml: YAML front matter }
    """

    if species:
        markdownFile = f"{PLANTS_DIR}{plant}.md"        
    else:
        markdownFile = f"{SINGLE_PLANT_DIR}{plant}.md"

    #-- error if no such file
    if not os.path.exists(markdownFile):
        raise ValueError(f"No such file {markdownFile}")

    markdown = extractPlantMarkdown(markdownFile)
    yaml = extractPlantYAML(markdownFile)

    if markdown is None:
        raise ValueError(f"No markdown for plant found matching {markdownFile}")
        
    return {
        "markdown": markdown,
        "yaml": yaml
    }

def parseArgs():
    """Parse out command line args
    --photo "Photo name"
      Matching the photo's name in the Photos app
    --plant "Plant name"
      Matching the individual plant's markdown file name in Memex
    """

    parser = argparse.ArgumentParser(description="Add a photo for an individual plant from the Photos library into Memex")
    parser.add_argument("--photo", help="Photo name - matching Photos app name", required=False)
    parser.add_argument("--plant", help="Plant name - matching markdown filename" )
    parser.add_argument("--uuid", help="Uuid of the photo in the Photos app", required=False)
    parser.add_argument("--species", help="Boolean flag to indicate if the photo is for a species or not", action="store_true", default=False, required=False)
    args = parser.parse_args()

    if not args.photo and not args.uuid:
        parser.error("Please provide either a photo name (--photo) or a uuid (--uuid) matching a photo in the Photos app")
    if not args.plant:
        parser.error("Please provide a plant name (--plant) matching memex markdown filename")
    return args

def writePlantFile( plantName: str, yaml: str, markdownContent: str, species: bool = False):
    """Update the markdown file for the individual plant with the new YAML front matter (update the file)

    Parameters:
    - plantName (str): Name of the plant (matching the markdown filename)
    - yaml (str): YAML front matter to be written to the file
    - markdown (str): Full content of the markdown file
    - species (bool): Boolean flag to indicate if the photo is for a species or not
    """

    if species:
        filePath = f"{PLANTS_DIR}{plantName}.md"
    else:
        filePath = f"{SINGLE_PLANT_DIR}{plantName}.md"

    if not os.path.exists(filePath):
        raise ValueError(f"No such file to writePlantFile {filePath}")

    with open(filePath, "w") as f:
        f.write("---\n")
        f.write(yaml)
        f.write("---\n")
        f.write(markdownContent)

def createYamlString( plantName: str, yamlStruct: dict, 
                     photoInfo: osxphotos.PhotoInfo, species: bool ) -> str:
    """Create a string containing YAML information ready to write to markdown file.

    Create the photos and all other sections separtely

    Parameters:
    - plantName (str): Name of the plant (matching the markdown filename)
    - yamlStruct (dict): YAML structure from the existing YAML front matter
    - photoInfo (osxphotos.PhotoInfo): PhotoInfo object for the photo
    - species (bool): Boolean flag to indicate if the photo is for a species or not
    Returns:
    str: YAML string
    """

    yaml = ""

    if species:
        url = PLANTS_IMAGES_URL
    else:
        url = SINGLE_PLANT_IMAGES_URL

    #-- add all the non photos information
    for key in yamlStruct.keys():
        if key=="photos":
            continue
        yaml += f"{key}: {yamlStruct[key]}\n"

    #-- loop thru each photo dict
    # - if not matching the photo, add it to the yaml
    # - if matching the photo, update it and track 
    # - add the new photo information (new index)
    lastPhoto = 0
    updatePhoto = False
    pDict = photoInfo.asdict()
    if "photos" not in yamlStruct.keys():
        yamlStruct["photos"] = {}
    else:
        for photoNum in yamlStruct["photos"].keys(): 
            #-- update the yamlStruct if filename matches
            if yamlStruct["photos"][photoNum]["filename"] == pDict["filename"]:
                for key in ( PHOTO_YAML_FIELDS ):
                    if key != "date":
                        yamlStruct["photos"][photoNum][key] = pDict[key]
                    else:
                        yamlStruct["photos"][photoNum][key] = pDict[key].strftime("%Y-%m-%d %H:%M:%S")
                updatePhoto = True
                #-- export the photo to the relevant directory to overwrite
                print(f"XXXXXX Updating the photo {pDict['filename']} in {plantName} with number {photoNum}")
                if exportPhoto(photoInfo, plantName,  photoNum, species ):
                    yamlStruct["photos"][photoNum]["memexFilename"] = f"{url}{plantName}/{photoNum}.jpeg"
                else:
                    raise ValueError(f"Failed to export photo to {SINGLE_PLANT_DIR}{plantName}/{photoNum}.jpeg")

            lastPhoto = photoNum

    #-- if not updatePhoto then add new photo to yamlStruct
    if not updatePhoto:
        lastPhoto = str(int(lastPhoto) + 1)
        yamlStruct["photos"][lastPhoto] = {}
        for key in ( PHOTO_YAML_FIELDS ):
            if key != "date":
                yamlStruct["photos"][lastPhoto][key] = pDict[key]
            else:
                yamlStruct["photos"][lastPhoto][key] = pDict[key].strftime("%Y-%m-%d %H:%M:%S")
        print(f"XXXX creating new Last photo number in YAML: {lastPhoto}")
        #-- export the photo to the relevant directory to add it
        if exportPhoto(photoInfo, plantName,  lastPhoto, species):
            yamlStruct["photos"][lastPhoto]["memexFilename"] = f"{url}{plantName}/{lastPhoto}.jpeg"
        else:
            raise ValueError(f"Failed to export photo to {SINGLE_PLANT_DIR}{plantName}/{lastPhoto}.jpeg")

    #-- convert yamlStruct into a yaml string and append to yaml
    yaml += "photos:\n"
    for photoNum in yamlStruct["photos"].keys():
        yaml += f"  {photoNum}:\n"
        for key in yamlStruct["photos"][photoNum].keys():
            yaml += f"      {key}: {yamlStruct['photos'][photoNum][key]}\n"

    return yaml

def updateMemex( plantName: str, plantMemex: dict, 
                    photoInfo : osxphotos.PhotoInfo, species: bool = False):
    """Modify the memex YAML front matter for the individual plant to include information about the new photo

    - If photo information already exists in the YAML, error/update it??? TODO
    - If photo information does not exist, add it to the YAML
    - update the markdown file with the new YAML

    Parameters:
    - plantName (str): Name of the plant (matching the markdown filename)
    - plantMemex (dict): { markdown: full content, yaml: YAML front matter }
    - photoInfo (osxphotos.PhotoInfo): PhotoInfo object for the photo
    - species (bool): Boolean flag to indicate if the photo is for a species or not
    """

    #-- content is a string with current contents of the markdow file
    markdown = plantMemex["markdown"]["content"]
    #-- remove any yaml frontmatter
    if markdown.startswith("---"):
        markdown = markdown[markdown.find("---", 3)+4:]

    #-- convert plantMemex[yaml] dict to a yaml string
    yaml = createYamlString(plantName, plantMemex["yaml"], photoInfo, species)

    print(f"Writing YAML for {plantName} with species={species}:\n{yaml}")
    print('----- markdown')
    print(markdown)
#    quit()

    writePlantFile( plantName, yaml, markdown, species ) 

if __name__ == "__main__":

    #-- grab command line arguments
    args = parseArgs()

    #-- Find single photo in Photos app matching name
    photo = findPhoto(args)

    #-- get the content of the markdown file, including YAML
    # - { markdown: full content, yaml: YAML front matter }
    plantMemex = retrievePlantFile(args.plant, args.species)

    pprint(plantMemex)
#    quit()

    #-- update the YAML front matter and export the image
    updateMemex(args.plant, plantMemex, photo, args.species)

