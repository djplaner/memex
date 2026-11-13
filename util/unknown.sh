#!/bin/zsh

# Find all the unknown bubbles

for name in `find docs -name \*.md`; do
    if ! grep '^type: ' $name > /dev/null ; then
        echo $name
    fi
done

