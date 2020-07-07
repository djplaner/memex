import sys
import markdown
import toml
import re
 
from simple_settings import settings

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import EditPost
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

def updatePost( config, content ):

    blog = Client(settings.blogXmlRpc, username, password )

    post = WordPressPost()

    post.title = config['post_title']
    post.id = config['id']
    post.terms_names={}
    post.terms_names['category'] = config['category']

    post.content = markdown.markdown(content)

    myposts = blog.call(EditPost(post.id, post ))


if len(sys.argv)==2: 
    username=settings.blogUsername
    password=settings.blogPassword
    markDownFile=sys.argv[1]

    (config, content ) = getFile( markDownFile )

    print( "CONFIG\n%s" %config )
    print( "Content\n%s" %content )

    updatePost( config, content )
    print(XX)



    myposts = blog.call(posts.GetPosts())

    for post in myposts:
        print("XXXXXXXXXXXXXXXXXXXX ")
        print("Id: %s. TITLE %s" % ( post.id,post.title))
        print("Link: %s " % post.link )
