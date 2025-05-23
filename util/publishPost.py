"""
publishPost.py --post <filename>

Given the filename/path of a markdown file

1. Read the content of the file ✔
2. Update any wikilinks into proper URL links (https://djon.es/memex/) ✔
3. Check "publishedPath" in the yaml frontmatter iff already posted
3. If not published 
    - calculate the publish date-based folder format yyyy/mm/dd/slug
    - add the calculation to the yaml frontmatter
4. Add previous/next links to the markdown file's front matter
    - **NOTE** Assumes that the new post will be the latest, hence only adds previous
5. Write the new/updated content to a new file in the blog folder based on publish date
6. **NO** Copy any cover images???
    - Any cover images and other files need to be outside the repo from now on
7. Modify the original blog post md file to include path to published post to support
    updating

TODO

- There is an issue with wikilinks (link definitions) not being created in Markdown when the wikilink is quoted
- updating an existing blog results in next/prev wrong
    previous is pointing to the post being updated
    - add a new page results in next/prev being correct

"""

 

MEMEX_FOLDER="/Users/davidjones/memex/docs"
MEMEX_URL="https://djon.es/memex"
BLOG_FOLDER="/Users/davidjones/blog/docs"
BLOG_URL="https://djon.es/blog"

DEBUG = False

import glob
from datetime import datetime
from pprint import pprint
from pathlib import Path
from slugify import slugify
import argparse
import frontmatter
import yaml
import re
import pytz

def retrieveArgs():
    """Retrieve command line arguments"""

    parser = argparse.ArgumentParser(description='Publish a post to the blog')
    parser.add_argument('--post', type=str, required=True,
                        help='Path to the markdown file to publish')
    parser.add_argument('--debug', action='store_true',
                        help='Enable debug mode')

    args = parser.parse_args()

    #-- check if post file exists
    if not Path(args.post).exists():
        parser.error(f"File {args.post} does not exist")

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

def writePost(postData:dict, memexPath:str=None):
    """
    Overwrite the file $BLOG_FOLDER/<postData['yaml']['publishedPath']>/index.md with the content of postData - yaml and content
    """

    #-- get the path to the blog post
    if memexPath is None:
        postPath = f"{BLOG_FOLDER}/{postData['yaml']['publishedPath']}/index.md"
    else:
        postPath = memexPath

    if DEBUG:
#        pprint(postData)
        print(f"DEBUG - writePost: {postPath}")

    #-- create object post with attributes metadata and content 
    #-- write the content to the blog file
    with open(postPath, 'w', encoding="utf-8-sig") as f:
        f.write("---\n")
        f.write(yaml.dump(postData['yaml']))
        f.write("---\n")
        f.write(postData['content'])

def readBlogMarkdown(markdownFile, transformLinks=True):
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

    pageData['old-content'] = post.content

    if transformLinks:
        # remove the link definitions from the content
        pageData = extractLinkDefs(pageData)
        pageData['linkDefs'] = generateAbsoluteLinks(markdownFile, pageData['linkDefs'])

    return pageData

def convertWikiLinks(postData : dict):
    """
    Convert Memex wiki links in postData['content'] to HTML links

    Loop through the keys of postData['linkDefs'] looking for [[<key>]] (wikilinks)
    and replace with normal markdown links [<key>](<linkDefs[key]['link']>)

    Also remove the "Authogenerated lilnk references" at the bottom
    
    param postData: a dictionary with 'content' and 'linkDefs' keys
    return: updated content str
    """

#    if DEBUG:
#        print("DEBUG: convertWikiLinks")
#        pprint(postData['linkDefs'])
#        input("Press Enter to continue...")
    #-- for each of the link definitions, convert the relative link to an absolute link
    if 'linkDefs' in postData:
        for linkDesc in postData['linkDefs']:
            #-- replace the wiki link with a markdown link
            if DEBUG:
                print(f"DEBUG: linkDesc: {linkDesc}")
            newLinkDesc = linkDesc
            #-- if link desc == link|label then replace with label
            if "|" in linkDesc:
                newLinkDesc = linkDesc.split("|")[1]
             
            postData['content'] = postData['content'].replace(f"[[{linkDesc}]]", f"[{newLinkDesc}]({postData['linkDefs'][linkDesc]['link']})")

    #-- remove '# "Autogenerated link references" at the end of the content
    postData['content'] = postData['content'].replace('# "Autogenerated link references"', "")

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

def getOrderedPosts():
    """
    Return an ordered list of all the posts in the blog folder

    - posts are Markdown files in the format YYYY/MM/DD/slug/index.md
    """

    postsPath = f"{BLOG_FOLDER}/2*/*/*/*/index.md"
    postMarkdownFiles = glob.glob(postsPath)

#    if DEBUG:
#        print(f"DEBUG: postMarkdownFiles: {postMarkdownFiles}")
#        print(f"DEBUG: len(postMarkdownFiles): {len(postMarkdownFiles)}")
#        print(f"DEBUG: postsPath: {postsPath}")

#        input("Press Enter to continue...")

    posts = []
    for postPath in postMarkdownFiles: 
        postData = readBlogMarkdown(postPath, False)
        if postData is None:
            raise Exception(f"Error reading {postPath}")
        if 'type' in postData['yaml'] and postData['yaml']['type'] != "post":
            #-- skip non-posts
            continue
        title = postData['yaml']['title']
        postDate = ""
        if 'date' in postData['yaml']:
            postDate = postData['yaml']['date']
            #-- convert postDate datetime.datetime to string
            postDate = postData['yaml']['date'].strftime("%Y-%m-%dT%H:%M:%S.%f%z")

        link = postPath

        posts.append( {
            "path": postPath,
            "content": postData,
            "date": postDate,
            "title": title,
            "link": link,
        })

    orderedPosts = sorted(posts, key=lambda x: x['date'], reverse=True)

    return orderedPosts

def getSetOldestPost(postData:dict):
    """
    Given the postData dictionary for the new post retrieve the previous 
    oldest post, update its next link to point to the new post and return
    the new post.

    params postData: a dictionary with 'yaml' and 'content' keys
    return: oldPostData: a dictionary with 'yaml' and 'content' keys for the previous oldest post
    """

    #-- get an ordered list of all the posts in the blog folder
    orderedPosts = getOrderedPosts()
    oldestPost = orderedPosts[0]['content']
    publishedPath = orderedPosts[0]['path'].replace(BLOG_FOLDER, "/").replace("/index.md", "")
    if DEBUG:
        #-- show the last post added
        print(f"DEBUG: publishedPath: {publishedPath}")
        input("Press Enter to continue...")
        #pprint(oldestPost)

    oldestPost['yaml']["next"] = {
        "text": postData['yaml']['title'],
        # remove the full path and add the /blog prefix
        "url": f'/blog{postData["yaml"]["publishedPath"].replace(BLOG_FOLDER, "")}'
    }
    oldestPost['yaml']["publishedPath"] = publishedPath

    #-- save the updated post
    writePost(oldestPost)

    return oldestPost

def updateNewPost(postData:dict, oldestPost:dict):
    """
    Update the next/previous yaml links for the new post (postData) to include
         next { text: "Home", url: "/blog/index.html" }
         previous { text: <oldestPost title>, url: <oldestPost publishedPath> }
    and other required headers
        template: blog-post.html
        date: <current date time>

    params:
        postData: a dictionary with 'yaml' and 'content' keys for new post
        oldestPost: a dictionary with 'yaml' and 'content' keys for the previous oldest post
    return: postData: a dictionary with 'yaml' and 'content' keys for the new post
    """

    postData['yaml']['next'] = {
        "text": "Home",
        "url": "/blog/index.html"
    }
    postData['yaml']['previous'] = {
        "text": oldestPost['yaml']['title'],
        "url": f'/blog{oldestPost["yaml"]["publishedPath"].replace(BLOG_FOLDER, "")}'.replace("//", "/")
    }

    postData['yaml']['template'] = "blog-post.html"
    postData['yaml']['date'] = pytz.utc.localize(datetime.now()) 
           #.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    return postData



def publishPost(memexFileName:str):
    """Given the filename of a markdown file modify the markdown and copy it into the 
    blog folder

    If the blog post is already published, then just copy it to the blog folder
    """

    if DEBUG:
        print(f"DEBUG: publishPost {memexFileName}")

    #-- get contents of markdown file as dict with keys
    #   yaml, content, linkDefs
    postData = readBlogMarkdown(memexFileName)
    # save the original content for latter use
    postData['content'] = convertWikiLinks(postData)

    if DEBUG:
        print("DEBUG: postData")
        pprint(postData)
        input("Press Enter to continue...")

    #-- has it already been published
    #     postData['yaml']['publishedPath'] = <path to published post>
    #  (relative to the blog folder)
    postFolderPath = ""
    if "publishedPath" in postData['yaml']:
        #-- if the post is already published, then just copy it to the blog folder
        # - no extra work required, already in the YAML
        postFolderPath = f"{BLOG_FOLDER}/{postData['yaml']['publishedPath']}/"
        #-- 
    else:
        #-- if the post is not published, then
        #   - calculate the publish date-based folder format yyyy/mm/dd/slug
        #   - get the previous post and update it's next/previous
        #   - add the next/prev to the current post
        postFolderPath = generatePostFolderPath(postData['yaml']['title'])
        postData['yaml']['publishedPath'] = postFolderPath.replace(BLOG_FOLDER, "")
        #-- retrieve and update the oldest post and update its next link
        oldestPost = getSetOldestPost(postData)
        #-- update the YAML for the new post with prev/next, date etc.
        postData = updateNewPost(postData, oldestPost)

    #-- create the folder, if necessary
    if not Path(postFolderPath).exists():
        Path(postFolderPath).mkdir(parents=True, exist_ok=True)

    #-- write the content to the blog file
    writePost(postData)
    #-- update the original blog post md file to include path to published post to support updating
    postData['content'] = postData['old-content']
    writePost(postData, memexFileName)

if __name__ == "__main__":
    #-- get command line args
    args = retrieveArgs()
    if args.debug:
        DEBUG = True
    publishPost(args.post)

    
    