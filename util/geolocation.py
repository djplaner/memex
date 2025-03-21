"""
title: geolocation.py
purpose: Experiments in using Pillow to read exif data from images
"""

from PIL import Image, ExifTags, IptcImagePlugin
from PIL.ExifTags import TAGS

from pprint import pprint
import folium

import osxphotos
import exifread

HOME_LAT = -27.53831
HOME_LONG = 152.05599

def getLatLong(image_file_path):
    image = Image.open(image_file_path)
    imageData = {
        'title': "no title", 'caption': None, 'latitude': None, 'longitude': None,
        'path': image_file_path, 'Image ImageDescription': "No description",
        'Image DateTime': "No date"
    }

    with open(image_file_path, 'rb') as f:
        exif = exifread.process_file(f)
#        print("------ exif read")
#        for tag in tags.keys():
#            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#                print(f"**{tag}** = {tags[tag]}")
#        print("----- /end")

        for field in ( "Image ImageDescription", "Image DateTime"):
            if field in exif:
                print(f"{field} = {exif[field]}")
                imageData[field] = str(exif[field])
#    ifreadTags = [
#        "Image ImageDescription", "Image DateTime",
#    ]

#    print("--------- TAGS")
#    for tag in TAGS:
#        print(f"{tag} = {TAGS[tag]}")
#    print("------- END TAGS")

    if image is None:
        raise ValueError(f"Could not open image file {image_file_path}")

    #-- gets an instance of exif class
    info = image.getexif()
    iptc = IptcImagePlugin.getiptcinfo(image)

#    exifTranslate = {
#        "ImageDescription": 270,
#        "UserComment": 37510,
#        "XPTitle": 40091,
#        "ExifImageWidth": 40962,
#        "ExifImageLength": 40963,
#    }

#    pprint(info)
#    pprint(iptc)

#    for key in exifTranslate.keys():
#        print(f"--- testing {key} -- {exifTranslate[key]}")
#        print(f"    -- info {info[exifTranslate[key]]}")
#        if ExifTags.TAGS.get(exifTranslate[key]) in info:
#            print(f"{key}: {info[ExifTags.TAGS.get(exifTranslate[key])]}")

    # loop through exif tags
#   print("=================")
#    if iptc is not None:
#        print("---- iptc")
#        print(f"dict is type {type(iptc)}")
#        for tag in iptc.keys():
#            print(f"{tag} = {iptc[tag]}")
#        print(iptc)
#        print("------")
#    print(info)
#    print("=================")
#    quit()

    #-- get the title and caption from exif
    #    if ExifTags.TAGS.get(270) in info:
    #        print(f"Title: {info[ExifTags.TAGS.get(270)]}")
    #        imageData['title'] = info[ExifTags.TAGS.get(270)]

#    if ExifTags.TAGS.get(37510) in info:
#        print(f"Caption: {info[ExifTags.TAGS.get(37510)]}")
#        imageData['caption'] = info[ExifTags.TAGS.get(37510)]

#    if ExifTags.IFD.GPSInfo not in info:
#        print("No GPS data found")
#        return None

    gps_ifd = info.get_ifd(ExifTags.IFD.GPSInfo)
#    print(" -- GPS dict")
#    print(gps_ifd)
#    print(f" latref {gps_ifd[1]}")
#    print(gps_ifd.values())

    latitude = float(gps_ifd[2][0]) + float(gps_ifd[2][1]) / 60 + float(gps_ifd[2][2]) / 3600
    longitude = float(gps_ifd[4][0]) + float(gps_ifd[4][1]) / 60 + float(gps_ifd[4][2]) / 3600

    #-- check if latitude is S
    if gps_ifd[1] == 'S':
        latitude = -latitude

    imageData['latitude'] = latitude
    imageData['longitude'] = longitude

    print("-----------------")
    print("-----------------")
    pprint(imageData)
    print("-----------------")

    return imageData

def getPointsFromImages( images ):

    points = []

    for imagePath in images:
        print(f"------   Image: {imagePath}")
        imageData = getLatLong(imagePath)
#        print(imageData)

        if imageData is not None:
#            imageData = getExif(imageData)
            points.append( imageData )

    return points

def saveMap( points, mapPath ):

    map = folium.Map(location=[HOME_LAT, HOME_LONG], zoom_start=15, 
                     tiles="Esri.WorldImagery")
#                     tiles="Stadia.AlidadeSatellite")

    photoNames = [ "ficus", "dam clearing", "Oma's phone", "Sandy's phone"]
    count = 0
    for point in points:
        folium.Marker([point['latitude'], point['longitude']], 
                      popup=point["Image ImageDescription"]).add_to(map)
        count += 1
    map.save(mapPath)
    
def generateMapFromImages( ):
    images = [
        "/Users/davidjones/Downloads/Sandys/IMG_0324.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0325.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0326.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0327.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0328.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0330.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0331.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0332.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0334.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0335.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0336.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0337.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0339.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0344.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0345.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_0346.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_1179.jpeg",
        "/Users/davidjones/Downloads/Sandys/IMG_7435.jpeg",
    ]


    points = getPointsFromImages( images )

    pprint(points, indent=4)

    saveMap( points, "index.html")

#    for photo in photos:
#        print(photo.original_filename, photo.date, photo.title, photo.keywords, photo.comments ) 
#        print(f"  latitude: {photo.latitude}, longitude: {photo.longitude}")
#        print(f"  path: {photo.path}")
    
    
if __name__ == "__main__":

    generateMapFromImages()




