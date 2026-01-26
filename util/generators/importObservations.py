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

from lib.eBird import importeBird
from lib.iNaturalist import importiNaturalist

from pprint import pprint

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

if __name__ == "__main__":
    eBirdBirds = importeBird()
    pprint(eBirdBirds.to_dict(),indent=4)
    #-- create appropriate observation and species markdown files
    # return a dataFrame of bird observations from iNaturalist spreadsheet
    iNatBirds = importiNaturalist()

    birdObservations = mergeEBirdAndINatObservations(eBirdBirds, iNatBirds)
#    generateBirdLifeList(birdObservations)
