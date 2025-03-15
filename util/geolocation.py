"""
title: geolocation.py
purpose: Experiments in using Pillow to read exif data from images
"""

from PIL import Image, ExifTags, IptcImagePlugin
from PIL.ExifTags import TAGS

import folium

HOME_LAT = -27.53831
HOME_LONG = 152.05599

def getLatLong(image_file_path):
    image = Image.open(image_file_path)
    imageData = {
        'title': "no title", 'caption': None, 'latitude': None, 'longitude': None,
        'path': image_file_path
    }
    if image is None:
        raise ValueError(f"Could not open image file {image_file_path}")

    #-- gets an instance of exif class
    info = image.getexif()
    iptc = IptcImagePlugin.getiptcinfo(image)

    # loop through exif tags
    print("=================")
    #print(image.info)
    if iptc is not None:
        print("---- iptc")
        print(f"dict is type {type(iptc)}")
        for tag in iptc.keys():
            print(f"{tag} = {iptc[tag]}")
        print(iptc)
        print("------")
    print(info)
    print("=================")

    #-- get the title and caption from exif
    if ExifTags.TAGS.get(270) in info:
        print(f"Title: {info[ExifTags.TAGS.get(270)]}")
        imageData['title'] = info[ExifTags.TAGS.get(270)]
    if ExifTags.TAGS.get(37510) in info:
        print(f"Caption: {info[ExifTags.TAGS.get(37510)]}")
        imageData['caption'] = info[ExifTags.TAGS.get(37510)]

    if ExifTags.IFD.GPSInfo not in info:
        print("No GPS data found")
        return None

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

    for point in points:
        folium.Marker([point['latitude'], point['longitude']], 
                      popup=point['title']).add_to(map)
    map.save(mapPath)
    
    
if __name__ == "__main__":
    images = [
        '/Users/davidjones/memex/docs/sense/landscape-garden/plants/images/honey-locust.jpeg',
        '/Users/davidjones/Downloads/honey-locust-copy.jpg',
        '/Users/davidjones/Downloads/Export/Ficus leaves from the roundabout.jpeg',
        '/Users/davidjones/Downloads/Export/dam-bank-clearing.jpeg'
    ]

    points = getPointsFromImages( images )

#    print(points)

    saveMap( points, "index.html")




