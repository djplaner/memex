"""
FILE:   woodDuck.py
PURPOSE: Use mkdocs-gen-file to generate a page containing all photos from three
 Wood duck meadows folders 
 - zones
 - plants
 - individual-plants
"""

import re
import glob
import mkdocs_gen_files
import logging
import frontmatter
import markdown
from bs4 import BeautifulSoup
from pprint import pprint

# logger = logging.getLogger("woodDuck")

# open calls using mkdocs-gen-files inherently uses docs
# DOC_FOLDER = "use mkdocs-gen-files to get docs folder"
GARDEN_FOLDER = "sense/landscape-garden/"
# GARDEN_FOLDER = ""
# PLANTS_PATH = f"{GARDEN_FOLDER}plants/"
PLANTS_PATH = "plants/"
DOCS_FOLDER = "/Users/davidjones/memex/docs/"
PLANTS_FOLDER = f"{DOCS_FOLDER}sense/landscape-garden/plants/"
INDIVIDUAL_PLANTS_FOLDER = f"{DOCS_FOLDER}sense/landscape-garden/individual-plants/"
INDIVIDUAL_PLANTS_PATH = "individual-plants/"


def retrieveZonePages(gardenFolder=GARDEN_FOLDER):
    """
    Generate array of hashes for all pages in GARDEN_FOLDER/NAV.md
    { 
        title: "", path: "relativePath", content: "raw content",
        html: "",
        figures: hash of hashes with figure info
    }
    """
    zoneNav = f"{gardenFolder}NAV.md"
#    lines = []
    pages = []
    linePattern = re.compile(r"^ *\* +\[([^\]]+)\]\(([^)]+)\)$")
    with mkdocs_gen_files.open(zoneNav, "r") as f:
        for line in f:
            # parse out line format into hash
            #   * [page-title](path)
            #   { page-title: "", path: "" }
            #   append hash to array
            match = linePattern.match(line)
            if (match):
                # lines.append({ "title": match.group(1), "path": match.group(2) })
                # path has just the name of the file
                relativePath = match.group(2)
                filePath = f"{DOCS_FOLDER}{GARDEN_FOLDER}{relativePath}"
                pageData = extractFileContent(filePath)
                figures = extractFigures(pageData['html'])
                pages.append(
                    {
                        "title": pageData['yaml']['title'],
                        "path": relativePath,
                        "content": pageData['content'],
                        "html": pageData['html'],
                        "figures": figures
                    })
    return pages


def generatePage(zonePages, plantsPages, individualPlantPages):
    """
    Write the wood-duck-gallery.md file, adding three sections. One each for zone, plants, and individual plants
    """

    with mkdocs_gen_files.open("sense/landscape-garden/wood-duck-gallery.md", "w") as f:
        f.write(f"""---
title: Wood duck meadows gallery
type: gallery
tags:
    - wood-duck-meadows
    - gallery
backlinks:
    - url: /memex/sense/landscape-garden/wood-duck-meadows.html
      title: Wood duck meadows
---

A dynamically generated gallery of all the photos from the pages associated with the zones and plants of [[wood-duck-meadows]]. An early exploration into integrating "[[computational-components]]" into the site.

!!! info "How to use the gallery"

    1. Scroll down the page to view smaller images and links to the original page holding the photo.

    2. Click on a photo to enter photo gallery mode which displays full size images and to click left/right through all the photos.


## Zones

""")

        for page in zonePages:
            f.write(f"""

### [{page['title']}]({page['path']})

                    """)
            addImages(f, page['title'], page['figures'])
#            f.write(f"- **Title `{page['title']}` path `{page['path']}`**\n")

        f.write(f"""
## Plants

""")
        for page in plantsPages:
            # -- skip if page['figures'] is empty
            if len(page['figures']) == 0:
                continue
            f.write(f"""

### [{page['title']}]({page['path']})

""")

            addImages(f, page['title'], page['figures'])

        f.write(f"""
## Individual Plants

""")
        for page in individualPlantPages:
            # -- skip if page['figures'] is empty
            if len(page['figures']) == 0:
                continue
            f.write(f"""
                    
### [{page['title']}]({page['path']})

""")

            addImages(f, page['title'], page['figures'])


def addImages(f, pageTitle, figures):
    """
    Given a file handle and hash of hashes representing figures 
    convert figure information into relevant markdown

    Called from generatePage
    """

    for imagePath in figures:
        f.write(f"""
<figure markdown>
![{figures[imagePath]['alt']}]({figures[imagePath]['image_path']}){{data-title="{pageTitle}" data-description="{figures[imagePath]['alt']}"}}
<caption>{figures[imagePath]['caption']}</caption>
</figure> 
""")


def retrievePlantsPages(plantsFolder=PLANTS_FOLDER):
    """
    Generate array of hashes for all pages from a given folder. By default looking in the PLANTS_FOLDER and other folders as called (only INDIVIDUAL_PLANTS_FOLDER at present)
    { page-title: "", path: "" }
    """

    files = glob.glob(f"{plantsFolder}*.md")
    pages = []

    for file in files:
        # -- remove DOCS_FOLDER from file
        path = file.replace(DOCS_FOLDER, "")
        # remove the landscape-garden path as well
        # Gallery is now in this folder, hence prefix is not needed
        path = path.replace("sense/landscape-garden/", "")
        pageData = extractFileContent(file)
        if plantsFolder == PLANTS_FOLDER:
            figures = extractFigures(pageData['html'], True)
        elif plantsFolder == INDIVIDUAL_PLANTS_FOLDER:
            figures = extractFigures(pageData['html'], False, True)
        print(f"--- plant file {file}")
        if "title" not in pageData['yaml']:
            pprint(pageData['yaml'], indent=4)
            print(f"--- no title in {file}")
            raise Exception(
                f"--- no title in {file} - check the front matter for the title")
        pages.append(
            {
                "title": pageData['yaml']['title'], "path": path,
                "content": pageData['content'],
                "html": pageData['html'],
                "figures": figures
            })
#        title = fMatter['title']
#        pages.append({ "title": title, "path": path, "frontMatter": fMatter })

    return pages


def extractFigures(html, PLANTS=False, INDIVIDUAL_PLANTS=False):
    """
    Given some content in HTML format, return a hash of hashes keyed on path to the figure.
    One hash for each figure in the content.

    Called three times from each of the retrieve functions. Each one sets the boolean flags to decide how image URLs are modified.

    {
        "plants/images/pepper-before-after-small.jpeg": {
            "alt": "Pepper before and after",
            "caption": "Pepper before and after"
            "path": "plants/images/pepper-before-after-small.jpeg"
        }
    }
    """

    figures = {}
    soup = BeautifulSoup(html, 'html.parser')

    # -- extract all figure tags from html
    figureTags = soup.find_all('figure')

    imageRE = re.compile(r"!\[(.*)\]\((.*)\)")
    captionRE = re.compile(r"<caption>(.*)</caption>")

    for figureTag in figureTags:
        """
        Each figure tag should follow the format
        <figure markdown="">
        ![alt](image_path)
        <caption>caption</caption>
        </figure>
        """
        figureComponents = {
            "alt": "",
            "image_path": "",
            "caption": ""
        }
        # extract alt and image_path
        match = imageRE.search(str(figureTag))
        if match:
            figureComponents['alt'] = match.group(1)
            figureComponents['image_path'] = match.group(2)
            # if image_path isn't a compete URL, prepend PLANTS_PATH
            if not figureComponents['image_path'].startswith("http"):
                if (PLANTS):
                    figureComponents['image_path'] = f"{PLANTS_PATH}{figureComponents['image_path']}"
                elif (INDIVIDUAL_PLANTS):
                    figureComponents['image_path'] = f"{INDIVIDUAL_PLANTS_PATH}{figureComponents['image_path']}"

        # extract the caption
        match = captionRE.search(str(figureTag))
        if match:
            figureComponents['caption'] = match.group(1)

        if figureComponents['image_path'] != "":
            figures[figureComponents['image_path']] = figureComponents

    return figures

def extractFileContent(path):
    md = markdown.Markdown(extensions=['meta'])
    pageData = {}
    with open(path, encoding="utf-8-sig") as f:
        post = frontmatter.load(f)

    pageData['content'] = post.content
    pageData['yaml'] = post.metadata
    pageData['html'] = md.convert(pageData['content'])

    return pageData

def extractXXFileContent(path):
    """
    Given full path to DOCS_FOLDER for a markdown file, extract the file content and return it as a hash
    {
        "content": "content of file",
        "yaml": { _all yaml defined variables_ },
        "html": "content of file converted to HTML
    }
    """
    md = markdown.Markdown(extensions=['meta'])
    pageData = {}
    with open(path, encoding="utf-8-sig") as f:
        pageData["content"] = f.read()
        html = md.convert(pageData["content"])
        pageData['yaml'] = md.Meta
        pageData['html'] = html

        for key in pageData['yaml'].keys():
            # if key is a list, get the first item
            if isinstance(pageData['yaml'][key], list):
                pageData['yaml'][key] = pageData['yaml'][key][0]
            pageData['yaml'][key] = pageData['yaml'][key].lstrip(
                '\"').rstrip('\"')

    return pageData


def generator():
    """
    Main harness for wood duck generator
    """

    # Generate array of hashes for all pages (lines) in GARDEN_FOLDER/NAV.md
    # { title: "", path: "" }
    zonePages = retrieveZonePages()
    # Generate array of hashes for all pages in PLANTS_FOLDER
    # excluding some specific ones
    # { page-title: "", path: "" }
    plantPages = retrievePlantsPages()
    individualPlantPages = retrievePlantsPages(INDIVIDUAL_PLANTS_FOLDER)

    generatePage(zonePages, plantPages, individualPlantPages)

    # Generate hash (on zone page title) of array of hashes (photo details)
    # { alt-tag: "", path: "", caption: ""}
#    zonePhotos = retrieveZonePhotos(zonePages)
    # for each file
    #   extract <figure markdown> from file

    # { alt-tag: "", path: "", caption: ""}
#    plantPhotos = retrievePlantPhotos(plantPages)
    # use duplicates to indicate duplicates as required
    # generate a hash (keyed on photo path) of hashes (photo details)
    # { alt-tag: "", path: "", caption: ""}
#    duplicatePhotos = detectDuplicates(zonePhotos, plantPhotos)

    # Create the file using mkdoc-gen-files
#    generateGallery(zonePages, plantPages, zonePhotos,
#                plantPhotos, duplicatePhotos)
    # Add boilerplate template to file
    # for each page in zonePages
    #   Add zonePage boilerplate


# if __name__ == "__main__":
#    generator()

generator()
