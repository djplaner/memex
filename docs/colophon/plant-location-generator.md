---
title: Plant location generator
type: "note"
tags: 
    - colophon
    - computational-components
---

See also: [[computational-components]]

Early experiments with extracting information (about plants) from photos resulting in the design and development of the following:

## Evolving outcomes

### [plant-locations](../sense/landscape-garden/individual-plants/plant-location.html)

Google map with markers for each plant location. Currently hard-coded drawing on data from the front matter individual plant markdown files.

To do

- Integrate with standard process of updating memex

    i.e. a generator that extracts the first image from all the markdown files in the individual-plants folder and generate the JS/JSON file used by the map (~/sense/landscape-garden/individual-plants/plant-gps.js).

## Adding a plant

`addPlantPhoto.py` a command line util that takes the name of a photo in Photos and the name of an individual plant markdown file and adds the photo information to the individual plant's markdown file.

To do

- Need to tidy up the code and modularise it


## Work in progress

- [x] `addPlantPhoto` - Python script to extract metadata from Photos and add to individual plant markdown files.
- [ ] `plantPhotoMetadata` - mkdocs macro (Python script) to extract metadata from individual plant YAML frontmatter in markdown files and auto-add to markdown content.
- [ ] `woodDuckMeadowsMap` - mkdocs generator (Python script) to generate a map of the garden with plant locations marked.
- [ ] Explore offline-map-generation for a solution to the resolution issue with Leaflet maps.

    Currently working when given file paths. Need to change to work with the single plant frontmatter from markdown files.

- [ ] Add individual-plants files to `woodDuckGallery` 
- [ ] **IMPORTANT** Each single plant needs to have a well-defined lat,long not connected to photos.

## Purpose

Work on [[wood-duck-meadows]] will include a fair bit of planting. For some of these plants we'll want to track and manage their life cycle. This will include taking photos over time. The number and type of individual plants will be large making manual tracking insufficient. Linking photos to a specific plant and broader information about the individual and type of plant will be key.

Initial aims include:

1. Extract information (including GPS location) of plants from photos;
2. Store that information in markdown/yaml frontmatter associated with individual plants; and,

    Putting it into individual plant markdown files will allow for changes to plant names etc. General moving around of Markdown files.
3. Use that information in a number of other [[computational-components]].

    Examples to include:

    - Macros that help with maintaining information about individual plants, plant species, and zones.

        - \{\{ plantLocation("plant-name") \}\} - returns the location (lat,long) of a plant with a link to some sort of map.
    - Generating map-based representations of [[wood-duck-meadows]] indicating individual plant locations and providing subsequent access to plant information.

        - `woodDuckMeadowsMap()` - generate a markdown page that includes a map of the garden with plant locations marked.

## Workflow

1. Photos taken with GPS enabled.
2. Imported into Photos app.
3. `addPhoto <photosName> <plantName>
        - _photosName_ is identifier for Photos
        - _plantName_ is the filename for the individual plant's markdown file in memex
        - Adds YAML frontmatter for photo into markdown file (iff not there already)
        - exports appropriately the photo to the relevant pics folder
            `~/sense/landscape-garden/individual-plants/photos/{plantName}_{photoNumber}.jpeg`

At next `mkdocs`

- `plantPhotoMetadata.py` macro is available to be used. Will include photo metadata in the markdown.
    - Retrives and makes available YAML frontmatter from the nominated plant markdown file
- `woodDuckMeadowsMap.py` generator produces the `wood-ducks-plant-map.md` file
    - Loops through each individual plant markdown file using YAML frontmatter to populate

### Design 1

1. Photos of plants taken with GPS enabled.
2. Stored in Photos 
    - Add photos to zone-based albums. (not necessary)
    - Add title and captions. (useful)
3. Add a memex folder `individual-plants` to hold markdown files for individual plants.

    - Information about photos for individual plants stored in these files using YAML front matter.
    - Stored under tags `photo_${x}` where x is the number (order) of photo for the plant.

    - Information stored will include
        - full path/name for the photo in Photos - useful for Python to get back to the original photo
        - Title and caption information from Photos/exif
        - Location
        - Date taken
        - ?? figure out additional useful information
4. Use Python to extract GPS location and other metadata from photos.

    - `addPlantPhoto` is a Python util that takes Photos' name of the photo and the name of an individual plant and adds markdown information to the individual plant's markdown file.
    - Issue is that the Photos app can have multiple photos with the same name. Suggesting we need other parameters to uniquely identify the photo.



| Photo metadata | Memex equiv | 
| --- | --- |
| Title | Descriptive title used in figure |
| Caption | Alt tag for photo |
| Keywords | Name of markdown file (for the individual plant) into which to add/update the yaml front matter | 
| Lat, Long | Part of the yaml |

Markdown files ~/plants/individual/[keyword[0]]

Each individual plant can have multiple photos, each with their own yaml.
```yaml
photos:
    1:
        photos_path: ...
        latitude: -37.876
        longitude: 145.042
        caption: "The original island bunya pine when we started restoration"
        title: "The original island bunya pine"
    2:
        ...
```


## Development/exploration

### Python photo modules

Various older, specific modules for reading exif image data, but [Pillow](https://pillow.readthedocs.io/en/latest/index.html) appears to be the best supported.

[Tutorial on reading exif using Pillow](https://thepythoncode.com/article/extracting-image-metadata-in-python)

Reading exif and other associated data via PIL is harder and less well documented than I would've expected.

### Map generation

The [folium module](https://python-visualization.github.io/folium/latest/) provide Python access to the [Leaflet.js](https://leafletjs.com/) library. But there's an issue with the map providers available with leaflet not having sufficient resolution to meaningfully work. e.g. two plants too close together to interact with separately via the web page.

[Leaflet offline](https://github.com/allartk/leaflet.offline?tab=readme-ov-file) - JS that allows offline use of Leaflet with local map tiles. Not exactly the solution I'm looking for as it relies on a database to store the tiles

!!! abstract "Google maps or free versions"

    Begging the question whether or not Google maps might offer better resolution, without the need to pay. Do I feed the Google monster, or look further for alternatives?

    **Status** Feeding the monster

#### Free versions

- [Open Web Mapping course](https://www.e-education.psu.edu/geog585/node/519)


Web mapping frameworks that display a [tiled web map](https://en.wikipedia.org/wiki/Tiled_web_map). The Google Maps API is another web mapping framework.

- [Folium](https://python-visualization.github.io/folium/quickstart.html) and [Leaflet.js](https://leafletjs.com/)
- [OpenLayers](https://openlayers.org)

    Open source, Free BSD licence. Similar to Leaflet. Long term and active development.

- [Polymaps](http://polymaps.org/docs/)

    Javascript library. Not actively developed.

Sources for tiled web maps include

- [OSM (Open Street Map)](https://www.openstreetmap.org/#map=15/-27.54545/152.06518)

    Open and leveraging local/community-based input
- Bing 
- [MapBox](https://www.mapbox.com/)

    Open source and paid versions.
- [Stadia Maps](https://stadiamaps.com)

- [Protomaps](https://docs.protomaps.com)

    Opensource provision of a world map (based on OpenMaps) as a single file. Can be used with Leaflet and OpenLayers.

Satellite resolution

- [OpenMapTiles](https://www.maptiler.com/news/2017/12/openmaptiles-satellite/) at 1 to 2 metres per pixel - only available in some places, not relevant

    - Via [MapTiler](https://www.maptiler.com/satellite/#dates-and-resolution)
- [Redit question](https://www.reddit.com/r/QGIS/comments/q0su5b/what_are_some_freeforcommercialuse_satellite/)

- [Guide to buying/using satellite images](https://up42.com/blog/a-definitive-guide-to-buying-and-using-satellite-imagery)

Spatial resolution - size of one pixel on the ground.

| Resolution | Description |
| --- | --- |
| &lte; 50cm | Very high resolution |
| 50cm - 2m | High resolution |
| 2m - 20m | Medium resolution |
| &gt; 20m | Low resolution |

Providers

- [up42](https://up42.com) 

  - free imagery from 2017 onwards in up to 10m resolution
  - Market place selling other imagery 
    - [Pleiades Neo HD15](https://up42.com/marketplace/data/archive/pneo-hd15) - 15cm resolution
- DigitalGlobe
- Planet 
- Airbus
- [Copernicus dataspace](https://dataspace.copernicus.eu)
- [Top 10 sources for Australia](https://geopera.com/blog/free-sources-of-satellite-data)

#### Google Maps

- Had to sign up for a Google Maps API key, which included providing details for a credit card.
- [Details about cost](https://mapsplatform.google.com/resources/blog/build-more-for-free-and-access-more-discounts-online-with-google-maps-platform-updates/) - $3250 free per month
- [Google maps console](https://console.cloud.google.com/google/maps-apis/home;onboard=true?project=micro-mediator-279707) 
- [Maps Javascript API](https://developers.google.com/maps/documentation/javascript)
- [Map with javascript](https://developers.google.com/maps/documentation/javascript/adding-a-google-map)

Initial implementation

- [x] Use the [map with javascript](https://developers.google.com/maps/documentation/javascript/adding-a-google-map) model and add it to a hard-coded HTML file (plant-location.html)
- [ ] JSON import to get the plant locations
- [ ] Add [markers](https://developers.google.com/maps/documentation/javascript/advanced-markers/overview) for each plant location
- [ ] Use [marker clustering](https://developers.google.com/maps/documentation/javascript/marker-clustering) based on zones?

### Offline map generation

[Offline use of leaflet](https://davidrs.com/wp/phonegap-3-0-leaflet-offline-maps/) as basis for [Stackoverlow suggestion](https://davidrs.com/wp/phonegap-3-0-leaflet-offline-maps/) explained using these steps

1. Create map tiles
    - uses [Mobile atlas creator](https://sourceforge.net/projects/mobac/) to downlaod tiles to local file system
2. Setup HTML and Javascript
    - uses leaflet.js as map viewer

Exploring use of [Skywatch](https://intercom.help/skywatch-ab92e82e1a0a/en/articles/9151512-about-the-skywatch-standard-data-product)

Questions

- Is it possible to download tiles via other means and use Leaflet?

### Accessing OS X Photos app

Photos are currently stored in the Photos app. The [osxphotos module](https://github.com/RhetTbull/osxphotos?tab=readme-ov-file) seems to provide an answer.

- `osxphotos.PhotosDB` - connects to Photosdb
  - `photos` - retrieve photos using various queries
    - return a list of `PhotoInfo` objects
        - path
        - latitude, longitude
        - place
        - comments
        - labels
        - exif_info
        - `export()` - save photos to different path, numerous options



[//begin]: # "Autogenerated link references for markdown compatibility"
[computational-components]: computational-components "Computational components"
[wood-duck-meadows]: ../sense/landscape-garden/wood-duck-meadows "Wood duck meadows"
[//end]: # "Autogenerated link references"