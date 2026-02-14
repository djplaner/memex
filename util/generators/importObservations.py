"""
importObservations.py

Read data files from external sources (eBird and iNaturalist) and create observations as individual markdown files. Separating out the subject of the observation (bird, plant)

Input:
- eBird
    - eBird CSV file located with path ~/memex_data/ebird.csv
    - images with filenames matching eBird sessionIds  
    ~/assets/memex/sense/birdwatching/images/<speciesName>/<sessionId>(_<count>).jpeg
- iNaturalist
    - CSV file ~/memex_data/iNaturalist.csv

iNaturalist and eBird code handled by separate libraries

Output:
- Observations are placed into ~/memex/docs/sense/Observations/<subject-type>/<commonName>/<uniqueId>.md

Connections:
- indexed by ~/memex/docs/sense/Observations/<subject-type>-life-list.md via a macro


Checks:
- Are there any images related to the session
- Is there a page for the bird - if not create it

Output:
- Markdown files in ~/memex/docs/sense/Observations/bird-observations/<species>-<sessionId>.md
- Content example below
- Markdown file for bird species if not already present in
    ~/memex/docs/sense/birdwatching/


"""

import sys
sys.path.append("/Users/davidjones/memex/util")
from pathlib import Path
from pprint import pprint

from lib.eBird import importeBird
from lib.iNaturalist import importiNaturalist
from lib.observations import filterObservations, displayObservationsIndex
from corpus import corpus

HOME_FOLDER="/Users/davidjones"
LIFE_LIST_DETAILS = {
    'plant': {
        'path': Path(f"{HOME_FOLDER}/memex/docs/sense/Observations/plant-life-list.md"),
        'title': "Plant life list"
    },
    'bird': {
        'path': Path(f"{HOME_FOLDER}/memex/docs/sense/Observations/bird-life-list.md"),
        'title': "Bird life list"
    },
    'other-fauna': {
        'path': Path(f"{HOME_FOLDER}/memex/docs/sense/Observations/other-fauna-life-list.md"),
        'title': "Other-Fauna life list"
    }
}

def mergeEBirdAndINatObservations(eBirdBirds, iNatBirds):
    """
    Merge eBird and iNaturalist bird observations into a dict keyed on species name
    with the values


    :param eBirdBirds: DataFrame
        DataFrame containing eBird bird observations
    :param iNatBirds: DataFrame
        DataFrame containing iNaturalist bird observations
    :return: DataFrame
        DataFrame containing merged bird observations
    """
    import pandas as pd

    #-- concatenate the two dataframes
    birdObservations = pd.concat([eBirdBirds, iNatBirds], ignore_index=True)

    #-- sort by date observed
    birdObservations = birdObservations.sort_values(by=['date_observed'], ascending=False)

    #-- generate observation markdown files
    from lib.eBird import generateEBirdObservationMDs
    from lib.iNaturalist import generateiNatObservationMDs

    generateEBirdObservationMDs(eBirdBirds)
    generateiNatObservationMDs(iNatBirds)

    return birdObservations

def generateLifeLists():
    """
    Generate the life lists for all of the LIFE_LIST_PATHS by extract all the observations for
    each species type from the markdown files (bubbles)
    """

    #-- get all the memex bubbles
    bubbles = corpus()

    #-- generate life lists for each species type
    for species in LIFE_LIST_DETAILS.keys():
        ##-- generate markdown for life list for <species>
        observations = filterObservations( bubbles, { "observation-type": species } )
        lifeListMarkdown = displayObservationsIndex( observations, { 'observation-type': species} )

        print(lifeListMarkdown)
        print()
        print(f"Found bubble for {LIFE_LIST_DETAILS[species]['title']}")
        input("Press enter to continue...")

        ##-- update the life list file by replace the life list markdown
        lifeListBubble = bubbles.get_bubbles_by_frontmatter( { "title": LIFE_LIST_DETAILS[species]['title'] } )
        if len(lifeListBubble) == 0:
            print(f"No bubble found for {LIFE_LIST_DETAILS[species]['title']}")
            continue
        pprint(lifeListBubble[0],indent=4)
        #-- need to update the life list markdown in lifeListBubble[0] with lifeListMarkdown

        #-- save the updated lifeListBubble[0]
        bubbles.saveBubble( lifeListBubble[0] )

        #-- need to add linkdefs (probably - without removing existing)
        # linkDefs are stored in the bubble's dictionary's linkDefs key. It's a dict keyed on
        # the full path  - going to be hard to update

if __name__ == "__main__":

    ## import and generate individual observation files from eBird and iNaturalist
    eBirdObs = importeBird()
    iNatObs = importiNaturalist()

#    generateLifeLists()
    


        #-- based on params, call a different view

        

    ## combine eBirdObs and iNatObs
#    observations = mergeObservations( { "ebird": eBirdObs, "inat": iNatObs })
#    generateBirdLifeList(birdObservations)
