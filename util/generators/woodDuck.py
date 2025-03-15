"""
FILE:   woodDuck.py
PURPOSE: Use mkdocs-gen-file to generate a page containing all photos from Wood duck meadows zones and plants
"""

import re
import glob
import mkdocs_gen_files
import logging
#import frontmatter
import markdown
from bs4 import BeautifulSoup

logger = logging.getLogger("woodDuck")

# open calls using mkdocs-gen-files inherently uses docs
#DOC_FOLDER = "use mkdocs-gen-files to get docs folder"
GARDEN_FOLDER = "sense/landscape-garden/"
#GARDEN_FOLDER = ""
#PLANTS_PATH = f"{GARDEN_FOLDER}plants/"
PLANTS_PATH = "plants/"
DOCS_FOLDER="/Users/davidjones/memex/docs/"
PLANTS_FOLDER = f"{DOCS_FOLDER}sense/landscape-garden/plants/"
#PLANTS_FOLDER = "plants/"


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
                #lines.append({ "title": match.group(1), "path": match.group(2) })
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

def generatePage(zonePages, plantsPages):
    
    with mkdocs_gen_files.open("sense/landscape-garden/wood-duck-gallery.md", "w") as f:
        f.write(f"""# Wood duck meadows gallery

See also: [[wood-duck-meadows]]

A dynamically generated gallery of all the photos from the pages associated with the zones and plants of [[wood-duck-meadows]]. An early exploration into integrating "[[computational-components]]" into the site.

View the photos either by:

1. Scrolling down the page.

    Smaller images, but with links to the original pages.
2. Click on a photo and move left/right through all photos.

    Full width images.

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
            #-- skip if page['figures'] is empty
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
    Generate array of hashes for all pages in PLANTS_FOLDER
    { page-title: "", path: "" }
    """

    files = glob.glob(f"{plantsFolder}*.md")
    pages = [ ]

    for file in files:
        #-- remove DOCS_FOLDER from file
        path = file.replace(DOCS_FOLDER, "")
        # remove the landscape-garden path as well
        # Gallery is now in this folder, hence prefix is not needed
        path = path.replace("sense/landscape-garden/", "")  
        pageData = extractFileContent(file)
        figures = extractFigures(pageData['html'], True)
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

def extractFigures(html, PLANTS=False):
    """
    Given some content in HTML format, return a hash of hashes keyed on path to the figure.
    One hash for each figure in the content.
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

    #-- extract all figure tags from html
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
                if ( PLANTS):
                    figureComponents['image_path'] = f"{PLANTS_PATH}{figureComponents['image_path']}"
                    
        # extract the caption
        match = captionRE.search(str(figureTag))
        if match:
            figureComponents['caption'] = match.group(1)

        if figureComponents['image_path'] != "":
            figures[figureComponents['image_path']] = figureComponents

    return figures


def extractFileContent(path):
    """
    Given full path to DOCS_FOLDER for a markdown file, extract the file content and return it as a hash
    {
        "content": "content of file",
        "yaml": { _all yaml defined variables_ },
        "html": "content of file converted to HTML
    }
    """

    md = markdown.Markdown(extensions = ['meta'])
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
            pageData['yaml'][key] = pageData['yaml'][key].lstrip('\"').rstrip('\"')

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
    generatePage(zonePages, plantPages)

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


#if __name__ == "__main__":
#    generator()

generator()
    
