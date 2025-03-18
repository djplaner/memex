# Copyright (C) 2025 David Jones
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

"""
Add a photo for an individual plant from the Photos library into Memex, including
1. Add metadata information into the YAML frontmatter of the plant's page
2. Add the photo to the relevant images directory

addPlantPhoto.py --name FILENAME --verbose

IMG_2578.HEIC
"""

import argparse
import os

import osxphotos
from osxphotos.cli import query_command, verbose

import markdown
import frontmatter

from PIL import Image

from pprint import pprint

SINGLE_PLANT_DIR="../docs/sense/landscape-garden/individual-plants/"
TMP_DIR="/Users/davidjones/downloads/"
TMP_FILENAME="testing-small"
IMAGE_SCALE=0.3333

@query_command
def addPlantPhoto(photos: list[osxphotos.PhotoInfo], **kwargs):
    """
    Add a photo for an individual plant from the Photos library into Memex, including
    1. Add metadata information into the YAML frontmatter of the plant's page
    2. Add the photo to the relevant images directory
    """

    verbose(f"Found {len(photos)} photos")
    verbose(f"kwargs: {kwargs}")

    findPhotos = []  # photos.query( **kwargs )
    verbose(
        f"Searching for name {kwargs['name']} in photos found {len(findPhotos)} photos")
    verbose(findPhotos)

    """ osxphoto query to get a specific file
    --name FILENAME
    --title TITLE
    """


def findPhoto(name: str):
    """Extract photo from Photos app matching the name

    Parameters:
    name (str): Name of the photo in the Photos app
    Returns:
    osxphotos.PhotoInfo: PhotoInfo object for the photo
    """
    photosData = osxphotos.PhotosDB()

    options = osxphotos.QueryOptions(name=[name])
    print(f"Searching for name {name}")
#    print(options)
    photos = photosData.query(options)

    print(f"Found {len(photos)} photos with name {name}")
    # print(photos)
    print("--------- photo")

    for photo in photos:
        for field in ( "title", "filename", "latitude", "longitude", 
                      "height", "width" ):
            print(f"-- {field}: {getattr(photo, field)}")
#        pprint(photo.info)
    if len(photos) == 0:
        raise ValueError(f"No photo found in Photos app with name matching {args.photo}")
    if len(photos) > 1:
        raise ValueError(f"Multiple photos found in Photos app with name matching {args.photo}")

    return photos[0]

def exportPhoto(photo: osxphotos.PhotoInfo, plant: str) -> bool:
    """Export the photo out of Photos app and resize it, saving it to the relevant direction
    - extract the photos from the Photos library
    - reduce the size by 1/3
    - save to the relevant folder

    Parameters:
    photo (osxphotos.PhotoInfo): PhotoInfo object for the photo
    plant (str): Name of the plant (matching the markdown filename)
    Returns:
    bool: True if successful, False otherwise
    
    """

    # TODO work on which options shoudl be set, perhaps parameterise
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
    exporter.export( dest=TMP_DIR, 
                    filename=TMP_FILENAME, options=exportOptions )

    with Image.open(f"{TMP_DIR}{TMP_FILENAME}.jpeg") as img:
        (width, height) = (img.width*IMAGE_SCALE, img.height*IMAGE_SCALE)
        img_resized = img.resize((int(width), int(height)))

        ## Save the image into individual plant/images/plant/<number>.jpeg
        img_resized.save("/Users/davidjones/downloads/testing-small-pil-X.jpeg")

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
    Given path local to DOCS_FOLDER for a markdown file, extract the front matter
    and return it"""

    md = markdown.Markdown(extensions = ['meta'])
    pageData = {}
    with open(path, encoding="utf-8-sig") as f:
        pageData["content"] = f.read()
        html = md.convert(pageData["content"])
        pageData['yaml'] = md.Meta
        pageData['html'] = html

#        print(pageData['yaml'])
#        print("------- YAML AFTER")
        
        for key in pageData['yaml'].keys():
            pageData['yaml'][key] = pageData['yaml'][key][0]
            # remove any quotes surrounding the value
            pageData['yaml'][key] = pageData['yaml'][key].lstrip('\"').rstrip('\"')
#            print(f"{key}: {pageData['yaml'][key]}")

        #fMatter = frontmatter.load(content)
#        fMatter = frontmatter.load(f)

        return pageData

    return None

def retrievePlantFile(plant: str):
    """Return data extract from the markdown file for an individual plant

    Parameters:
    plant (str): Name of the plant (matching the markdown filename)
    Returns:
    dict: { markdown: full content, yaml: YAML front matter }
    """

    markdownFile = f"{SINGLE_PLANT_DIR}{plant}.md"

    #-- error if no such file
    if not os.path.exists(markdownFile):
        raise ValueError(f"No such file {markdownFile}")

    markdown = extractPlantMarkdown(markdownFile)
    print("------- MARKDOWN")
    pprint(markdown)
    print("------- YAML")
    yaml = extractPlantYAML(markdownFile)
    pprint(yaml)
    print("----- end")
    print(yaml)

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
    parser.add_argument("--photo", help="Photo name - matching Photos app name")
    parser.add_argument("--plant", help="Plant name - matching markdown filename" )
    args = parser.parse_args()

    if not args.photo:
        parser.error("Please provide a photo name")
    if not args.plant:
        parser.error("Please provide a plant name")
    return args

def writePlantFile( plantName: str, yaml: str, markdownContent: str ):
    """Update the markdown file for the individual plant with the new YAML front matter (update the file)

    Parameters:
    plantName (str): Name of the plant (matching the markdown filename)
    markdown (str): Full content of the markdown file
    """

    filePath = f"{SINGLE_PLANT_DIR}{plantName}.md"
    #filePath = f"/tmp/{plantName}.md"

    if not os.path.exists(filePath):
        raise ValueError(f"No such file to writePlantFile {filePath}")

    with open(filePath, "w") as f:
        f.write("---\n")
        f.write(yaml)
        f.write("---\n")
        f.write(markdownContent)

def createYamlString( yamlStruct: dict, photoInfo: osxphotos.PhotoInfo ) -> str:
    """Create a string containing YAML information ready to write to markdown file.

    Create the photos and all other sections separtely

    Parameters:
    yamlStruct (dict): YAML structure from the existing YAML front matter
    photoInfo (osxphotos.PhotoInfo): PhotoInfo object for the photo
    Returns:
    str: YAML string
    """

    yaml = ""

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
    pprint(pDict, indent=2)
    if "photos" not in yamlStruct.keys():
        yamlStruct["photos"] = {}
    else:
        for photoNum in yamlStruct["photos"].keys(): 
            #-- update the yamlStruct if filename matches
            if yamlStruct["photos"][photoNum]["filename"] == pDict["filename"]:
                for key in ( "title", "filename", "latitude", "longitude", "description"):
                    yamlStruct["photos"][photoNum][key] = pDict[key]
                updatePhoto = True
            lastPhoto = photoNum

    #-- if not updatePhoto then add new photo to yamlStruct
    if not updatePhoto:
        lastPhoto = str(int(lastPhoto) + 1)
        yamlStruct["photos"][lastPhoto] = {}
        for key in ( "title", "filename", "latitude", "longitude", "description"):
            yamlStruct["photos"][lastPhoto][key] = pDict[key]

    #-- convert yamlStruct into a yaml string and append to yaml
    yaml += "photos:\n"
    for photoNum in yamlStruct["photos"].keys():
        yaml += f"  {photoNum}:\n"
        for key in yamlStruct["photos"][photoNum].keys():
            yaml += f"      {key}: {yamlStruct['photos'][photoNum][key]}\n"

    print("------ FINAL YAML")
    print(yaml)
    print("----")

    return yaml

def updatePlantYAML( plantName: str, plantMemex: dict, 
                    photoInfo : osxphotos.PhotoInfo ):
    """Modify the memex YAML front matter for the individual plant to include information about the new photo

    - If photo information already exists in the YAML, error/update it??? TODO
    - If photo information does not exist, add it to the YAML
    - update the markdown file with the new YAML

    Parameters:
    plantName (str): Name of the plant (matching the markdown filename)
    plantMemex (dict): { markdown: full content, yaml: YAML front matter }
    photoInfo (osxphotos.PhotoInfo): PhotoInfo object for the photo
    """

    #-- content is a string with current contents of the markdow file
    markdown = plantMemex["markdown"]["content"]
    #-- remove any yaml frontmatter
    if markdown.startswith("---"):
        markdown = markdown[markdown.find("---", 3)+4:]

    #-- convert plantMemex[yaml] dict to a yaml string
    yaml = createYamlString(plantMemex["yaml"], photoInfo)
    print("--- final YAML string")
    print(yaml)

    writePlantFile( plantName, yaml, markdown ) 

    pass

if __name__ == "__main__":

    #-- grab command line arguments
    args = parseArgs()

    #-- Find single photo in Photos app matching name
    photo = findPhoto(args.photo)

    #-- get the content of the markdown file, including YAML
    # - { markdown: full content, yaml: YAML front matter }
    plantMemex = retrievePlantFile(args.plant)

    #-- check to see if that photo is already associated with that plant
    #   - does it exist in the YAML frontmatter
    #   - does it exist in the images directory (this name is based on 
    #   - YAML front matter )

    #-- export the photo to the relevant directory
    # - would need to know the number of the image (from the YAML)
    exportPhoto(photo, "the-original-bunya-pine" )

    updatePlantYAML(args.plant, plantMemex, photo)

