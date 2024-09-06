"""
lifeList.py
- Convert an eBird life list CSV export and relveant images into a collection of markdown files
"""

from pathlib import Path
import pandas as pd
from pprint import pprint
import inflect

global LIFE_LIST_FOLDER
LIFE_LIST_FOLDER = Path("../docs/sense/birdwatching/")
global LIFE_LIST_DATA_FILE
LIFE_LIST_DATA_FILE = Path(LIFE_LIST_FOLDER / "ebirdData.csv")
global LIFE_LIST_PAGE 
LIFE_LIST_PAGE = Path(LIFE_LIST_FOLDER / "life-list.md")
global LIFE_LIST_IMAGE_FOLDER 
LIFE_LIST_IMAGE_FOLDER= Path(LIFE_LIST_FOLDER / "images")
global GALLERY_PAGE
GALLERY_PAGE = Path(LIFE_LIST_FOLDER / "life-list-gallery.md")

global LIFE_LIST_TEMPLATE
LIFE_LIST_TEMPLATE = """---
title: "Life list"
type: "note"
tags: birdwatching, birding
---

See also: [[birding]], [[life-list-gallery]]

Collection of birds I've seen. Generated from my [eBird](https://ebird.org) data. The [[life-list-gallery]] provides a gallery of all the bird photos I've taken.

| Common Name | Scientific Name | When | Where | # Photos |
| -------------|-----------------|----------|-----| ----- |
"""

global GALLERY_TEMPLATE
GALLERY_TEMPLATE = """---
title: "Life list gallery"
type: "note"
tags: birdwatching, birding
---

See also: [[birding]], [[life-list]]

Click on an image to see the full size version and to cycle through the gallery.

"""

global BIRD_PAGE_TEMPLATE
BIRD_PAGE_TEMPLATE = """---
title: "{{{BIRDNAME}}}"
type: "note"
tags: birding, birdwatching
---

See also: [[birding]], [[life-list]]

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

    #-- add a column 'images' to the df, each cell initial set to None
    df['images'] = None

    return df

def generatePhotoData(df):
    """Add relevant data about any photos associated with particular observations.

    Photo information is stored in a folder named after the bird in the LIFE_LIST_IMAGE_FOLDER.
    Individual photos are named after the submissionId possibly with the file name ending
    in 00x (x>0)

    Returns
    -------
    df : DataFrame

        Modified version of df. Add column "photos" containing a list of Paths for photos
    """

    photoData = {}

    #-- for each row in the data frame, create a dictionary entry
    #for index, row in df.iterrows():
    for row in df.iterrows():
        birdName = row[1]['camelCaseName']
        #-- check if there is a folder for the current bird
        birdFolder = Path(LIFE_LIST_IMAGE_FOLDER / birdName)
        if not birdFolder.exists():
            continue
        #-- get a list of all images in the folder
        # - should match the submission Id
        matchName = f"{row[1]['Submission ID']}*.jp*"
        matchingImages = list(birdFolder.glob(matchName))
        if len(matchingImages) == 0:
            continue

        df.at[row[0], 'images'] = matchingImages

    return df

def generateLifeList(df):
    """Write a markdown file with a formatted life list

    Each bird has a row with table columns: 
    - Common Name, 
    - Scientific Name, 
    - Observations - for each observation show location and date
    - Photos - show the number of photos for the bird

    Parameters
    ----------
    df : pandas.DataFrame
        Copy of eBird csv, with images column
    """

    p = inflect.engine()

    #-- open file
    with open(LIFE_LIST_PAGE, "w") as f:
        f.write(LIFE_LIST_TEMPLATE)

        #-- get a list of unique bird names "Common Name"
        birds = df['Common Name'].unique()

        for bird in birds:
            #-- extract all the rows for the current bird
            birdRows = df[df['Common Name'] == bird]

            #-- set the common values
            camelCaseName = birdRows['camelCaseName'].iloc[0]
            commonName = birdRows['Common Name'].iloc[0]
            scientificName = birdRows['Scientific Name'].iloc[0]
            commonNameLink = commonName

            totalImages = 0
            observations = ""

            #-- iterate through the rows
            for row in birdRows.iterrows():
                #-- count the number of elements in the list in 'images' column
                #observations = f"{observations} {row[1]['Location']} on {row[1]['Date']}"
                if row[1]['images'] is not None:
                    numImages = len(row[1]['images'])
                    totalImages += numImages
                    #observations = f"{observations} ({numImages} {p.plural('photos')}"
                    commonNameLink = f"[{commonName}](./{camelCaseName}.md)"
                observations = f"{observations}<br />"

            f.write(f"""| {commonNameLink} | {scientificName} | {row[1]['Date']} | {row[1]['Location']} | {totalImages} | \n""")

            if totalImages > 0:
                generateBirdPage(camelCaseName, commonName, birdRows)

def generateBirdPage(camelCaseName, commonName, birdRows):
    """
    Write a markdown file for a bird with photos.

    Parameters
    ----------
    camelCaseName : str
        The name of the bird in camelCase
    commonName : str
    birdRows: pandas.DataFrame
        Rows from the eBird data frame for the bird
    """

    birdPage = Path(LIFE_LIST_FOLDER / f"{camelCaseName}.md")

    with open(birdPage, "w") as f:
        content = BIRD_PAGE_TEMPLATE
        content = content.replace("{{{BIRDNAME}}}", commonName)

        f.write(content)

        #-- for each row
        imageCount = 0
        for row in birdRows.iterrows():
            #-- loop through images dict
            if row[1]['images'] is not None:
                for image in row[1]['images']:
                    imageCount += 1
                    # remove LIFE_LIST_FOLDER from the image path
                    imageRel = f"./{image.relative_to(LIFE_LIST_FOLDER)}"

                    f.write(f"""
<figure markdown id="{imageCount}">
  ![{commonName}]({imageRel}){{data-title="{commonName}" data-description="Observed at {row[1]['Location']} on {row[1]['Date']}"}}
  <caption>{commonName}<br />Observed at {row[1]['Location']} on {row[1]['Date']}</caption>
</figure>
""")

def generateImageGallery(df):
    """Generate life-list-gallery.md file with a gallery of all bird images

    Parameters
    ----------
    df : pandas.DataFrame
    """

    #-- extract all rows with 'images' column not None
    rows = df[df['images'].notnull()]

    with open(GALLERY_PAGE, "w") as f:
        f.write(GALLERY_TEMPLATE)

        for row in rows.iterrows():
            #-- loop through images dict
            for image in row[1]['images']:
                # remove LIFE_LIST_FOLDER from the image path
                imageRel = f"./{image.relative_to(LIFE_LIST_FOLDER)}"
                commonName = row[1]['Common Name']

                f.write(f"""
<figure markdown>
  ![{commonName}]({imageRel}){{data-title="{commonName}" data-description="Observed at {row[1]['Location']} on {row[1]['Date']}"}}
  <caption>{commonName}<br />Observed at {row[1]['Location']} on {row[1]['Date']}</caption>
</figure>
""")

def main():

    #-- grab the data
    listData = getLifeList()
    listData = modifyLifeList( listData )
    listData = generatePhotoData( listData )

    #-- generate markdown files
    # - Generate the life-list.md file listing all birds
    generateLifeList( listData )

    generateImageGallery( listData )


    
if __name__ == "__main__":

    main()
