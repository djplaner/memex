# extractWikity.py
# - extract contents of wikity and insert into memex (eventually)

import sys
from slugify import slugify
import os
import markdown
import toml
import re
 
from simple_settings import settings

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import EditPost,GetPost
from wordpress_xmlrpc import WordPressPost

def getFile( markDownFile ):
    with open(markDownFile) as f:
        markDownData = f.read()
    f.close()

    print("--------------- original -------------")
    print(markDownData)
    print("--------------- HTML -------------")
    print(markdown.markdown(markDownData))

    x = re.match("^---(.*)---(.*)", markDownData, re.M | re.S  )
    print(x)
    print(x[1])

    postConfig = toml.loads( x[1] )
    postContent = x[2] 

    return (postConfig, postContent )

#-----------------------------------------------
# get a list of posts
def getPostList( idList ):
    blog = Client(settings.wikityXmlRpc, settings.wikityUsername, 
                 settings.wikityPassword )

    posts = []

    for id in idList: 
        post = blog.call(GetPost(id))
        posts.append(post)

    return posts
    
#-----------------------------------------------------
# getPosts
# - extract all of the posts from the blog
# - divide the into two arrays cards and cardBoxes and
#   return the two arrays

def getPosts(  ):
    blog = Client(settings.wikityXmlRpc, settings.wikityUsername, 
                 settings.wikityPassword )

    cards = []
    cardBoxes = []

    offset = 0
    increment = 20
    while True:
        print("Getting from %s to %s" % ( offset, offset+increment))
        postList = blog.call(posts.GetPosts({'number': increment, 'offset': offset}))
        if len(postList) == 0: 
            break  # no more posts returned
        for post in postList:
            if post.title.startswith("CardBox::" ):
                cardBoxes.append(post)
            else:
                cards.append(post)
        offset = offset + increment

    return( cardBoxes, cards)

#-----------------------------------------------------------
# displayPosts( posts)
# - given an array of posts disply their titles and contents

def displayPosts( posts ):

    for post in posts:
        print("_____________________")
        print("id %s title %s"%(post.id,post.title))
        print(post.content)

#-----------------------------------------------------------
# makeCardBoxDirectories
# - given a list of posts with card boxes
# - create directories in memexHome/sense/ for each cardBox
#   using the title
# - This is where cards matching that cardBox will be placed

def makeCardBoxDirectories(cardBoxes):
    rex = re.compile("CardBox:: (.*)")
    for box in cardBoxes: 
        m = rex.search( box.title) 
        if m: 
            print("Title %s directory %s" % (box.title, 
                    "%ssense/%s" % (settings.memexHome,m[1]))) 
                    
            try:
               os.mkdir("%ssense/%s" % (settings.memexHome,m[1]))
            except OSError:
                print("Failed making directory")
        

#-----------------------------------------------------------
# makeCardBoxNotes
# - given a list of posts with card boxes
# - add files into sense that contain the contents using following
#   format
# # Title (path)
#
# ## Description
#
# TODO
#
# ## Path
#
# - first card link
# - second card link
#

CARD_BOX_TOP="""\
# TITLE

## Path

"""

def makeCardBoxNotes(cardBoxes):
    print("-------------- make Card Box notes")
    rex = re.compile("CardBox:: (.*)")
    for box in cardBoxes: 
        print("---- %s" % box.title)
        m = rex.search( box.title) 
        if m: 
            print("Title %s directory %s" % (box.title, 
                    "%ssense/%s" % (settings.memexHome,m[1]))) 
            
            title = m[1]
            path = "%ssense/%s.md" % ( settings.memexHome, title)

            content = CARD_BOX_TOP.replace("TITLE", title)

            print(content)

            crex = re.compile("\[\[(.*)]]$", re.M)
            matches = re.findall(crex, box.content)

            for match in matches:
                content = content + "- [%s](%s/%s)\n" %( match, title, match )

            content = content + "\n"
            #print( content )

            print("Path is %s"%path)
            with open(path, 'w') as f:
               f.write(content)
               f.close()

    print("------------------------ FINISH ")
                
            
#-----------------------------------------------------------
# writePosts( Category, posts)
# - given a list of posts and the category to which they belong
#   output individual markdown files for each card in the category folder

POST_TEMPLATE="""\
# TITLE

CONTENT

### Related categories

"""

def writePosts(membership, posts):

    for post in posts:
        #-- get HTML
        print("----- TITLE %s" %post.title)

        content = POST_TEMPLATE.replace("TITLE", post.title)
        content = content.replace("CONTENT", post.content)

        #-- calculate category
        category = 'loose'
        if post.title in membership:
            category = membership[post.title]

        #-- add the category "backlink"
        content = content + "- [%s](../%s)\n"%(category,category)

        #-- open and write file
        path = "%ssense/%s/%s.md" % ( settings.memexHome, category, post.title.replace("/",""))

#        print("  --- Path is %s"%path)
#        print( content )
#        print("---------------")
        with open(path, 'w') as f:
           f.write(content)
           f.close()
                    

#-----------------------------------------------------------
# displayCardBoxes( posts )

def displayCardBoxes( posts):

    for box in posts:
        print( "%s"%box.title)

#-------------------------------
# categoriseCards( cardBoxes)
# - return hash keyed on card titles which indicates which card boxes they belong to

def categoriseCards( cardBoxes ):

    categories = {}
    rex = re.compile("CardBox:: (.*)")
    for box in cardBoxes: 
        print("---- %s" % box.title)
        m = rex.search( box.title) 
        if m: 
            title = m[1]

            #-- get the names of the cards in the box
            crex = re.compile("\[\[(.*)]]$", re.M)
            matches = re.findall(crex, box.content)

            for match in matches:
                categories[match] = title

    return categories

#-----------------------------------------------------------

def main(): 

# --- get an initial cardbox
#    posts = getPostList( [71] )
#    post = posts[0]
#    print(post)
#    print(post.content)
#    cardBoxes = []
#    cardBoxes.append(post)

    #-- want card ids for Quality 39, Quality enhancement 42, Teaching quality 72

#    posts = getPostList( [39, 42, 72])
    #displayPosts(posts)

    #makeCardNotes( cards)
    #addCardBoxList( cardBoxes)
    #addLooseCards(cards)

    (cardBoxes, cards) = getPosts()

    #-- get hash of card titles that belong to categories
    membership = {}
    membership = categoriseCards( cardBoxes)

    print(membership)

    writePosts( membership, cards)

#    print("------------------- card boxes")
#    displayCardBoxes(cardBoxes) # DONE
 #   makeCardBoxDirectories( cardBoxes) # DONE
#    makeCardBoxNotes( cardBoxes) # DONE
#    print("------------------- cards")
#    displayPosts(cards)


if __name__=="__main__":
	main()