#!/bin/zsh

# build the static html in ~/memex_site
mkdocs build
# generate the page index in ~/memex_site
python3 -m pagefind --site ~/memex_site
# remove the old pagefind index in ~/memex
rm -rf ~/memex/docs/pagefind
# update ~/memex pagefind index
cp -pfr ~/memex_site/pagefind ~/memex/docs/pagefind
