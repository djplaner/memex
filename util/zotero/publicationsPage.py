# publicationsPage.py
# - read content from My Publications in Zotero and write to 
#   share/My Publications.md
from pyzotero import zotero

from simple_settings import settings

#---------------------------------------------------------
# return an array of full publication details
def getPublications():

    #-- get list of items in publications
    zot = zotero.Zotero(settings.zoteroUserId, 'user', settings.zoteroAPIKey)
    items = zot.publications()
#    for item in items: 
#        print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))


    return items

    #-- get more detail about each publication

def main(): 
    pubs = getPublications()

    print( pubs[0]['data'].keys())


if __name__ == "__main__":
    main()