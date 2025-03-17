
#import frontmatter
import markdown
import re
from bs4 import BeautifulSoup
import frontmatter
from pprint import pprint


# open calls using mkdocs-gen-files inherently uses docs
#DOC_FOLDER = "use mkdocs-gen-files to get docs folder"
GARDEN_FOLDER = "sense/landscape-garden/"
DOCS_FOLDER="/Users/davidjones/memex/docs/"
PLANTS_FOLDER = f"{DOCS_FOLDER}sense/landscape-garden/plants/"

def extractFrontMatter(path):
    """
    Given path local to DOCS_FOLDER for a markdown file, extract the front matter
    and return it"""

    with open(path, "r") as f:
        content = f.read()
        fMatter = frontmatter.loads(content)
        return fMatter.metadata

    return {}

def extractFrontMatterPython(path):
    """
    Given path local to DOCS_FOLDER for a markdown file, extract the front matter
    and return it"""

    md = markdown.Markdown(extensions = ['meta'])
    pageData = {}
    with open(path, encoding="utf-8-sig") as f:
        pageData["content"] = f.read()
        html = md.convert(pageData["content"])
        pageData['yaml'] = md.Meta
        pageData['html'] = html

        print(pageData['yaml'])
        print("------- YAML AFTER")
        
        for key in pageData['yaml'].keys():
            pageData['yaml'][key] = pageData['yaml'][key][0]
            # remove any quotes surrounding the value
            pageData['yaml'][key] = pageData['yaml'][key].lstrip('\"').rstrip('\"')
            print(f"{key}: {pageData['yaml'][key]}")

        #fMatter = frontmatter.load(content)
#        fMatter = frontmatter.load(f)

    return pageData

def extractFigures(html):
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
        match = captionRE.search(str(figureTag))
        if match:
            figureComponents['caption'] = match.group(1)

        if figureComponents['image_path'] != "":
            figures[figureComponents['image_path']] = figureComponents

    return figures



#path=f"{PLANTS_FOLDER}asparagus-africanus.md"
path=f"{PLANTS_FOLDER}schinus-terebinthifolia.md"
path=f"{PLANTS_FOLDER}the-original-island-bunya-pine.md"
results = extractFrontMatterPython(path)
frontMatter = extractFrontMatter(path)
print("-------- FRONT MATTER")
print(frontMatter)
print("--------")
figures = extractFigures(results['html'])

print("-------- FIGURES")
print(figures)
#print("--------")

#for key in results.keys():
#    print(f"{key}: {results[key]}")
