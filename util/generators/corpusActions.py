"""
corpusActions.py 

Generator that (will eventually) perform numerous actions that rely on reading the entire corpus of notes. All done in one generator so that the grabbing the entire corpus is done once.

See https://djon.es/memex/colophon/integrate-backlinks-automatically-onto-pages.html

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
from mkdocs.structure.files import File, Files

bubbles = {}

## Global holds the MkDocs config entry for the docs folder
FULL_DOCS_FOLDER = "/Users/davidjones/memex/docs/"
MEMEX_FOLDER = "/Users/davidjones/memex/"
DOCS_FOLDER = ""  # will be set in configure function
## Prefix added to URLs to match MkDocs configuration
# i.e. https://djon.es/**memex**/<URL>
PREFIX="/memex"
## Array of links to exclude from the backlinks
#  Expressed as a regex
EXCLUDE = [
    r"oldNAV\.",
    r"NAV\.",
    r"/reveal.js",
    r"/landscape-garden/work-files/"
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
    location = f"/{markdownFile}".rfind("/")
    currentFolder = markdownFile[:location]

#    print(f"Generating absolute links for {markdownFile} in folder {currentFolder}")
#    input("Press Enter to continue...")

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

        #-- remove "/Users/davidjones/memex/" from front of absPath
        absPath = absPath.replace("/Users/davidjones/memex/", "")
        #-- if absPath starts with /, remove it
        if absPath.startswith("/"):
            absPath = absPath[1:]

#        print(f"Link {link} -> {absPath}")

        newLinkDefs[absPath] = {
            'text': linkDefs[link]['text'],
            'description': linkDefs[link]['description']
        }

    return newLinkDefs

def extractLinkDefs(pageData):
    """
    Extract the link definitions from the content of the markdown file and add them to the pageData dictionary

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
    else:
        pageData['linkDefs'] = {}
        return pageData

    pageData['linkDefs'] = generateAbsoluteLinks(pageData['filePath'], pageData['linkDefs']) 

    return pageData

def generateAbsolutePath(currentFilePath: str, link: str) -> str:
    """
    Generate an absolute path from the current file path and the link
    
    Parameters
    currentFilePath: str - the path to the current markdown file
    link: str - the relative link to the markdown file
    Returns
    str - the absolute path to the markdown file, relative to the docs folder
    """

    #-- remove the file name from the current file path to get the folder
    location = f"/{currentFilePath}".rfind("/")
    currentFolder = currentFilePath[:location]

    #-- join the current folder with the link to get the absolute path
    absPath = str(pathlib.Path(currentFolder, link).resolve()).replace(MEMEX_FOLDER,"")

#    print(f"generateAbsolutePath - currentFilePath: {currentFilePath} and link: {link}")
#    print(f"   currentFolder {currentFolder}")
#    print(f"   absPath: {absPath}")

    #-- convert the absolute path to a string and remove the docs folder prefix
    absPath = str(absPath).replace(DOCS_FOLDER, "")

    #-- if it starts with /, remove it
    if absPath.startswith("/"):
        absPath = absPath[1:]

    return absPath
    
def addOtherLinks(markdownFiles: Files):
    """
    After the bubbles have all been loaded, revisit all the bubbles again, adding 'other' links to the linkdefs data structure, including 
    - relative markdown links 
        [text](./link.md) or [text](./link.md#anchor)
    - absolute local links 
        [text(/memex/link.md) or [text](/memex/link.md#anchor)

    Parameters
    markdownFiles: Files - a (MkDocs) Files object containing all the markdown files in the docs folder
    """

    for file in markdownFiles:
        content = file.content_string
        start = content.find("[//begin]")
        content = content[:start]

        # local links are defined as [text](./link.md) or [text](./link.md#anchor)
        localLinkRegex = r"\[([^\]]+)\]\((\.[^\)]+.md)\)"
        localLinks = re.findall(localLinkRegex, content)

        if len(localLinks)>0:
            for ( text, link ) in localLinks:
                # need to convert link to an absolute link
                absLink = generateAbsolutePath( file.src_path, link )

                description = text
                if 'title' in bubbles[absLink]['yaml']:
                    description = bubbles[absLink]['yaml']['title']
                
                bubbles[file.src_path]['linkDefs'][absLink] = {
                    'text': text,
                    'description': description
                }

        # absolute links are defined as [text](/memex/link.md) or [text](/memex/link.md#anchor)
        absLinkRegex = r"\[([^\]]+)\]\((/memex/[^\)]+.md)\)"
        absLinks = re.findall(absLinkRegex, content)
        if len(absLinks)>0:
            print(f"file {file.src_path} has {len(absLinks)} absolute links")
            for ( text, link ) in absLinks:
                # absLink is link minus the /memex/ prefix
                absLink = link.replace("/memex/", "")
                if 'title' in bubbles[absLink]['yaml']:
                    description = bubbles[absLink]['yaml']['title']

                if 'linkDefs' not in bubbles[file.src_path]:
                    bubbles[file.src_path]['linkDefs'] = {}

                bubbles[file.src_path]['linkDefs'][absLink] = {
                    'text': text,
                    'description': description
                }


    # DO NOT Remove the link definitions from the content
    # Need to convert the links to absolute link, where / is the docs folder

def extractFileContent( file : File ) -> dict:
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

    Parameter

    """

    pageData = {}
    #-- file is a pathlib.Path object, so convert it to a string and make
    #   relative to the docs folder
    #   e.g. /Users/davidjones/memex/docs/pkm.md becomes /pkm.md
#    docsFile = str(file).replace(FULL_DOCS_FOLDER, "")
#    print(f"Extracting content from {file} -> {docsFile}")
#    input("Press Enter to continue...")

    #with open(file, encoding="utf-8-sig") as f:
#    with mkdocs_gen_files.open(docsFile, 'r', encoding="utf-8-sig") as f:
#        bubble = frontmatter.load(f)

    #-- get the content of the file
    content = file.content_string

#    print(f"Content of {file.src_path}:\n{content}...\n")
#    input("Press Enter to continue...")
    bubble = frontmatter.loads(content)

    pageData['content'] = bubble.content
    pageData['yaml'] = bubble.metadata
    #pageData['filePath'] = str(file)
    pageData['filePath'] = file.src_path

    pageData = extractLinkDefs(pageData)

    return pageData

def retrieveMemexBubbles(markdownFiles: Files):
    """
    Retrieve all memex bubbles from the memex folder and return them as a list of dicts

    Parameters
    markdownFiles: Files - a (MkDocs) Files object containing all the markdown files in the docs folder
    Returns
    bubbles: dict of dicts
        <bubbleFilePath>: {
            'content': <content of bubble>,
            'yaml': <yaml metadata of bubble>,
            'filePath': <absolute path to bubble file>,
            'linkDefs': { <link>: { 'text': <text>, 'link': <link> } }
        }
    """
    global bubbles

    #-- get all files in the memex folder
#    files = glob.glob(f"{DOCS_FOLDER}/memex/*.md")
#    folder = pathlib.Path(DOCS_FOLDER)
#    files = folder.rglob("*.md")

#    for file in files:
    for file in markdownFiles:
#        print(f"Processing file {file.src_path} generated by {file.generated_by}")
        try:
            content = extractFileContent(file)
        except Exception as e:
            print(f"Error extracting content from {file.src_path}: {e}")
            quit()

#        content = extractFileContent(file)
        if content is not None:
            #localAbsPath = str(file).replace(DOCS_FOLDER, PREFIX)
#            localAbsPath = str(file).replace(DOCS_FOLDER, "")
#            print(f"file {file} becomes {localAbsPath}")
#            input("Press Enter to continue...")
            localAbsPath = file.src_path
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
    Generate a data structure that contains details of the backlinks to each bubble. i.e.
    another bubble (source bubble) includes a link to the destination bubble.

    Can be defined three different ways

    - linkDefs - added by a specific VSCode/Foam extension. Text at the bottom of the bubble that defines all the bubbles the current bubble links to.
    - local .md links - links in the current bubble of this form [wood-duck-gallery](./wood-duck-gallery.md) which are not added to linkDefs

    Broken implementation - hard coded backlinks

    Some generators are hard-coding backlinks into the header. But these aren't being added here. Should they? In theory, they should instead be hard coded as linkDefs, keeping a consistent method?

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

    #-- initialist the backlinks data structure
    backLinks = {}
    for file in bubbles.keys():
        backLinks[file] = {}

    for file in bubbles.keys():

        # loop thru each file, except those that are excluded
        bubble = bubbles[file]
        if any(re.search(pattern, bubble['filePath']) for pattern in EXCLUDE):
            continue

#            print(f"Processing bubble {file}")
#            pprint(bubble)
#            input("Press Enter to continue...")

        # add the current bubble's linkDefs to the backLinks data structure
        for destinationPath in bubble['linkDefs']:
            sourcePath = f'{bubble["filePath"].replace(DOCS_FOLDER, "")}'
            #sourcePath = f'{PREFIX}{bubble["filePath"].replace(DOCS_FOLDER, "")}'

#            print("----- ")
#            pprint(bubble['filePath'])
#            print(f"Source Path: {sourcePath}")
#            input("Press Enter to continue...")
            #-- 
            if destinationPath not in backLinks:
                print(f"Warning: destinationPath {destinationPath} not found in backLinks")
                print(f"from file {file}")
                input("Press Enter to continue...")
                backLinks[destinationPath] = {}
            backLinks[destinationPath][sourcePath] = bubble
            if file.endswith("sense/birdwatching/spottedDove.md"):
                print(f" -- backlink {destinationPath} = {sourcePath}")

            if destinationPath.endswith("sense/birdwatching/spottedDove.md"):
                print(f" -- backlink {destinationPath} = {sourcePath}")
                #pprint(bubble['linkDefs'])
                #input("Press Enter to continue...")

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

#    if filePath=="sense/birdwatching/spottedDove.md":
#        print(f"saving bubble to {filePath}")
#        print(yaml.dump(bubble['yaml']))
#        print("----")
#        print(bubble['content'])
#        input("Press Enter to continue...")

    #with open(bubble['filePath'], 'w', encoding="utf-8-sig") as f:
    with mkdocs_gen_files.open(filePath, 'w', encoding="utf-8-sig") as f:
        f.write("---\n")
        f.write(yaml.dump(bubble['yaml']))
        f.write("---\n")
        f.write(bubble['content'])

    mkdocs_gen_files.set_edit_path(filePath, "corpusActions.py")

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
            #fileLink = re.sub( rf"^{PREFIX}", "", sourceLink)
            fileLink = sourceLink

            title = "Unknown title"
            if 'title' in bubbles[fileLink]['yaml']:
                title = bubbles[fileLink]['yaml']['title']
            else:
                title = extractTitleFromContent(bubbles[fileLink]['content'])

            backlinks.append({
                'url': f"{PREFIX}/{sourceLink}".replace(".md", ".html"),
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
#        print(f"Found {len(imgLinks)} image links in {filePath}")
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
        #"edges": []
        "links": []
    }

#       "nodes": [
#        { "id": "id1", "name": "name1", "val": 1 }, 
#        { "id": "id2", "name": "name2", "val": 10 },
#    ],
#    "links": [
#        { "source": "id1", "target": "id2" },

    #-- add the nodes for the bubbles
    x = 1
    y = 1
    for filePath in bubbles.keys():
        if any(re.search(pattern, filePath) for pattern in EXCLUDE):
            continue

#        print(f"Processing {filePath}")
#        input("Press Enter to continue...")

        name = bubbles[filePath]['yaml'].get('title', 'No title found')
        # nodeId is filePath minus the PREFIX
        #-- remove the PREFIX from the filePath to get the nodeId
        #nodeId = filePath.replace(PREFIX, "")
        nodeId = f"{PREFIX}/{filePath}".replace(".md", ".html")

#        print(f"Processing {filePath}")
#        pprint(bubbles[filePath])
#        input("Press Enter to continue...")
        #-- add the node for the destination bubble
        # 'id':
        # 'name': <name of the bubble>
        # 'value': <path>
        graphData['nodes'].append({
            'id': nodeId,
            'name': name,
#            'x': x, 'y': y,
#            'value': filePath,
            'data': { 'name': name },
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
    # destinationFilePath is a file path relative to memex docs folder
    for destinationFilePath in backLinks.keys():
#        print("-------------------------")
#        print(f"Processing backlinks for {destinationFilePath}")
#        pprint(backLinks[destinationFilePath].keys())
#        input("1) Press Enter to continue...")
        # continue if there are no linkDefs for this destination
        for sourceLink in backLinks[destinationFilePath].keys():
#            print(f"    - {sourceLink} -> {destinationFilePath}" )

            #-- source and target need to be Web paths, adding PREFIX and replacing .md with .html
            #source = sourceLink.replace(PREFIX, "")
            source = f"{PREFIX}/{sourceLink}".replace(".md", ".html")
            #target = destinationFilePath.replace(PREFIX, "")
            target = f"{PREFIX}/{destinationFilePath}".replace(".md", ".html")
            #graphData['edges'].append({
            graphData['links'].append({
                'id': f"{edgeId}",
                'source': source,
                'target': target
            })
            edgeId += 1
#            print(f"    - {source} -> {target}")
#            input("Press Enter to continue...")

    #-- check the edges all have source and target
    #for edge in graphData['edges']:
    for edge in graphData['links']:
        if 'source' not in edge or 'target' not in edge:
            pprint(edge)
            raise ValueError(f"Edge {edge} does not have source or target")

    #-- check that each edge source has a corresponding node
    #for edge in graphData['edges']:
    for edge in graphData['links']:
        if edge['source'] not in [node['id'] for node in graphData['nodes']]:
            pprint(graphData['nodes'])
            raise ValueError(f"Edge {edge} has source {edge['source']} that does not exist in nodes")

    #-- save the graph data to a JSON file
#    with open(f"{DOCS_FOLDER}/colophon/graph.json", 'w', encoding="utf-8-sig") as f:
    with mkdocs_gen_files.open(f"colophon/graph.json", 'w', encoding="utf-8-sig") as f:
        json.dump(graphData, f, indent=4, ensure_ascii=False)
        #yaml.dump(graphData, f, allow_unicode=True)

        
def findFiles(markdownFiles: Files):
    findFiles= [
#    "sense/landscape-garden/wood-duck-gallery.md",
#        "sense/birdwatching/life-list.md",
#        "sense/birdwatching/spottedDove.md",
#        "sense/birdwatching/australasianFigbird.md",
#        "sense/birdwatching/greatEgret.md",
#        "sense/birdwatching/greatEgret.md",
    ]
#-- search markdownFiles for findFile in src_path 
    for findFile in findFiles:
        for file in markdownFiles:
            if file.src_path.endswith(findFile):
                print("-------------------------")
                print(f"Found {findFile} at {file.src_path}")
                print(f"generated by {file.generated_by}")
                print(file.content_string)
                input("Press Enter to continue...")
                continue

    input("Press Enter to continue...")

def saveBubbleToFile(bubble: dict):
    """
    Save a bubble to the file system

    Parameters
    bubble: dict - a dictionary containing the bubble content, yaml metadata, and file path
        {
            'content': <content of bubble>,
            'yaml': <yaml metadata of bubble>,
            'filePath': <absolute path to bubble file>
            'linkDefs': { <link>: { 'text': <text>, 'link': <link> } }
        }
    """

    #-- save the bubble to the file system

    with open(f"docs/{bubble['filePath']}", 'w', encoding="utf-8-sig") as f:
        f.write("---\n")
        f.write(yaml.dump(bubble['yaml']))
        f.write("---\n")
        f.write(bubble['content'])

#    print(f"Saved bubble to {bubble['filePath']}")
#    pprint(bubble['yaml'])
#    input("Press Enter to continue...")


def removeBackLinks():
    """
    Find any markdown files that have backlinks in the front matter (of the bubble) and remove the backlinks from the front matter in the actual files

    Backlink format

backlinks:
- title: Bush regeneration (Wood duck meadows)
  url: /sense/landscape-garden/regeneration.html
- title: The Island
  url: /sense/landscape-garden/the-island.html
- title: Mango paddock
  url: /sense/landscape-garden/mango-paddock.html
- title: Plants
  url: /sense/landscape-garden/plants/plants.html
    """

    #-- loop through each bubble and see if it has backlinks in the front matter
    for filePath in bubbles.keys():
        #-- if the filePath is not in the bubbles, skip it
        if filePath not in bubbles:
            continue

        #-- if the bubble has backlinks, remove them from the front matter
        if 'backlinks' in bubbles[filePath]['yaml']:
#            print(f"Removing backlinks from {filePath}")
#            pprint(bubbles[filePath]['yaml']['backlinks'])
            del bubbles[filePath]['yaml']['backlinks']
#            print("Backlinks removed")
#            pprint(bubbles[filePath]['yaml'])
            #-- save the bubble without backlinks
            saveBubbleToFile(bubbles[filePath])

"""
Main entry point for the generator
"""


config = configure()

# files is an object that access all the mkdoc files
# via the .items() method
# File object - https://www.mkdocs.org/dev-guide/api/#mkdocs.structure.files.File
filesEditor = mkdocs_gen_files.editor.FilesEditor.current()
#-- use mkdocs to get all the markdown files for mkdocs
markdownFiles = filesEditor.files.documentation_pages()
#findFiles(markdownFiles)
#-- use mkdocs data structures to get all Memex bubbles
retrieveMemexBubbles(markdownFiles)

#-- one-off utility function - to remove backlinks from front matter of actual files
#  not the mkdocs in memory copies
#removeBackLinks()
#quit()

addOtherLinks(markdownFiles)

#pprint(bubbles.keys())

#print(f"Retrieved {len(bubbles)} bubbles from the memex folder")
#input('(retrieveMemexBubbles) Press Enter to continue...')
#print(bubbles.keys( ))
#print("--------- spottedDove")
#pprint(bubbles["sense/birdwatching/spottedDove.md"], indent=4)
#print("---- pkm")
#pprint(bubbles["pkm.md"], indent=4)
#input("(retrieveMemexBubbles) Press Enter to continue...")

### Generate backlinks for the bubbles
# backlinks[<destinationFilePath>] = {
#    <sourceFilePath>: { <details of the bubble for this path> }
#    <sourceFilePath2>: { <details of the bubble for this path> }
# }
# Defines the backlinks for <destinationFilePath> with two links from two source files
backLinks = generateBackLinks(bubbles)

#print("------ showBacklinks")
#print("plant-life-list")
#print(backLinks["pkm.md"].keys())
#print("--------- plant life list")
#print(backLinks["sense/Observations/plant-life-list.md"].keys())
#print("--------- bird life list")
#print(backLinks["sense/Observations/bird-life-list.md"].keys())
#print("--------- red ash observation")
#print(backLinks["sense/Observations/plant-observations/redAsh/332976273.md"].keys())
#input("Press Enter to continue...")
#print("--------- pkm")
#input("(Show backlinks) Press Enter to continue...")
#pprint(backLinks)
#input("Press Enter to update front matter backlinks...")

#print("--------- spotted dove")
#pprint(backLinks["sense/birdwatching/spottedDove.md"])
#print("--------- gallery life list")
#input("Press Enter to update front matter backlinks...")
#for filePath in backLinks.keys():
#    print(f"Backlinks for {filePath}: keys {backLinks[filePath].keys()}")
#input("Press Enter to update front matter backlinks...")

updateFrontMatterBackLinks(bubbles, backLinks)
#moveImages(bubbles)
generateGraphJson(backLinks, bubbles)
