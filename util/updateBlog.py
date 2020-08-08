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

from bs4 import BeautifulSoup
 
from simple_settings import settings

from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import EditPost
from wordpress_xmlrpc import WordPressPost


def getFile( markDownFile ):
    with open(markDownFile) as f:
        markDownData = f.read()
    f.close()

#    print("--------------- original -------------")
#    print(markDownData)
#    print("--------------- HTML -------------")
#    print(markdown.markdown(markDownData))

    #x = re.match(".*^toml(.*)```(.*)", markDownData, re.MULTILINE | re.DOTALL  )
    #x = re.match("#.*^```toml(.*)```", markDownData, re.DOTALL  )
    x = re.match("```toml([^`]*)```(.*)", markDownData, re.MULTILINE | re.DOTALL  )
    #x = re.match("#^```(toml)", markDownData, re.MULTILINE  )
#    print(x)
#    print("TOML")
#    print(x[1])
#    print("TOML")

    postConfig = toml.loads( x[1] )
    postContent = x[2] 

    return (postConfig, postContent )

def updatePost( config, html ):

    blog = Client(settings.blogXmlRpc, settings.blogUsername, 
	                        settings.blogPassword )

    post = WordPressPost()

    post.title = config['post_title']
    post.id = config['id']
    post.terms_names={}
    post.terms_names['category'] = config['category']
    post.content = html

#    post.content = markdown.markdown(content)

    myposts = blog.call(EditPost(post.id, post ))

#-----------------------------------------------------------
# html = changeImgURL( html, base_url)
# - change all the image links in html by adding base_url
# https://stackoverflow.com/questions/54921192/python-search-and-replace-all-img-tag-in-html-string

def changeImgURL( html, base_url):
    soup = BeautifulSoup(html)

    for img in soup.findAll('img'):
        img['src'] = base_url + img['src']

    #return str(soup.body)#.prettify()
    return soup.body.encode_contents()#.prettify()

#-----------------------------------------------------------

def main(): 
    if len(sys.argv)==2: 
        markDownFile=sys.argv[1] 
        (config, content ) = getFile( markDownFile ) 
        html = markdown.markdown(content)

        if "img_base_url" in config:
            print("**** change image base url %s"%config['img_base_url'])
            html = changeImgURL( html, config['img_base_url'] )
        print( "HTML content \n %s" % html )
        updatePost(config,html)
#		print( "CONFIG\n%s" %config ) 
#		print( "Content\n%s" %content ) 
		
#		updatePost( config, content ) 
		
		

        return False

#    	myposts = blog.call(posts.GetPosts())

#    	for post in myposts:
#        	print("XXXXXXXXXXXXXXXXXXXX ")
#        	print("Id: %s. TITLE %s" % ( post.id,post.title))
#        	print("Link: %s " % post.link )

if __name__=="__main__":
	main()
