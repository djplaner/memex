"""
util/corpus.py

PURPOSE: Define corpus-related utilities for the memex project

Constructor accepts various parameters of two types
- Metadata parameters (e.g., type, date range)
- Other e.g. location etc.
"""

FULL_DOCS_FOLDER = "/Users/davidjones/memex/docs/"
DOCS_FOLDER=""

import glob
import pathlib
import frontmatter
import re
from pprint import pprint

class corpus:
    """
    A class to represent a corpus of Memex bubbles.
    
    Attributes:
        type (str): bubble type, default is None (i.e. all bubbles)
        paths (list): list of paths in which to search for bubbles
                 default is ["/"] (i.e. root path) 
                 paths are relative to the FULL_DOCS_FOLDER
    """

    def __init__(self, type=None, paths = ["/"] ):
        self.type = type
        self.paths = paths
        # retrieve corpus items
        self.bubbles = self._retrieve_corpus_bubbles()

    def __len__(self):
        return len(self.bubbles)

    def __iter__(self):
        # This method should return an iterator over the corpus items
        return iter(self.bubbles)

    def __next__(self):
        return next(self.bubbles)

    def __getitem__(self, key):
        # This method should allow access to items in the corpus by key
        pass

    def _retrieve_corpus_bubbles(self):
        """
        Retrieve items from the corpus based on the type.
        This is a placeholder for the actual implementation.
        """
        
        ## generate a list of files based on the paths
        files = self._get_fileNames_from_paths()

#        print(f"Retrieving corpus items from paths: {self.paths}")
#        print(f"Found {len(files)} files in the corpus.")
#        print(f"Files: {files}")

        bubbles = []
        for path in files:
            #-- extract the file content and metadata
            bubble = self._extract_file_content(path)
            #-- decide if the bubble should be included in the corpus
            if self._include_bubble(bubble):
                bubbles.append(bubble)
#            bubbles.append(bubble)

        return bubbles


    def _get_fileNames_from_paths(self):
        """
        Retrieve all file names for bubbles from the specified paths."""

        files = []
        
        for path in self.paths:
            #-- if path is a relative path, prepend the FULL_DOCS_FOLDER
            if not path.startswith(FULL_DOCS_FOLDER):
                path = FULL_DOCS_FOLDER + path
            
            #print(f"Searching for files in path: {path}")
            #-- get all files in the path
#            files += glob.glob(f"{path}*.md")
            folder = pathlib.Path(path)
            files += list(folder.rglob("*.md"))  

        return files


    def _include_bubble(self, bubble) -> bool:
        """
        Decide if the bubble should be included in the corpus based on its type.

        Currently only checks the file type
        
        Parameters:
            bubble (dict): The bubble to check.
        
        Returns:
            bool: True if the bubble should be included, False otherwise.
        """
        #-- if type is None, include all bubbles
        if self.type is None:
            return True
        
        #-- if bubble has a type and it matches the corpus type, include it
        if 'type' in bubble['yaml'] and bubble['yaml']['type'] == self.type:
            return True
        
        return False

    def _extract_file_content( self, path ) -> dict:
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
        docsFile = str(path).replace(FULL_DOCS_FOLDER, "")
        #print(f"Extracting content from {path} -> {docsFile}")
#        input("Press Enter to continue...")

        with open(path, encoding="utf-8-sig") as f:
#    with mkdocs_gen_files.open(docsFile, 'r', encoding="utf-8-sig") as f:
            bubble = frontmatter.load(f)

#        bubble = frontmatter.loads(content)


        pageData['content'] = bubble.content
        pageData['yaml'] = bubble.metadata
        pageData['filePath'] = str(path)
        #pageData['filePath'] = file.src_path

        pageData = self._extract_link_defs(pageData)
        #pprint(pageData)
#        input("Press Enter to continue...")

        return pageData

    def _extract_link_defs(self, pageData):
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

        pageData['linkDefs'] = self._generate_absolute_links(pageData['filePath'], pageData['linkDefs']) 

        return pageData

    def _generate_absolute_links(self, markdownFile, linkDefs):
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

#        print(f"Generating absolute links for {markdownFile} in folder {currentFolder}")
#        input("Press Enter to continue...")

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
            #-- TODO what to do when running as a macro??
            #absPath = absPath.replace("/Users/davidjones/memex/", "")
            #-- if absPath starts with /, remove it
            #-- TODO turn on with macro
            #if absPath.startswith("/"):
            #    absPath = absPath[1:]

#        print(f"Link {link} -> {absPath}")

            newLinkDefs[absPath] = {
                'text': linkDefs[link]['text'],
                'description': linkDefs[link]['description']
            }

        return newLinkDefs

    def get_bubble_by_type(self, bubble_type):
        """
        Get a list of all bubbles of a specific type.
        """
        #return [bubble for bubble in self.bubbles if bubble== bubble_type]

        bubbles = []
        for bubble in self.bubbles:

            yaml = bubble.get("yaml", {})
            if not yaml:
                continue
            type = yaml.get("type", "")
            if type == bubble_type:
                bubbles.append(bubble)

        return bubbles

    def get_bubbles_by_frontmatter(self , matter : dict ):
        """
        Get a list of all bubbles where the frontmatter matches the "frontmatter" provided in the format
        {
            title: <string>,
            type: <string>,
            tags: [<string>, <string>, ...],
            <string>: <string>,
        }
        
        :param self: corpus of all bubbles within Memex
        :param matter: Dict specifying frontmatter key-value pairs to match

        **todo** 
        - currently only matches exact values for all entries in matter. Provide an option to match if any of the entries match

        """

        bubbles = []
        for bubble in self.bubbles:

            yaml = bubble.get("yaml", {})
            if not yaml:
                continue

            match = True
            for key in matter:
                if key not in yaml:
                    match = False
                    break
                #-- if the value is a list, check if all items are in the yaml list
                if isinstance(matter[key], list):
                    if not all(item in yaml[key] for item in matter[key]):
                        match = False
                        break
                else:
                    if yaml[key] != matter[key]:
                        match = False
                        break

            if match:
                bubbles.append(bubble)

        return bubbles