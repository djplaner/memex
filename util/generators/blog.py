"""
FILE:   blog.py
PURPOSE: Use mkdocs-gen-file to dynamically generate various blog pages

- categories blog/category/<categoryName>.md
    List of posts in a category
- tags blog/tag/<tagName>.md
    List of posts in a tag
- monthly archives blog/YYYY/MM/index.md
    One for each.

Process
- Retrieve data all blog pages/posts
    - category[<categoryName>] - array of links to posts/pages
    - tags[<tagName>] - array of links to posts/pages
    - archives[YYYY/MM] - array of links to posts/pages
- Call different functions to generate the relative pages
"""

import re
import glob
import mkdocs_gen_files
import logging
# import frontmatter
#import markdown
#from bs4 import BeautifulSoup
from pprint import pprint

BLOG_FOLDER = "blog/"


def generateCategoryPage(categoryName, categoryPages):
    """
    """


    #with mkdocs_gen_files.open(f"blog/category/{categoryName}.md", "w") as f:
    with mkdocs_gen_files.open(f"blog/category/{categoryName}.md", "w") as f:
        print(f"#### Generating category page for {categoryName} at blog/category/{categoryName}.md")
        f.write(f"""---
title: Items for category {categoryName}
type: blog_category
---

# Items for category {categoryName}

See also: [[blog-home]], [[posts]], [[pages]]

- [[blog-home]]
- [[pkm]]
""")
    mkdocs_gen_files.set_edit_path( f"blog/category/{categoryName}.md", "blog.py")

def generateCategories(categories={}):
    """
    Generate all categories
    """

    categoryNames = [ "#dlrn15", "4paths", "5rs", "academicdevelopment", "addie", "alignment", "anu", "ascilite", "asciliteMentor", "bad", "bam", "bambimbad", "bim", "bim2", "bimErrors", "blackboardIndicators", "bricolage", "c2d2", "casa", "cck09", "Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "coding", "cognitiveEdge", "colophon", "complexityLeadership", "computationalThinking", "concretelounge", "concretelounges", "connectedcourses", "courseSites", "cquLearningHistory", "curriculumDesign", "curriculumMapping", "dejavu", "design theory", "development", "digitalIgnorance", "distributedcognition", "dlrn", "design-theory", "dLRN15", "dojo", "e-learning", "eating", "edc3100", "eded20455", "eded20456", "eded20458", "eded20487", "eded20488", "EDED20491", "edm8006", "eds4406", "edu8117", "edu8719", "eei", "eep", "elearning", "emd", "enterprise 2.0", "etmooc", "evaluation", "exploring", "fad", "FedWiki", "foult", "futures", "games", "herding cats", "highereducation", "ict", "iLecture", "indicators", "information systems", "innovation", "intuitionFail", "ipt", "irac", "journey", "lak11", "learningAnalytics", "literacies", "lmsEvaluation", "lmsreview", "lxdesign", "math", "mathematics", "mav", "memex", "missingPs", "moneyburner", "moodle", "moodleopenbook", "music", "narrative", "netgl", "ngl", "nvivo", "oasis", "oasm", "ocw", "oep", "oer", "open", "openbook", "opencase", "Outcomes And Analytics", "paperIdeas", "paris2008", "patterns", "phd", "photography", "pirac", "pkm", "plagiarism", "ple", "ples@CQUni", "plos", "presentations", "protean", "PsFramework", "pstn", "publication", "publications", "qilters", "quotes", "react", "react2008", "Reading", "redesign", "reflectivealignment", "research", "sdo", "secondLife", "set", "shadowsystems", "site2016", "tam", "teachered", "teaching", "theory", "thesis", "to read", "tools", "tpack", "twitter", "Uncategorized", "uxdesign", "visitor", "voiceThreadResearchPosters", "votapedia", "WCYDWT", "web 2.0 course sites", "web3dx", "webfuse", "WebfuseReflectionsImplications", "website"]

    for name in categoryNames:
        generateCategoryPage(name, [ ] )

def retrieveBlogItems(blogFolder=BLOG_FOLDER):
    """
    Retrieve all blog posts/pages from blogFolder, skipping 
    - category, tag and archive pages 

    Generate
    - category[<categoryName>] - array of links to posts/pages
    - tags[<tagName>] - array of links to posts/pages
    - archives[YYYY/MM] - array of links to posts/pages
    """

    # TODO how to exclude a bunch of files - before or after glob
    files = glob.glob(f"{blogFolder}*.md")
    pages = []

#    for file in files:
        # -- remove DOCS_FOLDER from file

    # TODO figure out what to return


def extractFileContent(path):
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

    # TODO implement
    #blogItems = retrieveBlogItems()

    # TODO pass in categories from blogItems
    generateCategories()


generator()
