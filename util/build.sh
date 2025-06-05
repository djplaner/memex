#!/bin/zsh

source ~/memex/.venv/bin/activate
mkdocs build
python3 -m pagefind --site ~/memex_site
