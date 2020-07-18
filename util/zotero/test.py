
from pyzotero import zotero

from simple_settings import settings


def main(): 
    zot = zotero.Zotero(settings.zoteroUserId, 'user', settings.zoteroAPIKey) 
    #items = zot.top(limit=5) 
    # items = zot.publications()
    # we've retrieved the latest five top-level items in our library
    # we can print each item's item type and ID
    for item in items:
        print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))


if __name__ == "__main__":
    main()