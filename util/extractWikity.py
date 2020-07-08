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

#-----------------------------------------------------------

def main(): 

    post = getPost( 154)

    print(post)
    print(post.content)

if __name__=="__main__":
	main()