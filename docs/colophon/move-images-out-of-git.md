---
title: Move images out of git
type: note
tags:
    - colophon
---

Due to laziness, I've been placing images into git for this site. Not a good idea since Git doesn't diff binary files, meaning whole copies of the image files are stored in the git history, bloating the size of the repository. Since the images (generally) don't change a lot it's not that bad, but...

For the record, the following table shows the number of images and the size of the git repository for the two sites. Memex is larger with fewer images (IMHO) because it's had a longer lifespan with some movement of images.

| Site | # Images | git repo size |
| --- | --- | --- |
| Memex (before move) | 323 | 289Mb |
| Blog (before move) | 1194 | 169 Mb | 

Necessary steps in the process, include:

1. [x] [Relocate the images outside of the git repo](#relocate-the-images-outside-of-the-git-repo)
2. [x] [Update the links in the markdown files](#update-the-links-in-the-markdown-files)
3. [x] [Copy the images to the web server](#copy-the-images-to-the-web-server)
4. [x] [Test the links](#test-the-links)
5. [ ] [Remove the images from the git repo](#remove-the-images-from-the-git-repo)

## Relocate the images outside of the git repo

[git-lfs](https://git-lfs.com/) appears to be one option, but that appears to require a git-lfs server. GitHub appears to provide such a service, but I'm wanting to reduce my reliance on big tech. I also don't to take on the maintenance of a git-lfs server (if that's possible).

Instead, the plan is to create a shared assets folder to be used by both the blog and the memex. This will be a folder that is not under git control. It will by `rsync`'d to the web server.

- Create the assets folder in home directory with the structure

    - `assets/memex/` - for memex images using the same folder structure as the memex `docs` folder
    - `assets/blog/` - for blog images using the same folder structure as the blog `docs` folder

TODO

- Python/shell script to copy the images from the git repo to the assets folder.

## Update the links in the markdown files

Python script to read all Markdown files, find images and update local (largely relative) links to absolute `/assets/memex/<path>/<fileName>` links.

## Copy the images to the web server

## Test the links

## Remove the images from the git repo

Perhaps not just the current and future removal, but also historically?
