---
backlinks:
- title: Web development
  url: /sense/Web-development/web-development.html
title: NPM Projects - How to
---
Trying to figure out and document a process for developing NPM JS projects, mainly to take advantage of associated CDN availability of the modules.

I'm actually using [this process](https://auth0.com/blog/developing-npm-packages/)

## NPM Docs

Start with the [NPM docs](https://docs.npmjs.com/packages-and-modules) focus on packages and modules

### Packages

- Described by a package.json - [creating a package.json](https://docs.npmjs.com/creating-a-package-json-file)
- Scope - [scoped/unscoped and public/private](https://docs.npmjs.com/package-scope-access-level-and-visibility)
	- unscoped packages are alway spublic
### Modules

- anything in the ```node_modules``` directory that can be loaded by Node.js


1. init - in folder
    ```npm init```

## Other tutorials

- [Learn how to develop npm packages](https://auth0.com/blog/developing-npm-packages/)
- [How to make tiny npm package](https://www.freecodecamp.org/news/how-to-make-a-beautiful-tiny-npm-package-and-publish-it-2881d4307f78/)