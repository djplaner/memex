#!/bin/zsh
# rsync ~/assets to djones

rsync -azvuPh ~/assets/ djones@djon.es:/home/djones/public_html/assets/

