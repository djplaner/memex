"""
publishPost.py --post <filename>

Given the filename/path of a markdown file

1. Read the content of the file ✔
2. Update any wikilinks into proper URL links (https://djon.es/memex/) ✔
3. Calculate the publish date-based folder format yyyy/mm/dd/slug
4. Add previous/next links to the markdown file's front matter
5. Write the updated content to a new file in the blog folder based on publish date
    - if it's already published update the content
6. Copy any cover images???
"""

 

MEMEX_FOLDER="/Users/davidjones/memex/docs"
MEMEX_URL="https://djon.es/memex"
BLOG_FOLDER="/Users/davidjones/blog/docs"
BLOG_URL="https://djon.es/blog2"

from datetime import datetime
from pprint import pprint
from pathlib import Path
from slugify import slugify
import argparse
import frontmatter
import re

def retrieveArgs():
    """Retrieve command line arguments"""

    parser = argparse.ArgumentParser(description='Publish a post to the blog')
    parser.add_argument('--post', type=str, required=True,
                        help='Path to the markdown file to publish')

    args = parser.parse_args()
    return args

def extractLinkDefs(pageData):
    """
    Extract the link definitions from the content of the markdown file
    and add them to the pageData dictionary

    Link definitions are defined at the bottom of the cotent located between
    [//begin] and [//end] tags. Format is:
    [link text]: <relative link> "description"

    param pageData: a dictionary with 'content' and 'yaml' keys
    return: a dictionary with 'content', 'yaml', and 'linkDefs' keys
    - 'linkDefs' is a dictionary of dictionaries keyed on 'text' 
             { 'text': <text>, 'link': <link>, 'description': <description> }
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
                link = match.group(2)
                description = match.group(3)
                #-- add the link definition to the dictionary
                pageData['linkDefs'][text] = {
                    'link': link,
                    'description': description
                }

        # Remove the link definitions from the content
        pageData['content'] = pageData['content'][:start] + pageData['content'][end+len("[[//end]]"):]
    else:
        pageData['linkDefs'] = None

    return pageData

def generateAbsoluteLinks(markdownFile, linkDefs):
    """
    transform the relative links in linkDefs[<text>]['link'] into absolute links using
    the path to the markdown file as a reference point

    e.g. where 
        markdownFile = docs/share/blog/2025/a-new-day.md
        linkDefs = {
            'colophon': {
                'link': '../../../colophon/colophon',
                'description': 'About (colophon)'
            }
        }
        the new linkDefs['link'] = 'https://djon.es/colophon/colophon.md'

    param markdownFile: the path to the markdown file
    param linkDefs: a dictionary of link definitions
    return: a dictionary of link definitions with absolute links
    """

    #-- Grab the (current)folder containing the markdownFile
    location = markdownFile.rfind("/")
    currentFolder = markdownFile[:location]

    #-- for each of the link definitions, convert the relative link to an absolute link
    for linkDesc in linkDefs:
        # add .md to the link to refer to an actual file
        targetLink = linkDefs[linkDesc]['link'] + ".md"
        # targetLink is relative, append it to current folder to provide a relative path to resolve
        path = f"{currentFolder}/{targetLink}"
        # resolve the path to an absolute path
        p = Path(path)
        absPath = p.resolve()
        # convert the absolute path to a URL
        url = str(absPath).replace(MEMEX_FOLDER, MEMEX_URL)
        # replace the markdown link to html
        url = url.replace(".md", ".html")
        linkDefs[linkDesc]['link'] = url

    return linkDefs


def readBlogMarkdown(markdownFile):
    """
    Extract the content of a markdown file into 
    - 'yaml' - yaml frontmatter 
    - 'content' - the markdown content
    - 'linkDefs' - parsed link reference descriptions at the end of the file between [[//begin]] and [[//end]]

    param markdownFile: the path to the markdown file
    return: a dictionary with 'yaml' and 'content' keys
    """

    pageData = {}

    # Use frontmatter to extract the 'content' and 'yaml'
    with open(markdownFile, encoding="utf-8-sig") as f:
        post = frontmatter.load(f)

    pageData['content'] = post.content
    pageData['yaml'] = post.metadata

    # remove the link definitions from the content
    pageData = extractLinkDefs(pageData)
    pageData['linkDefs'] = generateAbsoluteLinks(markdownFile, pageData['linkDefs'])

    return pageData

def convertWikiLinks(postData : dict):
    """
    Convert Memex wiki links in postData['content'] to HTML links

    Loop through the keys of postData['linkDefs'] looking for [[<key>]] (wikilinks)
    and replace with normal markdown links [<key>](<linkDefs[key]['link']>)
    
    param postData: a dictionary with 'content' and 'linkDefs' keys
    return: updated content str
    """

    #-- for each of the link definitions, convert the relative link to an absolute link
    for linkDesc in postData['linkDefs']:
        #-- replace the wiki link with a markdown link
        postData['content'] = postData['content'].replace(f"[[{linkDesc}]]", f"[{linkDesc}]({postData['linkDefs'][linkDesc]['link']})")

    return postData['content']

def generatePostFolderPath(title:str):
    """
    Generate the path to the folder to contain the blog post based on the title and current date
    using the format YYYY/MM/DD/slug

    param title: the title of the blog post
    return: a string with the path to the blog post's folder
    """

    #-- get the current date
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    #-- generate the slug from the title
    slug = slugify(title)

    #-- generate the path to the blog post
    postPath = f"{BLOG_FOLDER}/{year}/{month}/{day}/{slug}"

    return postPath

def publishPost(post:str):
    """Given the filename of a markdown file modify the markdown and copy it into the 
    blog folder

    If the blog post is already published, then just copy it to the blog folder
    """
    print(f"publishPost {args.post}")

    #-- get contents of markdown file as dict with keys
    #   yaml, content, linkDefs
    postData = readBlogMarkdown(post)
    postData['content'] = convertWikiLinks(postData)

    #-- calculate the YYYY/MM/DD/slug format based on 
    #   - slug is based on postData['yaml']['title']
    #   - current date/time used to calculate the YYYY/MM/DD
    postFolderPath = generatePostFolderPath(postData['yaml']['title'])
    #-- create the folder, if necessary
    if not Path(postFolderPath).exists():
        Path(postFolderPath).mkdir(parents=True, exist_ok=True)

    #-- calculate the next/previous links
    #   iff folder already exists use those
    #   update the yaml frontmatter

    # TODO what about handling any cover images, should these be copied or should
    # they be kept in memex?

    #-- write the content to the blog file





if __name__ == "__main__":
    #-- get command line args
    args = retrieveArgs()
    publishPost(args.post)

    
    