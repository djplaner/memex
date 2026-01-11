"""
importeBird.py

Reads eBird CSV file and creates appropriate observation markdowns

Input:
- eBird CSV file located with path ~/memex_data/ebird.csv
- images with filenames matching eBird sessionIds  
   ~/assets/memex/sense/birdwatching/images/<speciesName>/<sessionId>(_<count>).jpeg

Checks:
- Are there any images related to the session
- Is there a page for the bird - if not create it

Output:
- Markdown files in ~/memex/docs/sense/Observations/bird-observations/<species>-<sessionId>.md
- Content example below
- Markdown file for bird species if not already present in
    ~/memex/docs/sense/birdwatching/


"""

import pandas as pd
from pathlib import Path

HOME_FOLDER="/Users/davidjones"
LIFE_LIST_DATA_FILE = Path(f"{HOME_FOLDER}/memex_data/ebirdData.csv")

ASSETS_HOME=f"{HOME_FOLDER}/assets/memex/"
ASSETS_URL="https://djon.es/"

BIRD_ASSETS_HOME= Path(f"{ASSETS_HOME}/sense/birdwatching/")
BIRD_OBSERVATIONS_HOME = Path(f"{HOME_FOLDER}/memex/docs/sense/Observations/bird-observations/")
LIFE_LIST_IMAGE_FOLDER = Path(BIRD_ASSETS_HOME / "images")


#MEMEX_HOME="/Users/davidjones/memex/"
#LIFE_LIST_FOLDER = Path(f"{MEMEX_HOME}/docs/sense/birdwatching/")
#LIFE_LIST_DOCS_FOLDER = Path(f"sense/birdwatching")
##LIFE_LIST_FOLDER = Path("sense/birdwatching")
#LIFE_LIST_DATA_FILE = Path(LIFE_LIST_FOLDER / "ebirdData.csv")
##LIFE_LIST_PAGE = Path(LIFE_LIST_FOLDER / "life-list.md")
#LIFE_LIST_PAGE = Path("sense/birdwatching/life-list.md")
##GALLERY_PAGE = Path(LIFE_LIST_FOLDER / "life-list-gallery.md")
#GALLERY_PAGE = Path("sense/birdwatching/life-list-gallery.md")


OBSERVATION_MD_TEMPLATE = """---
title: "<Common Name> (<Scientific Name>) - eBird observation <Date>"
type: observation
subject: [ <wikiLink common name> ]
observation-type: bird
date: <Date>
description: "eBird observation of <Common Name> (<Scientific Name>) on <Time> <Date>"
tags:
    - birdwatching
    - eBird
observation-data:
    common-name: "<Common Name>"
    scientific-name: "<Scientific Name>"
    taxonomic-order: "<Taxonomic Order>"
    latitude: <Latitude>
    longitude: <Longitude>
    date: "<Date>"
    time: "<Time>"
    county: "<County>"
    location: "<Location>"
---

[[<wikiLink common name>]] observation recorded via eBird on <Time> <Date> at <Location> ([<Latitude>, <Longitude>](https://www.google.com/maps/search/?api=1&query=<Latitude>,<Longitude>)).

<images markdown>

"""

BIRD_SPECIES_MD_TEMPLATE = """---
title: "<Common Name>"
type: bird-species
bird-data:
    common-name: "<Common Name>"
    scientific-name: "<Scientific Name>"
    taxonomic-order: "<Taxonomic Order>"
description: "Information (largely observations) about the bird species <Common Name> (<Scientific Name>)"
tags:
    - birdwatching
    - species
---

## Observations

{{ observations( subject: <wikiLink common name> ) }}

"""


def geteBirdDF():
    """
    Return a DataFrame containing the eBird life list data
    """

    if not LIFE_LIST_DATA_FILE.exists():
        raise FileNotFoundError(f"Life list file {LIFE_LIST_DATA_FILE} not found")

    df = pd.read_csv(LIFE_LIST_DATA_FILE)

    # -- raise an error if no rows found
    if df.empty:
        raise ValueError("No data found in the life list")

    return df

def modifyeBirdDF(df : pd.DataFrame):
    """
    Make any necessary modifications to the life list data, including
    - add a column 'camelCaseName' based on 'Common Name'
    - add a column 'wikiLink' based on 'Common Name'
    - add empty column 'images' to hold image data
    """

    # -- add a column 'camelCaseName' based on 'Common Name'
    # df['camelCaseName'] = df['Common Name'].str.replace(" ", "").str.lower()
    df['camelCaseName'] = df['Common Name'].str.replace(
        " ", "").str.replace("-", "")
    # -- make the first letter of each 'camelCaseName' lowercase
    df['camelCaseName'] = df['camelCaseName'].str[0].str.lower() + \
        df['camelCaseName'].str[1:]
    #-- add a column 'wikiLink' based on 'Common Name'
    df['wikiLink'] = df['Common Name'].str.lower()
    df['wikiLink'] = df['wikiLink'].str.replace(" ", "-")

    # -- add a column 'images' to the df, each cell initial set to None
    df['images'] = None

    return df

def addPhotoData(df : pd.DataFrame):
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

    # -- for each row in the data frame, create a dictionary entry
    # for index, row in df.iterrows():
    for row in df.iterrows():
        birdName = row[1]['camelCaseName']
        # -- check if there is a folder for the current bird
        birdFolder = Path(LIFE_LIST_IMAGE_FOLDER / birdName)
        if not birdFolder.exists():
            continue
        # -- get a list of all images in the folder
        # - should match the submission Id
        matchName = f"{row[1]['Submission ID']}*.jp*"
        matchingImages = list(birdFolder.glob(matchName))
        if len(matchingImages) == 0:
            continue

        df.at[row[0], 'images'] = matchingImages

    return df

def generateObservationMDs(df : pd.DataFrame):
    """
    Loop thru each observation 
    - construct filename for the observation
        ~/assets/memex/sense/birdwatching/images/<speciesName>/<sessionId>(_<count>).jpeg
    - check if file exists - if so skip
    - if not create the markdown file in
        ~/memex/docs/sense/Observations/bird-observations/<species>-<sessionId>.md
      - include matching images if any
    
    :param df: DataFrame
        DataFrame containing the eBird data with any modifications
    """

    #-- loop through each row in the dataframe
    for index, row in df.iterrows():
        speciesName = row['camelCaseName']
        sessionId = row['Submission ID']
        observationMDFile = Path( f"{BIRD_OBSERVATIONS_HOME}/{speciesName}/{sessionId}.md")
        numImages = len(row['images']) if row['images'] is not None else 0
        
        # -- check if the file already exists
        if observationMDFile.exists():
            print(f"Observation markdown {observationMDFile} already exists - skipping")
            continue
        else:
            # -- ensure the parent folder exists
            observationMDFile.parent.mkdir(parents=True, exist_ok=True)

        # -- create the markdown content
        mdContent = OBSERVATION_MD_TEMPLATE
        mdContent = mdContent.replace("<Common Name>", row['Common Name'])
        mdContent = mdContent.replace("<Scientific Name>", row['Scientific Name'])
        mdContent = mdContent.replace("<Date>", row['Date'])
        mdContent = mdContent.replace("<Time>", str(row['Time']))
        mdContent = mdContent.replace("<Location>", row['Location'])
        mdContent = mdContent.replace("<Latitude>", str(row['Latitude']))
        mdContent = mdContent.replace("<Longitude>", str(row['Longitude']))
        mdContent = mdContent.replace("<wikiLink common name>", row['wikiLink'])

        if numImages == 0:
            mdContent = mdContent.replace("<images markdown>", "No images available for this observation.")
        else:
            imagesMarkdown = generateImageMarkdown(row)
            mdContent = mdContent.replace("<images markdown>", imagesMarkdown)

#        print(mdContent)
#        print(f"Generating observation markdown for {speciesName} session {sessionId} with {numImages} images")
#        print(f"Generated observation markdown: {observationMDFile}")

        # -- write the markdown file
        with open(observationMDFile, 'w') as f:
            f.write(mdContent)

def generateImageMarkdown(row) -> str:
    """
    Generate the markdown for images in the observation markdown

    :param row: Series
        Row from the DataFrame containing the observation data
    :return: str
        Markdown string for images
    """

    imagesMD = ""
    for imagePath in row['images']:
#        relativePath = imagePath.relative_to(HOME_FOLDER + "/memex/assets/")
        imgUrl = str(imagePath).replace(str(HOME_FOLDER), ASSETS_URL)


        imagesMD += f"""
<figure markdown>
![{row['Common Name']}]({imgUrl})
</figure>

"""

    return imagesMD

def generateBirdSpeciesMDs( df: pd.DataFrame):
    """
    Loop thru each unique bird species in the DataFrame
    - check if a markdown file exists for the species in
        ~/memex/docs/sense/birdwatching/<species>.md
    - if not create it using the BIRD_SPECIES_MD_TEMPLATE

    :param df: DataFrame
        DataFrame containing the eBird data with any modifications
    """

    uniqueSpecies = df['camelCaseName'].unique()

    for species in uniqueSpecies:
        speciesMDFile = Path( f"{BIRD_ASSETS_HOME}/{species}.md")

        # -- check if the file already exists
        if speciesMDFile.exists():
            print(f"Species markdown {speciesMDFile} already exists - skipping")
            continue

        # -- get the first row matching the species to get common and scientific names
        speciesRow = df[df['camelCaseName'] == species].iloc[0]

        # -- create the markdown content
        mdContent = BIRD_SPECIES_MD_TEMPLATE
        mdContent = mdContent.replace("<Common Name>", speciesRow['Common Name'])
        mdContent = mdContent.replace("<Scientific Name>", speciesRow['Scientific Name'])


def main():

    # -- grab the data
    listData = geteBirdDF()
    listData = modifyeBirdDF(listData)
    listData = addPhotoData(listData)

    generateObservationMDs(listData)
    generateBirdSpeciesMDs(listData)

    ## TODO
#    generateImageGallery(listData)

    # -- generate markdown files
    # - Generate the life-list.md file listing all birds
#    generateLifeList(listData)



if __name__ == "__main__":
    main()
