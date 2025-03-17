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
"""

import osxphotos
from osxphotos.cli import query_command, verbose

from pprint import pprint


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

    return photos

def exportPhoto(photo):

    exportOptions = osxphotos.ExportOptions(
       convert_to_jpeg=True, 
       jpeg_quality=0.5, 
       update=True, 
       overwrite=True,
       location=False, 
       exiftool=True,
       use_photos_export=True
    )
    exporter = osxphotos.PhotoExporter( photo[0] )
    exporter.export( dest="/Users/davidjones/downloads/", filename="testing-small", options=exportOptions )



if __name__ == "__main__":
    #-- find the photo
    photo = findPhoto("IMG_2590.HEIC")

    #-- extract the configuration information

    #-- export the photo to the relevant directory
    exportPhoto(photo)

