# publicationsPage.py
# - read content from My Publications in Zotero and write to 
#   share/My Publications.md

import re
from pyzotero import zotero

from simple_settings import settings

PAGE_TEMPLATE = """
# My Publications

A list of PUB_COUNT formal academic publications. My [Google Scholar Profile](http://scholar.google.com/citations?user=k8DkjXIqUl4J) has more detail

| Publication Type | Total |
| ---------------- | ----- |
"""

PUBLICATION_TYPE = {
    'book': 'Authored Book',
    'bookSection':'Book Chapter',
    'journalArticle':'Refereed Journal Paper',
    'conferencePaper':'Refereed Conference Paper',
    'presentation':'Presentation',
    'thesis': 'PhD Thesis'
}

PUBLICATION_ORDER = [ 'book', 'bookSection', 'thesis', 'journalArticle', 
            'conferencePaper','presentation']

zot = zotero.Zotero(settings.zoteroUserId, 'user', settings.zoteroAPIKey)

#---------------------------------------------------------
# return an array of full publication details
def getPublications():

    #-- get list of items in publications
    items = zot.publications()
#    for item in items: 
#        print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))

    return items

    #-- get more detail about each publication

#---------------------------------------------------------
# counts = calculateCounts( pubs, field)
# - given dict of publications, return a dict that gives the number of 
#   items of each field

def calculateCounts( pubs, field='itemType' ):
    counts = {}

    for item in pubs:
        if field not in item['data']:
            continue
        type = item['data'][field]
        if type not in counts:
            counts[type] = 0
        counts[type]+=1

    return counts

#------------------------------------------------------------
# list = getPubsField( pubs, field)
# - return a list containing just the field from the list of pubs

def getPubsField( pubs, field):
    pubsList = []

    for item in pubs:
        if field not in item['data']:
            continue
        pubsList.append(item['data'][field])

    return pubsList

#---------------------------------------------------------
# pubs = getYearsPubs( pubs, year)
# - give list of pubs and a year
# - return list of pubs from that year

def getYearsPubs( pubs, year ):
    yearPubs = []

    for item in pubs:
        if 'date' not in item['data']:
            continue

        print("-- %s" % item['data']['date'])

        if item['data']['date'] == year:
            yearPubs.append(item)

    return yearPubs

#--------------------------------------------------------------
# output = getPubsOutput( pubs )
# - given a list pubs, return a string show pubs

def getPubsOutput( pubs):

    itemKeys = getPubsField( pubs, "key")
    print("ITem keys %s" %itemKeys)

    outputString = ""
    for key in itemKeys:
        #zot.add_parameters( format="bib", style="apa")
        output = zot.items( itemKey= key, format="bib", style="apa")
        outputString = outputString + output.decode("utf-8")

    print("------------- ouput")
    print(outputString)
    return outputString
#    return "Had %s pubs" % len(pubs)

#--------------------------------------------------------------
# updateFile( types)
# - write to the file

def updateFile( pubs, types ):
    pubCount = len(pubs)

    markDown = PAGE_TEMPLATE.replace("PUB_COUNT",str(pubCount))

    #-- generate table of publication type counts
    for type in PUBLICATION_ORDER:
        if type not in types or type not in PUBLICATION_TYPE:
            continue
        markDown = markDown + "| %s | %s |\n" % (PUBLICATION_TYPE[type],types[type])
    markDown = markDown + "\n"

    #-- show the by the year complete display
    yearCounts = calculateCounts( pubs, 'date' )
    #-- just get the round years
    years = []
    for year in yearCounts.keys():
        print("-- %s" % year)
        result = re.match( '^[0-9][0-9][0-9][0-9]$', year)
        if result:
            years.append(year)

    print( years)

    years.sort( reverse = True)
    for year in years:
        markDown = markDown + "## %s\n" %year

        #-- loop through publications for the given year
        yearPubs = getYearsPubs( pubs, year)
        print(yearPubs)

        markDown = markDown + getPubsOutput( yearPubs)
        markDown = markDown + "\n\n"

    #-- write to the file
    with open( settings.myPubsFile, "w") as f:
        f.write( markDown)
    f.close()

#    print( markDown )



def main(): 
    pubs = getPublications()

    print( pubs[0]['data'].keys())


    #-- calculate counts of different types - straight python
    types = calculateCounts( pubs )
    print( types)

    updateFile( pubs, types)

    #-- display the annual list 
    #   - including display in format
    # https://pyzotero.readthedocs.io/en/latest/#read-api-methods
    # - zot.add_parameters( format="bib") or some such


if __name__ == "__main__":
    main()