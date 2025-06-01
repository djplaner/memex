"""
corpusActions.py 

Generator that (will eventually) perform numerous actions that rely on reading the entire corpus of notes. All done in one generator so that the grabbing the entire corpus is done once.

Actions include

- generateBackLinks

    Add backlinks to all notes 
    TODO: exactly how to do add and display the information

"""

import pathlib
import glob
import os
import frontmatter
from pprint import pprint
import mkdocs_gen_files
from mkdocs.config import Config, load_config

INDIVIDUAL_PLANTS_FOLDER="sense/landscape-garden/individual-plants"
DOCS_FOLDER = ""

def extractFileContent( file ):
    """
    Given path local to a markdown file, extract the file content and return as a dictionary of the form
      {
        "content": "content of file",
        "yaml": { _all yaml defined variables_ },
        "filePath": "/path/to/file.md"
        }

    """

    pageData = {}
    with open(file, encoding="utf-8-sig") as f:
        bubble = frontmatter.load(f)

    pageData['content'] = bubble.content
    pageData['yaml'] = bubble.metadata
    pageData['filePath'] = str(file)

    return pageData

def retrieveMemexBubbles():
    """
    Retrieve all memex bubbles from the memex folder and return them as a list of dicts
    """
    bubbles = []

    #-- get all files in the memex folder
    files = glob.glob(f"{DOCS_FOLDER}/memex/*.md")
    folder = pathlib.Path(DOCS_FOLDER)
    files = folder.rglob("*.md")

    for file in files:
        print(f"Processing file: {file}")
        content = extractFileContent(file)
        if content is not None:
            bubbles.append(content)
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

def extractBubbleLinks(content):
    """
    Given the Markdown content of a bubble, extract all links to other bubbles and return them as a list.

    parameters
    content: str
        The Markdown content of the bubble
    returns
    links: list of str
        A list of bubble links found in the content, each link is a string representing the file path to the bubble
    """

    wikiLinkRegex = r'\[\[([^\]]+)\]\]'

#    TODO Look at publishPost and wikiLinkDefs

def generateBackLinks(bubbles):
    """
    Generate a data structure that contains details of the backlinks to each bubble

    parameters
    bubbles: list of dicts
        List of bubbles, each bubble is a dict with keys 'content', 'yaml', and 'filePath'

    returns
    backlinks: dict of dicts
        {
            <bubbleFilePath>: {
                { <backlink??>: {
                    <filePathBackLinkSource> : <count of backlinks>,
                    <filePathBackLinkSource2> : <count of backlinks2>,
                }
            }
            ...
        }
    
    """

    backLinks = {}

    for bubble in bubbles:
        # extract all bubble links (links to other bubbles) from the bubble
        bubbleLinks = extractBubbleLinks(bubble['content'])

        # for each bubbleLink, add it to the backLinks dict
        for link in bubbleLinks:
            if link not in backLinks:
                backLinks[link] = {}
            if bubble['filePath'] not in backLinks[link]:
                backLinks[link][bubble['filePath']] = 0
            backLinks[link][bubble['filePath']] += 1

    return backLinks


config = configure()

print("------------ corpusActions")
bubbles = retrieveMemexBubbles()
backLinks = generateBackLinks(bubbles)