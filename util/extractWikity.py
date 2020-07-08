# extractWikity.py
# - extract contents of wikity and insert into memex (eventually)

import sys
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

def main(): 

#    post = getPost( 154)
#    print(post)
#    print(post.content)

    (cardBoxes, cards) = getPosts()

    print("------------------- card boxes")
    displayPosts(cardBoxes)
    print("------------------- cards")
    displayPosts(cards)


if __name__=="__main__":
	main()