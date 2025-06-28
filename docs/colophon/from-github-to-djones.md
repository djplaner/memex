---
backlinks:
- title: Memex - Version 3
  url: /memex/colophon/version-3-memex-design.html
tags:
- colophon
- github
- memex
title: Moving Memex from GitHub to djon.es
type: note
---
### Publish site

Site publication no longer happens on github pages. Instead use `mkdocs build` to create a local site in the fixed folder `~/memex_site`. A git repo connected to [djon.es/memex/](https://djon.es/memex/).

1. Pre-requisite: `~/memex_site` is a clone of ssh://djones@djon.es/home/djones/public_html/memex/
2. Use Foam locally editing markdown files as per normal.
3. When ready to publish updates 
   1. Run `mkdocs build` from the `memex` report to construct HTML in `~/memex_site` and now commit the updates 
   2. `cd ~/memex_site`
   3. `git add -u`
   4. `git commit -m "_Update text_"` **figure out how to add more in update text**
   5. `git push -u origin master`

### Update github published site

Run `mkdocs gh-deploy --force` from the `memex` folder


## Dev log

Possible approaches

1. **FAIL** GitHub using [git-deploy](https://www.frontendhero.dev/tutorial/deploying-github-commits-to-ftp-server/)

    Commit is only managing the markdown files, not the publishing of the site.

2. **FAIL** git-ftp

    Ditto, commit (locally) only doing the markdown files.

3. **FAIL** mkdocs build ; Cyberduck sync

    mkdocs build rebuilds the entire site, meaning that the entire site is uploaded each time.

4. **SUCCESS** mkdocs build to a git repo that is synced to djon.es

    - mkdocs build to a folder outside original _memex_ repo **not possible**
    - create a git repo within _site_ folder **DONE**
        - `git init .`
        - `git add --all`
        - `git commit -m "Initial commit"`
    - Test if git is able to pick up only changes with a new _mkdocs build_
        - Update this file
        - `mkdocs build`
        - `git add -u`
        - `git commit -m "First update"`
    - Can the repo be pushed to djon.es? _YES_
        See ["Hosting remote git repos with cpanel"](https://cpanel.net/blog/tips-and-tricks/hosting-remote-git-repositories-with-cpanel/) with the process 
        1. Create & upload ssh keys to djon.es