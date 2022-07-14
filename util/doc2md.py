"""
doc2md.py
- Convert a given Word document to markdown
"""

from logging import exception
import mammoth
import html2markdown
from pathlib import Path
import os
import argparse
from pprint import pprint

from bs4 import BeautifulSoup

DESTINATION = r"C:\\Users\\s2986288\\code\\Content-Interface-Tweak\\docs"
# DESTINATION="\\staff.ad.griffith.edu.au\ud\fr\s2986288\Documents\GitHub\Card-Interface-Tweak\docs"

# SOURCE=r"C:\\Users\\s2986288\\OneDrive - Griffith University\\Software Development\\Documentation\\Card Interface Demo-Instructions"
SOURCE = r"C:\\Users\\s2986288\\code\\Content-Interface-Tweak\\documentation"

CSS = """
<link rel="stylesheet" type="text/css"
   href="https://s3.amazonaws.com/filebucketdave/banner.js/gu_study_md.css">
"""


STYLE_MAP = """
     p[style-name='Section Title'] => h1:fresh
     p[style-name='Quote'] => blockquote:fresh
     p[style-name='Quotations'] => blockquote:fresh
     p[style-name='Quotation'] => blockquote:fresh
     p[style-name='Body Text'] => p:fresh
     p[style-name='Text'] => p:fresh
     p[style-name='Default'] => p:fresh
     p[style-name='Normal (Web)'] => p:fresh
     p[style-name='Normal'] => p:fresh
     p[style-name='Text body'] => p:fresh
     p[style-name='Textbody1'] => p:fresh
     p[style-name='Picture'] => div.picture > p:fresh
     p[style-name='Picture Right'] => div.pictureRight
     p[style-name='PictureRight'] => div.pictureRight
     r[style-name='University Date'] => span.universityDate
     p[style-name='Video'] => div.video
     p[style-name='Film Watching Options'] => div.filmWatchingOptions
     r[style-name='Checkbox Char'] => span.checkbox
     p[style-name='Checkbox'] => span.checkbox
     p[style-name='ActivityTitle'] => div.activity > h2:fresh
     p[style-name='Activity Title'] => div.activity > h2:fresh
     p[style-name='ActivityText'] => div.activity > div.instructions > p:fresh
     p[style-name='Activity Text'] => div.activity > div.instructions > p:fresh
     p[style-name='Activity']:ordered-list(1) => div.activity > div.instructions > ol > li:fresh
     p[style-name='Activity']:unordered-list(1) => div.activity > div.instructions > ul > li:fresh
     p[style-name='Activity'] => div.activity > div.instructions > p:fresh
     p[style-name='Bibliography'] => div.apa > p:fresh
     p[style-name='Reading']:ordered-list(1) => div.reading > div.instructions > ol > li:fresh
     p[style-name='Reading']:unordered-list(1) => div.reading > div.instructions > ul > li:fresh
     p[style-name='Reading'] => div.reading > div.instructions > p:fresh
     p[style-name='Title'] => h1
     p[style-name='Card'] => div.gu_card
     r[style-name='Emphasis'] => em:fresh
     p[style-name='Timeout'] => span.timeout
     p[style-name='Embed'] => span.embed
     p[style-name='Note']:ordered-list(1) => div.ael-note > div.instructions > ol > li:fresh
     p[style-name='Note']:unordered-list(1) => div.ael-note > div.instructions > ul > li:fresh
     p[style-name='Note'] => div.ael-note > div.instructions > p:fresh
     p[style-name='Blackboard Card'] => div.bbCard:fresh
     p[style-name='Heading 1'] => h2
     p[style-name='Heading 2'] => h3
     p[style-name='Heading 3'] => h4
     p[style-name='Blackboard Item Heading'] => h2.blackboard
     p[style-name='Blackboard Item Heading 2'] => h1.blackboard
     r[style-name='Blackboard Item Link'] => span.blackboardLink
     p[style-name='Blackboard Item Link'] => span.blackboardlink
     r[style-name='Blackboard Item Link Char'] => span.blackboardLink
     r[style-name='Blackboard Content Link'] => span.blackboardContentLink
     r[style-name='Blackboard Menu Link'] => span.blackboardMenuLink
     r[style-name='small'] => span.smallText
     r[style-name='StrongCentered'] => span.strongCentered
     r[style-name='Centered'] => span.centered
     u => u
"""

# -- what and why
# mammoth "${SOURCE}\Card Demo - update styles.docx" --output-format=markdown > "${DESTINATION}\whatWhy.md"o_html()

# ----------------------------------
# html = updateHtml( inHtml)
# - do some processing on the HTML to prepare for github

STYLE_PREPEND = {
    "reading": '<div class="readingImage"></div>',
    "activity": '<div class="activityImage"></div>',
    "flashback": '<div class="flashbackImage"><img src="https://s3.amazonaws.com/filebucketdave/banner.js/images/com14/flashback.png" alt="Flashback logo" /></div>',
    "canaryExercise": '<div class="canaryImage"><img src="https://s3.amazonaws.com/filebucketdave/banner.js/images/com14/Tweety.svg.png"  alt="Tweety bird"  /></div>',
    "ael-note": '<div class="noteImage"></div>',
    "weeklyWorkout": '<div class="weeklyWorkoutImage"><img src="https://filebucketdave.s3.amazonaws.com/banner.js/images/com14/weeklyWorkout.png" alt="Female weight lifter" /></div>',
    "comingSoon": '<div class="comingSoonImage"></div>',
}


def updateHtml(inHtml):
    soup = BeautifulSoup(inHtml, features="html5lib")

    # Look for embed objects and translate HTML entities to HTML tags
    for span in soup.findAll('span', {'class': 'embed'}):
        # sometimes .string is None but there is stuff in .txt
        if span.string is None:
            span.string = span.text
            if span.string is None:
                continue
        newSoup = BeautifulSoup(span.string, 'html.parser')
        span.string.replace_with(newSoup)

    #-- remove all img tags
    for img in soup.findAll('img'):
        img.decompose()

    # work through STYLE_PREPEND and prepend the specified
    for divClass in STYLE_PREPEND:
        # loop through each div with the class
        for divElement in soup.findAll('div', {'class': divClass}):
            toAppend = BeautifulSoup(STYLE_PREPEND[divClass], 'html.parser')
            divElement.insert(0, toAppend)

    return soup.body.encode_contents()


def convertWordDoc(wordDocFileName):
	"""
	Given the filename/path for a Word doc, convert it to HTML and return the HTML
	"""
	with open(wordDocFileName, "rb") as docx_file:
		print(f"Converting {wordDocFileName} to HTML")
		result = mammoth.convert_to_html(docx_file, style_map=STYLE_MAP)
		print(f"Conversion complete")
#		print(result)
		html = updateHtml(result.value) 

		md = html2markdown.convert(html)
		return md
#            with open( page["DESTINATION"], "w", encoding="utf-8") as md_file:
#                md_file.write(CSS) # add some css at the end
#                md_file.write(md)
#        print(result.value)


def parseArgs():
	""" Return dict containing arguments
	- wordDoc - filename for the Word doc to convert
	""" 

	parser = argparse.ArgumentParser( description="convert a Word document to markdown (stdout)") 
	parser.add_argument('wordDoc', action="store")
#    parser.add_argument("--folder", action="store",
#                        default=settings.MIGRATION_FOLDER) 
	args = parser.parse_args()

	return args


if __name__ == "__main__":
	args = parseArgs()

	print(f"Converting {args.wordDoc}")
	try: 
		html = convertWordDoc( args.wordDoc)
		print(html)
	except Exception as e:
		print(f"Error: {e}")


