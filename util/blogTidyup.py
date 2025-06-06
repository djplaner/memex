"""
blogTidyup.py

Modify the ~/docs/blog folder structure (containing output of Wordpress to markdown) to better fit the old blog structure. May end up working from one folder (outside memex, created by Wordpress to markdown), filtering and writing any changes to new (memex) location

Work to be done

- Modify any old links to davidtjones.wordpress.com
- Fix up folder structure for blog posts
    YYYY/MM/<slug> to YYYY/MM/DD/<slug>
- Adding comments
    - Including the parent/child relationship
- Move pages from date based folder structure to one based on URLs (matching Wordpress blog)

"""

import os
import shutil
import glob
#import markdown
import yaml
import frontmatter
import re
import urllib.request
from datetime import datetime

from wpparser import parse
from pprint import pprint

# Location of XML files from Wordpress
WORDPRESS_EXPORT_FILE = "/Users/davidjones/Downloads/export.xml"
# Location of markdown files generated by Wordpress to markdown - contains pages and posts folders
INPUT_FOLDER = "/Users/davidjones/import-blog/output"
OUTPUT_FOLDER = "/Users/davidjones/blog/docs"

OLD_BLOG_URL = "https://davidtjones.wordpress.com"
OLD_BLOG_URL_MISSING = "davidtjones.wordpress.com"
CURRENT_BLOG_URL = "https://djon.es/blog"
MEMEX_BLOG_URL = "/blog"


BROKEN_LINKS = {}

# Replace any old blog content with something that now works
OUTDATED_CONTENT = [
    {
        "pattern": r"\\\[googlevideo=[^\]]*\\\]",
        "replace": "Google video no longer available"
    },
    {
        "pattern": r"\\\[slideshare [^\]]*\\\]",
        "replace": "Presentation from Slideshare no long available"
    },
    {
        "pattern": r"\\\[h5p [^\]]*\\\]",
        "replace": "H5P content no longer available"
    },
]
    
CONTENT_TIDYUP = [
    { "pattern": "<figure>", "replace": "<figure markdown>" },
    { "pattern": "<figcaption>", "replace": "<caption>" },
    { "pattern": "</figcaption>", "replace": "</caption>" }
]

# Update any old blog links to current strucutre (mostly for pages)
# - links are in Memex format, as blog links will have been converted 
OLD_LINKS = [
    {
        #"pattern": r"https://djon.es/blog/research/current-research-projects/",
        "pattern": rf"\({MEMEX_BLOG_URL}/research/current-research-projects/\)",
        "replace": rf"({MEMEX_BLOG_URL}/current-research-projects/)"
    },
    {
        "pattern": rf"\({MEMEX_BLOG_URL}/research/the-moodle-open-book-module-project/\)",  
        "replace": rf"({MEMEX_BLOG_URL}/the-moodle-open-book-module-project/)"
    },
    {
        "pattern": rf"\({MEMEX_BLOG_URL}/elearning-and-innovation/\)",
        "replace": rf"({MEMEX_BLOG_URL}/2009/08/20/elearning-and-innovation-specialist-report-1-4-20-august)/"
    },
    {
        "pattern" :rf"\({MEMEX_BLOG_URL}/\)",
        "replace": rf"({MEMEX_BLOG_URL}/blog-home.md)"
    },
    {
        "pattern": rf"\({MEMEX_BLOG_URL}/category/bim/bim2\)",
        "replace": rf"({MEMEX_BLOG_URL}/category/bim2)"
    }
#    { . djon.es/blog links should already be converted
#        "pattern": r"\(https://djon.es/blog/([^/]+)/\)",
#        "replace": r"(/memex/blog/\1/index.md)"
#    }
]


def readBlogMarkdown(markdownFile):
    pageData = {}
    with open(markdownFile, encoding="utf-8-sig") as f:
        post = frontmatter.load(f)

    pageData['content'] = post.content
    pageData['yaml'] = post.metadata

    return pageData
#    print("------------ post")
#    print(post)
#    print("--- metadata")
#    for key in post.keys():
#        print(f"{key}: {post[key]}")
#    quit()


def isBrokenLink(link):
    """
    Check any valid full URL (http/https) to see if it's broken
    """
    # -- ensure it's a full URL - starting with http
    if not link.startswith("http"):
        return False

    req = urllib.request.Request(link)

    try:
        resp = urllib.request.urlopen(req)
        if resp.status in [400, 404, 403, 408, 409, 501, 502, 503]:
            print(f"Broken link: {link} - {resp.status}")
            return True
    except urllib.error.HTTPError as e:
        print(f"Broken link: {link} - {e.code}")
        return True

    return False


def replaceOldBlogLink(link): 
    """
    If link contains an old davidtjones.wordpress.com link replace it in the content
    - Standard old link
    - Link without http[s]://
    """
    if OLD_BLOG_URL in link:
        #-- replace davidtjones.wordpress links with current blog URL
        link = link.replace(OLD_BLOG_URL, CURRENT_BLOG_URL)
        #print(f"Replacing Link: {link} -> {newLink}")
    elif re.match(rf"^{OLD_BLOG_URL_MISSING}", link):
        # -- check for old blog links without http[s]
        link = link.replace(OLD_BLOG_URL_MISSING, CURRENT_BLOG_URL)
    return link

def replaceBlogLink(link):
    """
    If link contains a current djon.es/blog link replace it with a memex link
    - djon.es/blog becomes djon.es/blog/memex (works for pages)
    - TODO Posts may need more work

    Pages will have YYYY/MM/DD format. Posts won't
    May not need to distinguish. Just change the URL leads
    """

    #postRegex = rf"^{CURRENT_BLOG_URL}/[0-9]{{4}}/[0-9]{{2}}/[0-9]{{2}}/"
    if CURRENT_BLOG_URL in link:
        #-- replace current blog links with memex blog URL
        newLink = link.replace(CURRENT_BLOG_URL, MEMEX_BLOG_URL)
        print(f"*** Replacing Link: {link} -> {newLink}")
        return newLink

    return link

def transformAbsoluteMemexLinks(content, memexPath):
    """
    Look for absolute memex links (/memex/...) in markdown content. Replace with links relative to the current page memexPath. Add an index.md on the end

    Some gotchas
    - links within internal anchors #, add the index.md before the #
    - category links /memex/blog/category/ - don't add index.md
    
    Parameters
    - content: str  The markdown content to be cleaned up
    - memexPath: str  The memex absoluted path for the index.md file into which content will be placed.

    Returns
    - content: str  The cleaned up markdown content
    """

    #-- extract all absolute memex links from content (markdown)
    # -   (/memex/...)

    memexLink = r"\(/memex/[^)]+\)"
    matches = re.findall(memexLink, content)
    # convert matches to dict
    links = {match: match for match in matches}

    for link in links.keys():
        #-- remove the () that specify a markdown link
        newLink = link.replace( "(", "").replace(")", "")
        #-- does the link contain a # (internal anchor)
        if '#' in newLink:
            #-- remove the anchor from the link
            newLink = newLink.split("#")[0]
            anchor = link.split("#")[1]
            #-- add index.md to the end of the link
            memexRelPath = os.path.relpath(newLink, start=memexPath)
            print(f"##    -- ANCHOR {memexPath}\n#### Replacing Link: \n## {newLink}\n## {memexRelPath}/index.md#{anchor}")
            content = content.replace(f"({newLink}#{anchor})", f"({memexRelPath}/index.md#{anchor})")
        else:
            memexRelPath = os.path.relpath(newLink, start=memexPath)
            #-- if the link is a category link, don't add index.md, just add .md
            if "/category/" in newLink:
                #-- don't add index.md to the end of the link
                memexRelPath = os.path.relpath(newLink, start=memexPath)
                print(f"##    -- CATEGORY {memexPath}\n#### Replacing Link: \n## {newLink}\n## {memexRelPath}.md")
                content = content.replace(f"({newLink})", f"({memexRelPath}.md)")
            elif newLink.endswith(".md"):
                memexRelPath = os.path.relpath(newLink, start=memexPath)
                print(f"##    -- CATEGORY {memexPath}\n#### Replacing Link: \n## {newLink}\n## {memexRelPath}.md")
                content = content.replace(f"({newLink})", f"({memexRelPath})")
            else:
                #-- add index.md to the end of the link
                print(f"##    -- {memexPath}\n#### Replacing Link: \n## {newLink}\n## {memexRelPath}/index.md")
                content = content.replace(f"({newLink})", f"({memexRelPath}/index.md)")
        
    return content

def cleanupContent(content, memexPath):
    """
    Given markdown from a blog post/page, perform the following cleanup

    - Convert davidtjones.wordpress links to djon.es/blog
    - Convert djon.es/blog links to absolute memex links
    - Convert absolute memex links to links relative to memexPath

    Parameters
    - content: str  The markdown content to be cleaned up
    - memexPath: str  The memex absoluted path for the index.md file into which content will be placed.

    Returns
    - content: str  The cleaned up markdown content
    """

    #-- create dict containing all links extracted from content
    # - key will be original link found in content
    # - value will be what to replace it with
    links = {}
    #-- extract all links from content (markdown)
    matchRe = r'\[.*?\]\((.*?)\)'
    matches = re.findall(matchRe, content)
    # convert matches to dict
    links = {match: match for match in matches}

    for link in links.keys():

        #-- check if link is an old blog link
        # - Must be first so current blog url can be changed later
        newLink = replaceOldBlogLink(link)
        #-- convert djon.es/blog full links to memex absolute links
        newLink = replaceBlogLink(newLink)
        content = content.replace(link, newLink)

        #-- replace any page internal links        
        regex = r"^#"
#        if '#' in link:
        if re.match(regex, link):
#            print(f"-------- before")
#            print(content)
            #content = re.sub(rf"\[([^\]]?)\]\({link}\)", r"\1", content)
            content = re.sub(rf"\[([^\]]*)]\({link}\)", r"\1", content)
#            print(f"Link: {link} ->")
#            input("Press Enter to continue...")
#            print(f"-------- after")
#            print(content)
#            input("Press Enter to continue...")
#            print(f"Replaced Link: {link} ")
#            quit()

        # if link not in BROKEN_LINKS check if broken link
#        if link not in BROKEN_LINKS and isBrokenLink(link):
#            BROKEN_LINKS[link] = True

    #-- replace specific out-dated links
    for outDatedLink in OLD_LINKS:
#        print(f"XXXX Looking for outdated link: {outDatedLink['pattern']} replace with {outDatedLink['replace']}")
        if re.search(outDatedLink['pattern'], content):
#            print(f"SSSSS Found outdated link: {outDatedLink['pattern']} replace with {outDatedLink['replace']}")
            content = re.sub(outDatedLink["pattern"], outDatedLink["replace"], content)

    content = transformAbsoluteMemexLinks(content, memexPath)
    #-- replace any outdated content
    for outdated in OUTDATED_CONTENT:
        #print(f"SSSSSSSs {outdated['pattern']} -> {outdated['replace']}")
        ##-- create regex for outdated["pattern"]
        regex = rf"{outdated['pattern']}"
        ## does regex exist in content
        if re.search(regex, content):
            print(f"SSSSS Found outdated content: {outdated['pattern']}")
            content = re.sub(outdated["pattern"], f"""
!!! warning "Outdated content no longer available"

    {outdated["replace"]}\n""", content)

    #-- tidy up other content
    for contentTidy in CONTENT_TIDYUP:
        regex = rf"{contentTidy['pattern']}"
        ## does regex exist in content
        if re.search(regex, content):
#            print(f"SSSSS Found outdated content: {contentTidy['pattern']}")
            content = re.sub(contentTidy["pattern"], contentTidy["replace"], content)
        
    return content

def cleanupYaml(yamlData):
    """
    Yaml frontmatter has issues if the title contains a quote character of various forms, including
    - an actual quote
    - an escaped quote
    - an escaped single quote
    Replace all these. The actual quote gets replaced first.
    """

    replaceHash = { '"': '\\"', "&quot;" : '\\"', "&#039;" : "'" }
    if "title" in yamlData:
        if isinstance(yamlData["title"], str): 
            change = False
            oldTitle = yamlData["title"]
            for toReplace in replaceHash.keys():
                if toReplace in yamlData["title"]:
                    change = True
                    yamlData["title"] = yamlData["title"].replace(toReplace, replaceHash[toReplace])
            #-- remove any quotes surrounding title
            if change:
                yamlData["title"] = yamlData["title"].replace( r'^"', '').replace( r'"$', '')
#                print(f"old title {oldTitle}")
#                print(f"new title {yamlData['title']}")
#                input("Press enter")

    return yamlData
    

def getOrderedPosts(xml, postMarkdownFiles):
    """
    Take a list of full pathnames for all blog posts and return an ordered list of dicts
    {
        "postPath": <full path to post>,
        "postContent": {
            "yaml": <yaml frontmatter from file>,
            "content": <markdown content from file>
            "postXML": <raw XML data for the post>
            "postDate": <date of the post>
            "destinationPath": <path to copy the post to folder for the post>
            "sourcePath": <path to the source folder for the post>
        }
    }
    """

    posts = []
    for postPath in postMarkdownFiles: 
        postData = readBlogMarkdown(postPath)
        if postData is None:
            raise Exception(f"Error reading {postPath}")
        title = postData['yaml']['title']
        postDate = ""
        if 'date' in postData['yaml']:
            postDate = postData['yaml']['date']
            #-- convert postDate datetime.datetime to string
            postDate = postData['yaml']['date'].strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        postXmlData = findXmlPost( xml, title, postDate )
        if postXmlData is None:
            print(f"Error: No matching post found for {title} in XML...skipping")
#            input("Press Enter to continue...")
            continue
        destinationPath = f"{OUTPUT_FOLDER}{postXmlData['link'].replace(CURRENT_BLOG_URL, '')}"
        link = f"{MEMEX_BLOG_URL}{postXmlData['link'].replace(CURRENT_BLOG_URL, '')}"

        sourcePath = postPath.replace("index.md", "")

        posts.append( {
            "postPath": postPath,
            "postContent": postData,
            "postXML": postXmlData,
            "postDate": postDate,
            "postLink": link,
            "destinationPath": destinationPath,
            "sourcePath": sourcePath
        })

    #-- sort the posts by date given by post["postContent"]["yaml"]["date"]
    orderedPosts = sorted(posts, key=lambda x: x["postContent"]["yaml"]["date"], reverse=True)

#    for post in orderedPosts:
#        print(f"Post: {post['postPath']} Date: {post['postContent']['yaml']['date']}")

    return orderedPosts


def updatePosts(xml):
    """
    Perform all updates required for blog posts

    - Move from YYYY/MM/<slug> to YYYY/MM/DD/<slug> folder structure
    - Look for old links to wordpress.com and update
    - Look for broken links
    - Copy the images folder if it exists
    - Create the updated index.md file

    Also create the dummy pages.md file with an index of all pages added
    """

    # get list of full paths for all posts
    postMarkdownFiles = glob.glob(f"{INPUT_FOLDER}/posts/*/*/*/index.md")

    orderedPosts = getOrderedPosts(xml, postMarkdownFiles)

    postsAdded = []

    # track numPosts to calculate prev/next
    count = 0
    numPosts = len(orderedPosts)

    #for post in postMarkdownFiles:
    for postData in orderedPosts:
        # default previous/next is loop back to home page
        previous = { 'text': 'Home', 'url': '/blog/index.html' }
        next = { 'text': 'Home', 'url': '/blog/index.html' }
        if count > 0:
            next = { 
                    'text': f'{orderedPosts[count-1]["postContent"]["yaml"]["title"]}',
                    'url': orderedPosts[count-1]["postLink"]
                       }
        if count < numPosts - 1:
#            pprint(orderedPosts[count+1])
            previous = { 
                    'text': f'{orderedPosts[count+1]["postContent"]["yaml"]["title"]}',
                    'url': orderedPosts[count+1]["postLink"]
                   }

        count += 1

        postData["postContent"]["yaml"]["previous"] = previous
        postData["postContent"]["yaml"]["next"] = next

        title = postData["postContent"]['yaml']['title']
        postDate = postData["postDate"]
        #-- identify the posts absolute memex path
        postMemexPath = postData["destinationPath"]

        #---------------------- perform various cleanups on the content
        #-- clean up the markdown content
        postData['postContent']['content'] = cleanupContent(postData['postContent']['content'], postMemexPath)
        postData['postContent']['yaml'] = cleanupYaml(postData['postContent']['yaml'])

        #--------------------- create and copy new folder/content
        # - destination will mirror the xmlData link YYYY/MM/DD/<slug>
        destinationPath = postData["destinationPath"]
        sourcePath = postData["sourcePath"]

        # update the destinationPath folder - create it iff ! exist and copy images
        updateMemexFolder(sourcePath, destinationPath)
        # add in the index.md file for the post
        writeMemexIndex(destinationPath, postData['postContent'], postData['postXML'])


        #------------ Track the posts that were added for use to write the page index
        # - pageXmlData['link'] without the CURRENT_BLOG_URL
        postAdd = postData['postXML']['link'].replace(CURRENT_BLOG_URL, '')
        postsAdded.append( postAdd )


    writePostsIndex(postsAdded)


def updatePages(xml):
    """
    Perform all updates required for Blog pages

    - Move from date to old blog file structure
    - Look for old links to wordpress.com and update
    - Look for other broken links??
    - Copy the images folder if it exists
    - Create the updated index.md file

    Also create the dummy pages.md file with an index of all pages added

    Process
    - Get all names of pages
    - for each page
        - Read the markdown file - frontmatter and markdown
        - Find a matching page in the XML
        - Create a folder using the page location from XML
        - if there's an images folder, copy it and contents across
        - Parse content
            - Find any links to old blog posts and update them
            - Find any broken links
    """

    # get full paths for the markdown files for all pages
    pageMarkdownFiles = glob.glob(f"{INPUT_FOLDER}/pages/*/*/*/index.md")

    pagesAdded = []

    for page in pageMarkdownFiles:
        #----------- get content for this page
        # - pageData - yaml and content (markdown) from exported markdown file
        # - pageXmlData - raw content from XML export file

        #- get the markdown content and frontmatter
        pageData = readBlogMarkdown(page)
        if pageData is None:
            raise Exception(f"Error reading {page}")

#        pageData['content'] = cleanupContent(pageData['content'])
        title = pageData['yaml']['title']
        postDate = ""
        if 'date' in pageData['yaml']:
            postDate = pageData['yaml']['date']
            # convert postDate from datetime:datetime to string
            postDate = pageData['yaml']['date'].strftime("%Y-%m-%dT%H:%M:%S.%f%z")
        #- find the post in the XML
        pageXmlData = findXmlPost( xml, title, postDate, "page" )
        #pprint(pageXmlData)
        if pageXmlData is None:
            print(f"Error: No matching page found for {title} in XML...skipping")
            continue


#        print("--" * 40)
#        print(f"Title: {pageXmlData['title']} type {pageXmlData['post_type']} status {pageXmlData['status']}")
#        print(f"post_date {pageXmlData['post_date']}")
#        print(f"post_link {pageXmlData['link']}")

        destinationPath = f"{OUTPUT_FOLDER}/{pageXmlData['link'].replace(CURRENT_BLOG_URL, '')}"
        pageMemexPath = f"{MEMEX_BLOG_URL}{pageXmlData['link'].replace(CURRENT_BLOG_URL, '')}"
        #print(f"sourcePath: {page}\ndestinationPath: {destinationPath}\npageMemexPath: {pageMemexPath} ")
        #relPath = os.path.relpath("/memex/blog/research/the-moodle-book-project/", start=pageMemexPath)
        #input(f"relPath: {relPath}")

        #---------------------- perform various cleanups on the content
        #-- clean up the markdown content
        pageData['content'] = cleanupContent(pageData['content'], pageMemexPath)
#        print(pageData['content'])
        sourcePath = page.replace("index.md", "")

        #updateMemexFolder(page, pageData, pageXmlData)
        updateMemexFolder(sourcePath, destinationPath)
        writeMemexIndex(destinationPath, pageData, pageXmlData)

        #-- update pagesAdded with sub-folders that the page was copied to local to docs
        # - pageXmlData['link'] without the CURRENT_BLOG_URL
        pageAdd = pageXmlData['link'].replace(CURRENT_BLOG_URL, '')
        #pageAdd = page.replace("index.md", "").split("/")[-2]
#        print(f")))))))) page: {page} >>> Page added: {pageAdd}")
        pagesAdded.append( pageAdd )

        #input("Press Enter to continue...")

    writePagesIndex(pagesAdded)

def writePostsIndex(posts):
    """
    Create a temp index.md file in the blog folder with a list of all posts added

    TODO A better format might be better, but this is simply testing, eventually a generator may do this work
    """

    #-- write the new index.md file
    with open(f"{OUTPUT_FOLDER}/posts.md", "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("title: Posts\n")
        f.write("type: posts\n")
        f.write("---\n")
        #-- add in some additional pre-amble
#        f.write(f"\nSee also: [[blog-home | Home]], [[pages]], [[posts]]\n\n")
        #-- write the content
        for post in posts:
            #-- get the last part of the path for the name
            name = post.split("/")[-2]
            #-- remove any leading / from page
            post = post.lstrip("/")
            f.write(f"- [{name}]({post}index.md)\n")

def writePagesIndex(pages):
    """
    Create a temp page.md file in the blog folder with a list of all pages added

    Simply an un-organised list of all pages added

    TODO - put into a better structure - may not be required?
    """

    #-- write the new index.md file
    with open(f"{OUTPUT_FOLDER}/pages.md", "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("title: Pages\n")
        f.write("type: pages\n")
        f.write("---\n")
        #-- add in some additional pre-amble
#        f.write(f"\nSee also: [[blog-home | Home]], [[pages]], [[posts]]\n\n")
        #-- write the content
        for page in pages:
            #-- get the last part of the path for the name
            name = page.split("/")[-2]
            #-- remove any leading / from page
            page = page.lstrip("/")
            f.write(f"- [{name}]({page}index.md)\n")

        
def updateMemexFolder(sourcePath : str, destinationPath : str):
    """
    Create a new folder for the page in memex
    Create an images folder within it iff not exists

    Parameters
    - sourcePath: str  Folder where markdown page file and images folder created
    - destinationPath: str Path for folder under memex where content will be placed
    """

#    destinationPath = f"{OUTPUT_FOLDER}/{pageXmlData['link'].replace(CURRENT_BLOG_URL, '')}"
#    sourcePath = page.replace("index.md", "")
#    print(f"$$$$$$ New Folder path: {destinationPath} old folderpath {sourcePath}" )

    #-- create the new folder if it doesn't exist 
    if not os.path.exists(destinationPath):
        os.makedirs(destinationPath)
    if os.path.exists(f"{sourcePath}/images"):
        os.makedirs(f"{destinationPath}/images", exist_ok=True)
        #-- copy the images folder contents
        shutil.copytree(f"{sourcePath}/images", f"{destinationPath}/images", dirs_exist_ok=True)

def generateCommentsString(xmlComments):
    """
    Turn an array of comment data structures from Wordpress into YAML frontmatter
    that can be inserted into the post/page markdown file

    Comments and pingbacks are split

    comments:
        - author: <author>
          author_url: <url>
          content: <content>
          date: <date>
    pingbacks:
        - author: <author>
          author_url: <url>
        - author: <author>
          author_url
        

    Params:
    - comments: array of comment data structures from Wordpress
    Returns:
    - commentsString: str  The YAML string to display the comments/pingbacks
    """

    #-- separate the comments and pingbacks
    comments = []
    pingbacks = []
    for comment in xmlComments:
        if comment['approved']=="0":
            continue
        if comment['type'] == "pingback":
            pingbacks.append(comment)
        else:
            #-- convert author "admin" to "David Jones"
            if comment['author'] == "admin":
                comment['author'] = "David Jones"
            comments.append(comment)

    commentString = yaml.dump(comments)
    # TODO need to add <br />
    # indent comment string by 4 spaces
    commentString = re.sub(r"^", "    ", commentString, flags=re.MULTILINE)
    pingbackString = yaml.dump(pingbacks)
    pingbackString = re.sub(r"^", "    ", pingbackString, flags=re.MULTILINE)

    return f"comments:\n{commentString}\npingbacks:\n{pingbackString}\n"

def writeMemexIndex( memexPath, pageData, pageXmlData ):
    """
    Write the index.md file for a given page/post in the appropriate folder

    - Add additional YAML 
        - type
        - template

    - Add pre-amble to beginning of markdown
        - admonition for post date, tags, categories
        - See also links
    """

#    print("--------- pageXmlData")
#    pprint(pageXmlData)
#    print("--------- pageData")
#    print("--------- pageData")
#    pprint(pageData["yaml"])
#    pprint(pageData)
#    quit()
#    print(f"\nWriting index.md for {pageXmlData['title']} to {memexPath}/index.md")

    with open(f"{memexPath}/index.md", "w", encoding="utf-8") as f:
        #-- write the frontmatter
        f.write("---\n")
        yamlData = pageData['yaml']
        #-- remove the author key from the yamlData
        yamlData.pop("author", None)
        if "title" in yamlData:
            if ":" in yamlData["title"] or "#" in yamlData["title"]:
                yamlData["title"] = f'"{yamlData["title"]}"'
            if '\"' in yamlData["title"]:
                #-- remove the backslash from the title
                yamlData["title"] = yamlData["title"].replace('\\\"', '\"')
        yaml.dump(yamlData, f)

            #f.write(f"{key}: {pageData['yaml'][key]}\n")
#            print(f"Writing {key}: {pageData['yaml'][key]}")
        #-- add in memex frontmatter
        f.write(f"type: {pageXmlData['post_type']}\n")
        f.write(f"template: blog-post.html\n")

        #-- write comments
        if len(pageXmlData['comments'])>0:
            pprint(pageXmlData['comments'])
            commentString = generateCommentsString(pageXmlData['comments'])
            print(commentString)
            f.write(commentString)
#        if "categories" in pageXmlData and len(pageXmlData['categories']) > 0:
#            pprint(pageXmlData['categories'])
#            quit()
#            f.write(f"categories: [")
#            for category in pageXmlData['categories']:
#                f.write(f"{category}, ")
#            f.write("]\n")
        #-- need to add categories
        f.write("---\n")
        #----------- add in some additional pre-amble
        # add metadata for the post (date, tags, etc)
#        metaData = generateMetaDataMarkdown(pageXmlData)
#        f.write(f"\n{metaData}\n")

        #- see also links
#        f.write(f"\nSee also: [[blog-home | Home]]\n\n")
        #-- write the content
        f.write(pageData['content'])

#    if len(pageData['yaml']['categories']) > 1:
#        quit()

def generateMetaDataMarkdown(pageXmlData):
    """
    Convert XML data about a post into formatted markdown to be shown at the top of a post/page

    Showing at least post_date, tags, categories
    """

    dateObject = datetime.strptime( pageXmlData['post_date'], "%Y-%m-%d %H:%M:%S")
    postDateMd = f"**Post date:** {dateObject.strftime("%A, %B %d, %Y %I:%M %p")}\n"
    categoryMd = ""
    if 'categories' in pageXmlData and len(pageXmlData['categories']) > 0:
        categoryString = ""
        for category in pageXmlData['categories']:
            categoryString += f"[{category['name']}]({MEMEX_BLOG_URL}/category/{category['name']}.md) "
        categoryMd = f"    \n**Categories:** {categoryString} \n"
    ## create string tags by joining with commas
    tagMd = ""
    if 'tags' in pageXmlData and len(pageXmlData['tags']) > 0:
        tagMd = f"    <br />**Tags:** {', '.join( str(x) for x in pageXmlData['tags'])} <br />"

    return f"""
!!! info inline end ""

    {postDateMd}{categoryMd}{tagMd}
"""

def findXmlPost( xml, title, postDate, type="post"):
    """
    Return the Wordpress XML post matching the given title, post date, and type, but only if the post is published

    params:
    xml - the parsed XML data
    title - the title of the post to find
    postDate - full date/time when post was created
    type - the post type to find (page, post, attachment)
    """

    #-- remove any \" from the title"
    title = title.replace('\\\"', '\"')
    foundPosts = []
    #-- convert postDate to GMT from local zone
    gmtPostDate = ""
    if postDate != "":
        gmtPostDate = datetime.strptime(postDate, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%Y-%m-%d %H:%M:%S")

#    print(f"\nLOOKING Title: {title} Post date: {postDate} gmtPostDate: {gmtPostDate}")
    for post in xml["posts"]:
        if post['status'] != "publish":
            continue
#        print(f"Title: {post['title']} type {post['post_type']} status {post['status']}")
        if post['title'] == title:
#            print(f">>> FOUND Title: {title} Post Title: {post['title']} XML Post date: {post['post_date']} gmtPostDate: {gmtPostDate}")
            if post['post_type'] == type:
#                print(f">>> FOUND Title: {title} Post Title: {post['title']} XML Post date: {post['post_date']} gmtPostDate: {gmtPostDate}")
                if post['post_date'] == gmtPostDate:
                    foundPosts.append(post)

    if len(foundPosts) == 0:
        return None
    if len(foundPosts) == 1:
        return foundPosts[0]
    
#    pprint(foundPosts)
    raise Exception(f"Error: Found multiple posts with the same title {title} in XML...skipping")

def showPosts(data):
    """
    Dump out posts - test function

    data["posts"] contain all items, including attachment,post,page,
    """

    for post in data["posts"]:
        if post['status'] != "publish":
            continue
        if post["post_type"] != "page":
            continue
        if post["post_type"] == "attachment":
            continue

#        if len(post["comments"])==0:
#            continue
#        print(post['content'])
        print(f"Title: {post['title']} type {post['post_type']} status {post['status']}")
        print(f"Link: {post['link']}")
#        pprint(post["comments"])
        print("-" * 40)
#        input("Press Enter to continue...")

def reportOutcomes():
    """
    Called at completion to give a summary of operations
    """

    #-- identify broken links
    # - not actually doing this check
#    print(f"Found {len(BROKEN_LINKS)} broken links")
#    pprint(BROKEN_LINKS)

if __name__ == "__main__":


    wordpressXml = parse(WORDPRESS_EXPORT_FILE)

    updatePages(wordpressXml)

    updatePosts(wordpressXml)


