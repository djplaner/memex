"""
lifeList.py
- Convert an eBird life list CSV export into a collection of markdown files
"""

from pathlib import Path
import pandas as pd
from pprint import pprint

global LIFE_LIST_FOLDER
LIFE_LIST_FOLDER = Path("../docs/sense/birdwatching/")
global LIFE_LIST_DATA_FILE
LIFE_LIST_DATA_FILE = Path(LIFE_LIST_FOLDER / "ebirdData.csv")
global LIFE_LIST_PAGE 
LIFE_LIST_PAGE = Path(LIFE_LIST_FOLDER / "life-list.md")
global LIFE_LIST_IMAGE_FOLDER 
LIFE_LIST_IMAGE_FOLDER= Path(LIFE_LIST_FOLDER / "images")

global LIFE_LIST_TEMPLATE
LIFE_LIST_TEMPLATE = """---
title: "Life list"
type: "note"
tags: birdwatching, birding
---

See also: [[birding]]

Collection of birds I've seen (and photographed) in the wild. This list is based on my eBird data.

| Date | Common Name | Scientific Name | Location | # Photos |
| ---- | -------------|-----------------|----------| ---- |
"""

global BIRD_PAGE_TEMPLATE
BIRD_PAGE_TEMPLATE = """---
title: "{{{BIRDNAME}}}"
type: "note"
tags: birding, birdwatching
---

See also: [[birding]], [[life-list]]

(Click on the images to see a larger version)

"""

global BIRD_IMAGE_TEMPLATE
BIRD_IMAGE_TEMPLATE = """
<figure markdown="span">
    ![](./images/blueFacedHoneyEater.jpg)
    <figcaption><a href="https://en.wikipedia.org/wiki/Blue-faced_honeyeater">Blue-faced Honeyeater</a></figcaption>
</figure>
"""

def getLifeList():
    """
    Retrieve the life list data from the CSV file
    """

    if not LIFE_LIST_DATA_FILE.exists():
        raise FileNotFoundError("Life list file not found")

    df = pd.read_csv(LIFE_LIST_DATA_FILE)

    #-- raise an error if no rows found
    if df.empty:
        raise ValueError("No data found in the life list")

    return df

def modifyLifeList(df):
    """
    Make any necessary modifications to the life list data, including
    - add a column 'camelCaseName' based on 'Common Name'
    """

    #-- add a column 'camelCaseName' based on 'Common Name'
    #df['camelCaseName'] = df['Common Name'].str.replace(" ", "").str.lower()
    df['camelCaseName'] = df['Common Name'].str.replace(" ", "").str.replace("-", "")
    #-- make the first letter of each 'camelCaseName' lowercase
    df['camelCaseName'] = df['camelCaseName'].str[0].str.lower() + df['camelCaseName'].str[1:]

    return df

def generatePhotoData(df):
    """
    Given a data frame containing life list data, generate a dictionary. Keyed on
    'camelCaseName' for each bird. Each bird is an array of information about any 
    photos taken of that bird.
    """

    photoData = {}

    #-- for each row in the data frame, create a dictionary entry
    #for index, row in df.iterrows():
    for row in df.iterrows():
        birdName = row[1]['camelCaseName']
        birdFolder = Path(LIFE_LIST_IMAGE_FOLDER / birdName)
        if not birdFolder.exists():
            continue
        #-- get a list of all images in the folder
        birdImages = [f for f in birdFolder.iterdir() if f.is_file()]
        photoData[birdName] = birdImages

    return photoData

def generateLifeList(df, photoData):
    """
    Generate a markdown file listing all birds in the life list
    """

    #-- open file
    with open(LIFE_LIST_PAGE, "w") as f:
        f.write(LIFE_LIST_TEMPLATE)

        #-- write the list of birds
        for row in df.iterrows():
#            f.write("""| {0} | {1} | {2} | {3} |\n""".format(row[1]['Date'], row[1]['Common Name'], row[1]['Scientific Name'], row[1]['Location']))

            birdName = row[1]['camelCaseName']

            name = row[1]['Common Name']
            numImages = 0

            if birdName in photoData:
                numImages = len(photoData[birdName])
                generateBirdPage(birdName, row, photoData[birdName])
                name = f"[{name}]({birdName}.md)"

            f.write(f"""| {row[1]['Date']} | {name} | {row[1]['Scientific Name']} | {row[1]['Location']} | {numImages} | \n""")

def generateBirdPage(name, row, images):
    """
    Write a markdown file for a bird with photos.
    """

    birdPage = Path(LIFE_LIST_FOLDER / f"{name}.md")

    print(f"-- generate bird page for {name} - {birdPage}")

    with open(birdPage, "w") as f:
        content = BIRD_PAGE_TEMPLATE
        content = content.replace("{{{BIRDNAME}}}", row[1]['Common Name'])

        f.write(content)

        for image in images:
            # remove LIFE_LIST_FOLDER from the image path
            imageRel = f"../{image.relative_to(LIFE_LIST_FOLDER)}"

            f.write(f"""<figure markdown>![{name}]({imageRel})</figure>\n""")

def main():

    #-- grab the data
    listData = getLifeList()
    listData = modifyLifeList( listData )
    photoData = generatePhotoData( listData )

    #-- generate markdown files
    # - Generate the life-list.md file listing all birds
    generateLifeList( listData, photoData )

    # - Generate individual files for birds with photos
    #generateBirdPages( listData, photoData )

    
if __name__ == "__main__":

    main()
