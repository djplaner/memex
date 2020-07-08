# extractWikity.py
# - extract contents of wikity and insert into memex (eventually)

import sys
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

def getPost( id ):
    blog = Client(settings.wikityXmlRpc, settings.wikityUsername, 
                 settings.wikityPassword )

    post = blog.call(GetPost(id))

    return post
    
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
    rex = re.compile("CardBox:: (.*)")
    for box in cardBoxes: 
        m = rex.search( box.title) 
        if m: 
            print("Title %s directory %s" % (box.title, 
                    "%ssense/%s" % (settings.memexHome,m[1]))) 
            
            path = "%ssense/%s.md" % ( settings.memexHome,
                                m[1])

#            with open(path, 'w') as f:
#                f.write(CARD_BOX_TOP)

            content = CARD_BOX_TOP.replace("TITLE", m[1])

            print(content)

            rex = re.compile("\[\[(.*)]]$", re.M)
            matches = re.findall(rex, box.content)

            for match in matches:
                print( "- [[%s]]" %match)
                
            
                    


#-----------------------------------------------------------

def main(): 

    post = getPost( 71 )
    print(post)
    print(post.content)
    cardBoxes = []
    cardBoxes.append(post)
    makeCardBoxNotes( cardBoxes)

#    (cardBoxes, cards) = getPosts()

#    makeCardBoxDirectories( cardBoxes)

    #makeCardNotes( cards)

    #addCardBoxList( cardBoxes)
    #addLooseCards(cards)

#    print("------------------- card boxes")
#    displayPosts(cardBoxes)
#    print("------------------- cards")
#    displayPosts(cards)


if __name__=="__main__":
	main()