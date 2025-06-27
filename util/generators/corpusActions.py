"""
corpusActions.py 

Generator that (will eventually) perform numerous actions that rely on reading the entire corpus of notes. All done in one generator so that the grabbing the entire corpus is done once.

Actions include

- generateBackLinks

    Add backlinks to the front matter of each bubble 
        - backlinks
            - url: <absolute filepath to a bubble pointing to current>
              title: <title of the bubble> 
            - url: <absolute filepath to a bubble pointing to current>
              title: <title of the bubble>
    Displayed by Jinja template

 Also provides some utility functions

 - addYamlFrontMatter 

    Which adds YAML front matter to all bubbles that don't have it. Run only once

Limitations:

- Only counting wikilinks included in the linkDefs section of the bubble.
- Ignores other types of links e.g. [home](../index.md)

Problems

- Assumes all pages have YAML

"""

import json
import pathlib
import glob
import re
import yaml
import frontmatter
from pprint import pprint
import mkdocs_gen_files
from mkdocs.config import Config, load_config

## Global holds the MkDocs config entry for the docs folder
DOCS_FOLDER = ""
## Prefix added to URLs to match MkDocs configuration
# i.e. https://djon.es/**memex**/<URL>
PREFIX="/memex"
## Array of links to exclude from the backlinks
#  Expressed as a regex
EXCLUDE = [
    r"oldNAV\."
]

def generateAbsoluteLinks(markdownFile, linkDefs):
    """
    transform the relative links in linkDefs[<text>]['link'] into absolute links using
    the path to the markdown file as a reference point

    e.g. where 
        markdownFile = docs/share/blog/2025/a-new-day.md
        linkDefs = {
            '../../../colophon/colophon': {
                'text': 'About (colophon)',
                'description': 'About (colophon)'
            }
        }
        replace the link key to /colophon/colophon.html

    param markdownFile: the path to the markdown file
    param linkDefs: a dictionary of link definitions
    return: a dictionary of link definitions with absolute links
    """

    #-- Remove the markdown file name to get the current folder for the file
    location = markdownFile.rfind("/")
    currentFolder = markdownFile[:location]

    newLinkDefs = {}

    for link in linkDefs:
        # add .md to the link to refer to an actual file
        targetLink = link + ".md"
        # targetLink is relative, append it to current folder to provide a relative path to resolve
        path = f"{currentFolder}/{targetLink}"
        # resolve the path to an absolute path
        p = pathlib.Path(path)
        absPath = p.resolve()
        #-- Get an absolute path with the docs folder as the root
        absPath = str(absPath).replace(DOCS_FOLDER, "")

        newLinkDefs[absPath] = {
            'text': linkDefs[link]['text'],
            'description': linkDefs[link]['description']
        }

    return newLinkDefs

def extractLinkDefs(pageData):
    """
    Extract the link definitions from the content of the markdown file
    and add them to the pageData dictionary

    The links are relative to the path of the markdown file that contains them. They need to be transformed into a standard format that can be used as keys. Transform to absolute links relative to the docs directory.

    Link definitions are defined at the bottom of the cotent located between
    [//begin] and [//end] tags. Format is:
    [link text]: <relative link> "description"

    param pageData: a dictionary with 'content' and 'yaml' keys
    return: a dictionary with 'content', 'yaml', and 'linkDefs' keys
    - 'linkDefs' is a dictionary of dictionaries keyed on 'link' 
             { <link>: { 'text': <text>, 'description': <description> }}
    """

    # Find the start and end of the link definitions
    start = pageData['content'].find("[//begin]")
    end = pageData['content'].find("[//end]")

    # Extract the link definitions
    if start != -1 and end != -1:
        linkDefs = pageData['content'][start:end]
        #-- convert the string linkdefs into a dictionary
        # split the link definitions into lines
        linkDefs = linkDefs.split("\n")
        # remove the first and last lines 
        linkDefs = linkDefs[1:-1]
        pageData['linkDefs'] = {}
        for line in linkDefs:
            regex = r"\[(.*?)\]: (.*?) \"(.*?)\""
            match = re.match(regex, line)
            if match:
                #-- extract the link text, link, and description
                text = match.group(1)
                # remove any |.*$ from the text
                text = text.split("|")[0].strip()
                link = match.group(2)
                description = match.group(3)
                #-- add the link definition to the dictionary
                if link not in pageData['linkDefs']:
                    pageData['linkDefs'][link] = {}
                pageData['linkDefs'][link] = {
                    'text': text,
                    'description': description
                }

        # DO NOT Remove the link definitions from the content
        # Need to convert the links to absolute link, where / is the docs folder
        pageData['linkDefs'] = generateAbsoluteLinks(pageData['filePath'], pageData['linkDefs']) 
    else:
        pageData['linkDefs'] = []

    return pageData

def extractFileContent( file ):
    """
    Given path local to a markdown file, extract the file content and return as a dictionary of the form
      {
        "content": "content of file",
        "yaml": { _all yaml defined variables_ },
        "filePath": "/path/to/file.md"
        "linkDefs": { 
            '<text>':  { 'link': <link>, 'description': <description> },
            '<text2>': { 'link': <link2>, 'description': <description2> },
        }

    """

    pageData = {}
    with open(file, encoding="utf-8-sig") as f:
        bubble = frontmatter.load(f)

    pageData['content'] = bubble.content
    pageData['yaml'] = bubble.metadata
    pageData['filePath'] = str(file)

    pageData = extractLinkDefs(pageData)

    return pageData

def retrieveMemexBubbles():
    """
    Retrieve all memex bubbles from the memex folder and return them as a list of dicts

    Returns
    bubbles: dict of dicts
        <bubbleFilePath>: {
            'content': <content of bubble>,
            'yaml': <yaml metadata of bubble>,
            'filePath': <absolute path to bubble file>,
            'linkDefs': { <link>: { 'text': <text>, 'link': <link> } }
        }
    """
    bubbles = {}

    #-- get all files in the memex folder
    files = glob.glob(f"{DOCS_FOLDER}/memex/*.md")
    folder = pathlib.Path(DOCS_FOLDER)
    files = folder.rglob("*.md")

    for file in files:
        content = extractFileContent(file)
        if content is not None:
            localAbsPath = str(file).replace(DOCS_FOLDER, "")
            bubbles[localAbsPath] = content
        else:
            raise ValueError(f"Could not extract content from {file}")

    return bubbles

def configure():
    """
    Grab the mkdocs configuration and use it to configure the generator
    """

    config = load_config("mkdocs.yml")

    #-- check for docs_dir in config
    if 'docs_dir' in config:
        global DOCS_FOLDER
        DOCS_FOLDER = config['docs_dir']
    else:
        raise ValueError("No docs_dir found in mkdocs configuration")

    return config

def generateBackLinks(bubbles: dict):
    """
    Generate a data structure that contains details of the backlinks to each bubble

    parameters
    bubbles: dict of dicts contents of all Foam bubbles

    returns
    backlinks: dict of dicts
        {
            <bubbleFilePath>: { same key as used in bubbles
                { 
                    <absFilePathOfPageLinkingTobubbleFilePath?>:
                    <details of the bubble for this path>,
                   ... 
                }
            }
            ...
        }
    
    """

    backLinks = {}
    for file in bubbles.keys():
        backLinks[file] = {}

    for file in bubbles.keys():
        # extract all bubble links (links to other bubbles) from the bubble
        # TODO needs to access the linkDefs and perhaps transform them
        ## bubbleLinks = extractBubbleLinks(bubble['content'])

        bubble = bubbles[file]

        ## Only generate backlinks for pages that aren't EXCLUDED
        if any(re.search(pattern, bubble['filePath']) for pattern in EXCLUDE):
            continue

        # for each bubbleLink, add it to the backLinks dict
        for destinationPath in bubble['linkDefs']:
            sourcePath = f'{bubble["filePath"].replace(DOCS_FOLDER, "")}'
            #sourcePath = f'{PREFIX}{bubble["filePath"].replace(DOCS_FOLDER, "")}'
            #-- 
            if destinationPath not in backLinks:
                backLinks[destinationPath] = {}
            backLinks[destinationPath][sourcePath] = bubble

    return backLinks

def saveBubble(bubble:dict):
    """
    Save a bubble to the file system

    parameters
    bubble: dict - a dictionary containing the bubble content, yaml metadata, and file path
        {
            'content': <content of bubble>,
            'yaml': <yaml metadata of bubble>,
            'filePath': <absolute path to bubble file>
            'linkDefs': { <link>: { 'text': <text>, 'link': <link> } }
        }
    """

    filePath = bubble['filePath'].replace(f"{DOCS_FOLDER}/", "")

    #with open(bubble['filePath'], 'w', encoding="utf-8-sig") as f:
    with mkdocs_gen_files.open(filePath, 'w', encoding="utf-8-sig") as f:
        f.write("---\n")
        f.write(yaml.dump(bubble['yaml']))
        f.write("---\n")
        f.write(bubble['content'])

    mkdocs_gen_files.set_edit_path(filePath, "corpousActions.py")

def extractTitleFromContent(content : str):
    """
    Given the markdown content of a bubble, extract the title from the content.
    It will be the first heading 1 title "# title" in the content.

    Parameters
    content: str - the content of the bubble
    title: str - the title of the bubble, or "No title found" if no title is found
    """

    titleRegEx = r"^#\s*(.*)$"

    title = re.match(titleRegEx, content, re.MULTILINE)

    if title:
        return title.group(1) 
    else: 
        return "No title found"
    

def updateFrontMatterBackLinks(bubbles, backLinks):
    """
    Loop through all of the backlinks and update FrontMatter backlink
    information if required

    parameters
    bubbles: dict of dicts - all of the bubble content 
       keyed on the file path of the destination bubble
    backLinks: dict of dicts - backlinks to each bubble
        keyed on the file path fo the source bubble

    TODO 
    - If/how to check if the FrontMatter should be updated

    Parameters
    backLinks: dict of dicts - contains details about all backlinks
        {
            <bubbleFilePath>: {
                { 
                    <absFilePathOfPageLinkingTobubbleFilePath?>:
                    <details of the bubble for this path>,
                   ... 
                }
            }
            ...
        }
    """

    # Go through each of the bubbles for which we've recorded
    # backlinks
    # - destinationFilePath is file path of the bubble the back links
    #   are pointing to
    for destinationFilePath in backLinks.keys():
#    for destinationFilePath in ['/seek/stretching-educations-iron-triangle.md']:
        #-- construct a array of dicts to add to the bubbles[destinationFilePath]['yaml'] aka frontmatter
        backlinks = []
        # destinationPath = /seek/stretching-educations-iron-triangle.md
        #-- loop through all the backlinks
        for sourceLink in backLinks[destinationFilePath].keys():

            #-- sourceLink is the absolute path to the bubble linking to the destination bubble, but it has PREFIX prepended to it

            #-- calculate the title of the source bubble, complicated
            #   because not all bubbles have frontmatter with titles
            # - default try the description from linkDefs
            # - But start with default
            title = "No given title"
            # Run sourceLink (a URL) to a bubble file path by removing WWW PREFIX 
            #fileLink = sourceLink.replace(PREFIX, "")
            fileLink = re.sub( rf"^{PREFIX}", "", sourceLink)

            title = "Unknown title"
            if 'title' in bubbles[fileLink]['yaml']:
                title = bubbles[fileLink]['yaml']['title']
            else:
                title = extractTitleFromContent(bubbles[fileLink]['content'])

            backlinks.append({
                'url': sourceLink.replace(".md", ".html"),
                'title': title
            })

        #-- add the backlinks to the frontmatter of the front matter 
        # Not sure if this test is all that important, given that changes
        # might appear to be happening in memory
        if destinationFilePath not in bubbles:
            continue
            raise ValueError(f"Destination file path {destinationFilePath} not found in bubbles")
        if backlinks == bubbles[destinationFilePath]['yaml'].get('backlinks', []):
            continue
        bubbles[destinationFilePath]['yaml']['backlinks'] = backlinks

        saveBubble(bubbles[destinationFilePath])

def addYamlFrontMatter(bubbles):
    """
    Some bubbles may not have front matter, so add it if it doesn't exist.

    This is a clean up method. Should only need to be run once.

    Parameters
    bubbles: dict of dicts - all of the bubble content 
       keyed on the file path of the destination bubble
    """

    for filePath in bubbles.keys():
        #-- ignore any file that already has YAML with title
        if 'yaml' in bubbles[filePath]:
            if 'title' in bubbles[filePath]['yaml']:
                continue

        bubbles[filePath]['yaml'] = {}
        bubbles[filePath]['yaml']['title'] = extractTitleFromContent(bubbles[filePath]['content'])

        #-- remove the title from the content
        titleRegEx = rf"^# {bubbles[filePath]['yaml']['title']}\s*$"
        bubbles[filePath]['content'] = re.sub(
            titleRegEx, "", bubbles[filePath]['content'], count=1, flags=re.MULTILINE )
        #-- remove any leading newlines
        bubbles[filePath]['content'] = bubbles[filePath]['content'].lstrip("\n")

        # save the new bubble
        saveBubble(bubbles[filePath])

def moveImages(bubbles):
    """
    Modify the image URLs in bubbles to point to https://djon.es/assets/memex/<imagePath>/<fileName>
    - where <imagePath> is the path to the image relative to the docs folder
    """

    for filePath in bubbles.keys():
        imgLinks = re.findall(r"!\[.*?\]\((.*?)\)", bubbles[filePath]['content'])
        print(f"Found {len(imgLinks)} image links in {filePath}")
        if len(imgLinks) == 0:
            continue
        for imgLink in imgLinks:
            #-- if the image link is already an absolute link, skip it
            if imgLink.startswith("http"):
                continue

            folderPath = pathlib.Path(filePath).parent
            absImgLink = f"https://djon.es/assets/memex{folderPath}/{imgLink}"

            print(f"    - {imgLink} abs link: {absImgLink}")
            bubbles[filePath]['content'] = bubbles[filePath]['content'].replace(
                f"({imgLink})", f"({absImgLink})")

        #-- save the modified bubble
        saveBubble(bubbles[filePath])

def generateGraphJson(backLinks, bubbles):
    """
    Generate a JSON file that contains the backlinks in a format that can be used by a graph visualization library

    Parameters
    backLinks: dict of dicts - backlinks to each bubble
        keyed on the file path fo the source bubble
    bubbles: dict of dicts - all of the bubble content
    """

    graphData = {
        "nodes": [],
        "edges": []
    }

    #-- add the nodes for the bubbles
    x = 1
    y = 1
    for filePath in bubbles.keys():
#        print(f"Processing {filePath}")
#        pprint(bubbles[filePath])
#        input("Press Enter to continue...")
        #-- add the node for the destination bubble
        # 'id':
        # 'name': <name of the bubble>
        # 'value': <path>
        graphData['nodes'].append({
            'id': filePath,
            'x': x, 'y': y,
#            'value': filePath,
            'label': bubbles[filePath]['yaml'].get('title', 'No title found')
        })
        x+=1
        y+=1

    #-- add the nodes for the backlinks
    # {
    #     destinationFilePath: {
    #         linkDefs:{
    #             sourceLink: { 'description', 'text' }
    #        }
    #    }   
    # }
    edgeId = 1
    for destinationFilePath in backLinks.keys():
#        print("-------------------------")
#        pprint(f"Processing backlinks for {destinationFilePath}")
#        pprint(backLinks[destinationFilePath].keys())
#        input("1) Press Enter to continue...")
        # continue if there are no linkDefs for this destination
        for sourceLink in backLinks[destinationFilePath].keys():
#            print(f"    - {sourceLink} -> {destinationFilePath}" )
            graphData['edges'].append({
                'id': f"{edgeId}",
                'source': sourceLink,
                'target': destinationFilePath
            })
            edgeId += 1
#        input("Press Enter to continue...")

    #-- check the edges all have source and target
    for edge in graphData['edges']:
        if 'source' not in edge or 'target' not in edge:
            pprint(edge)
            raise ValueError(f"Edge {edge} does not have source or target")

    #-- check that each edge source has a corresponding node
    for edge in graphData['edges']:
        if edge['source'] not in [node['id'] for node in graphData['nodes']]:
            raise ValueError(f"Edge {edge} has source {edge['source']} that does not exist in nodes")

    #-- save the graph data to a JSON file
    with open(f"{DOCS_FOLDER}/colophon/graph.json", 'w', encoding="utf-8-sig") as f:
        json.dump(graphData, f, indent=4, ensure_ascii=False)
        #yaml.dump(graphData, f, allow_unicode=True)

"""
Main entry point for the generator
"""

config = configure()

bubbles = retrieveMemexBubbles()
#pprint(bubbles)
#input("Press Enter to update front matter...")
#addYamlFrontMatter(bubbles)
backLinks = generateBackLinks(bubbles)
#pprint(backLinks)
#input("Press Enter to update front matter backlinks...")

#updateFrontMatterBackLinks(bubbles, backLinks)
#moveImages(bubbles)
#generateGraphJson(backLinks, bubbles)
