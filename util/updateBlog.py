# updateBlog.py
# - Update blog posts on djon.es/blog from markdown files
#   in share/blog
# - still hard coded
# - TODO change to do "cached" updates of blog posts

#
# Markdown files for blog posts need to begin with some TOML config
# surrounded by --- e.g.
# ```
# post_title='Getting started with memex'
# layout="post"
# published=false
# id=17864
# link="https://djon.es/blog/2020/07/07/getting-started-with-memex/"
# category="memex"
# ```    

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

    x = re.match("#.*^```toml(.*)```(.*)", markDownData, re.MULTILINE | re.DOTALL  )
    print(x)
    print(x[1])

    postConfig = toml.loads( x[1] )
    postContent = x[2] 

    return (postConfig, postContent )

def updatePost( config, content ):

    blog = Client(settings.blogXmlRpc, settings.blogUsername, 
	                        settings.blogPassword )

    post = WordPressPost()

    post.title = config['post_title']
    post.id = config['id']
    post.terms_names={}
    post.terms_names['category'] = config['category']

    post.content = markdown.markdown(content)

    myposts = blog.call(EditPost(post.id, post ))

#-----------------------------------------------------------

def main(): 
	if len(sys.argv)==2: 
		markDownFile=sys.argv[1] 
		
		(config, content ) = getFile( markDownFile ) 
		print( "CONFIG\n%s" %config ) 
		print( "Content\n%s" %content ) 
		
		updatePost( config, content ) 
		
		return False

#    	myposts = blog.call(posts.GetPosts())

#    	for post in myposts:
#        	print("XXXXXXXXXXXXXXXXXXXX ")
#        	print("Id: %s. TITLE %s" % ( post.id,post.title))
#        	print("Link: %s " % post.link )


if __name__=="__main__":
	main()