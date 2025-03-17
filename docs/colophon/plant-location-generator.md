---
title: Plant location generator
type: note
tags: colophon, computational-components
---

See also: [[computational-components]]

Early experiments with extracting information (about plants) from photos resulting in the design and development of the following:

- [ ] `addPlantPhoto` - Python script to extract metadata from Photos and add to individual plant markdown files.
- [ ] `plantPhotoMetadata` - mkdocs macro (Python script) to extract metadata from individual plant YAML frontmatter in markdown files and auto-add to markdown content.
- [ ] `woodDuckMeadowsMap` - mkdocs generator (Python script) to generate a map of the garden with plant locations marked.

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

The [folium module](https://python-visualization.github.io/folium/latest/) provide Python access to the [Leaflet.js](https://leafletjs.com/) library. 

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