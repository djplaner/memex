"""
FILE: restBlog.py
DESCRIPTION: Experimentation with REST API for blog

Exploring the use of the REST API based on 
  https://robingeuens.com/blog/python-wordpress-api/
API reference
  https://developer.wordpress.org/rest-api/reference/posts/#create-a-post

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

"""

import requests
import base64
import sys
import io

import re

from slugify import slugify
from simple_settings import settings
from pprint import pprint

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


WORDPRESS_USER = "djblog"
WORDPRESS_PASSWD = settings.MEMEX
WORDPRESS_CREDENTIALS = f"{WORDPRESS_USER}:{WORDPRESS_PASSWD}"
WORDPRESS_TOKEN = base64.b64encode(WORDPRESS_CREDENTIALS.encode("utf-8"))
WORDPRESS_HEADER = {'Authorization': 'Basic ' +
                    WORDPRESS_TOKEN.decode('utf-8')}


def read_wordpress_posts():
    api_url = 'https://djon.es/blog/wp-json/wp/v2/posts?page=1&per_page=100'
    response = requests.get(api_url)
    response_json = response.json()
    print(response_json)


def create_wordpress_post( postDetails ):
    """
    @function create_wordpress_post
    @param postDetails: dict of post details
    @return: response
    @description: Create a new post on the wordpress blog
    """
    api_url = 'https://djon.es/blog/wp-json/wp/v2/posts'
#    data = {
#        'title': 'Example wordpress post',
#        'status': 'draft',
#        'slug': 'example-post',
#        'content': 'This is the content of the post'
#    }

    response = requests.post(api_url, headers=WORDPRESS_HEADER, json=postDetails)

    return response

def generateWordPressPost():
    """ 
    @function generateWordPressPost
    @return: dict of post details
    @description: Generate a dict of post details

    Current categories: bad casa
    """

    title = 'Example wordpress post'
    postDetails = {
        'title': title,
        'status': 'draft',     # publish, future, draft, pending, private
        'slug': slugify(title),
        'categories': [ "bad", "casa" ],
        #'tags': [],
        'content': 'This is the content of the post'
    }

    return postDetails


def main():
    """ 
    """

    print(f"WORDPRESS_USER={WORDPRESS_USER}")
    print(f"WORDPRESS_PASSWD={WORDPRESS_PASSWD}")

    #read_wordpress_posts()
    postDetails = generateWordPressPost()
    pprint(postDetails)
    #response = create_wordpress_post(postDetails)
    #print(response)


if __name__ == "__main__":
    main()
