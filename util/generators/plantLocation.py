"""
plantLocation.py

Generator to re-write ~/sense/landscape-gardens/individual-plants/plant-gps.js to contain
an array of dicts

    {
        title: <title from markdown file frontmatter>,>
        lat: <from markdown file frontmatter>, long: <from markdown file frontmatter>,
        description: <extract from photo??>,
        imageUrl: <first image from markdown yaml>
        memex: <name of markdown file>,
        date: <from the photo? is it needed??>,
        zone: <from where>
    },

- Read all of the markdown files in the individual-plants folders
- Extract the frontmatter
- ?? how to get the zones ??

"""

import glob
import os
import frontmatter
from pprint import pprint

INDIVIDUAL_PLANTS_FOLDER="../../docs/sense/landscape-garden/individual-plants"

def extractFrontMatter( file ):
    """
    Given path local to DOCS_FOLDER for a markdown file, extract the front matter
    and return it as a dictionary

    {   'latitude': -27.538371666666666,
        'longitude': 152.0554055,
        'photos': 
        {1: 
            {'date': datetime.datetime(2025, 3, 14, 17, 28, 38),
                'description': 'Mulberry - White Shahtoot',
                'filename': '6427D205-E5E9-44BC-B3F2-54BA95E455FC.heic',
                'latitude': -27.538371666666666,
                'longitude': 152.0554055,
                'memexFilename': 'images/white-shahtoot-mulberry/1.jpeg',
                'title': 'None'}
        },
        'tags': ['individual-plants'],
        'title': 'White Shahtoot mulberry',
        'type': 'single-plant'}
    """

    with open(file, "r") as f:
        content = f.read()
        fMatter = frontmatter.loads(content)
        #-- get filename of file, remove path
        #-- remove the .md from the filename
        fMatter.metadata['memex'] = os.path.basename(file).replace(".md", "")
        return fMatter.metadata

    return None


def getPlantData():
    """
    Read all markdown files in the individual-plants folder (except "individual_plants.md"), retrieve the frontmatter, and extract photo information and place it into an array
    """

    images = []

    print(f"{INDIVIDUAL_PLANTS_FOLDER}/*.md")
    files = glob.glob(f"{INDIVIDUAL_PLANTS_FOLDER}/*.md")

    print(files)

    for file in files:
        print(f"Reading {file}")
        frontMatter = extractFrontMatter(file)

        if frontMatter is None:
            raise ValueError(f"Unable to extract front matter from {file}")

        images.append( frontMatter)

    return images

def generatePlantJS(plantData):
    """
    Use the list of dicts for individual plants to write a new javascript file
    """

    #-- open the file for writing
    with open(f"{INDIVIDUAL_PLANTS_FOLDER}/plant-gps.js", "w") as f:
        f.write("const plantLocations = [\n")

        #-- loop through the list of dicts
        for plant in plantData:
            #-- extract the data
            title = plant['title']
            print(f"Processing {title}")
            #-- if no latitude or longitude, skip
            if 'latitude' not in plant or 'longitude' not in plant:
                print(f"Warning: No latitude or longitude for {title}")
                continue
            lat = plant['latitude']
            long = plant['longitude']
            #-- check if photos is empty
            description = ""
            imageUrl = ""
            date = ""
            if len(plant['photos']) > 0:
                description = plant['photos'][1]['description']
                imageUrl = plant['photos'][1]['memexFilename']
                date = plant['photos'][1]['date']
            else:
                print(f"Warning: No photos for {title}")
            memex = plant["memex"]
            zone = "unknown"  # TODO: how to get the zone?

            #-- write the data to the file
            f.write(f"""
    {{
        title: '{title}',
        lat: {lat},
        long: {long},
        description: '{description}',
        imageUrl: '{imageUrl}',
        memex: '{memex}',
        date: '{date}',
        zone: '{zone}'
    }},
""")

        f.write("];\n")
        f.write("export default plantLocations;\n")


if __name__ == "__main__":
    plantData = getPlantData()
    generatePlantJS(plantData)