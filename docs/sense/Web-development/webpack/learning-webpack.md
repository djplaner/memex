---
backlinks:
- title: Web development
  url: /sense/Web-development/web-development.html
title: Learning Webpack
---
Finally grok Webpack.  ~/code/2021/webpack

## Testing process

Need to test by included in Blackboard

## Set up processes

### npm set up

- ```npm init -y``` - create initial default 
- ```npm i -D webpack webpack-cli``` - basic webpack
- ```npm i -D style-loader css-loader``` - add CSS to asset management
- ```npm i -D html-webpack-plugin``` - for output management
- ```npm i -D webpack-dev-server``` - development server
- ```npm i -D webpack-merge``` - handle separate production/dev configs

- ```npm start``` - run the dev server
- ```npm run build``` - build the bundle

### Basic development ideas

- Using multiple "entry points" for each component?, but not in a SPA?

### webpack.config.js



## Getting Started

[webpack getting started page](https://webpack.js.org/guides/getting-started/)

### Initial demo 

~WEBPACK/001_demo

Major topics covered
- Why using Webpack
- Allowing webpack to manage Javascript libraries, rather than include in html
- src is just a index.js file (in ```src```)
- output is put into ```dist``` which can then be loaded i.e. production
- webpack transpiles the ```import``` statements, but nothing else

Initial setup
- Just installing ```webpack``` and ```webpack-cli```
- setting ```"private": true,``` in package.json
- running with ```npx webpack```

Using a configuration
- adding npm commands ```scripts``` to work nicer, less typing (package.json)

### [Asset management](https://webpack.js.org/guides/asset-management/)

Essentially, treat other resources (e.g. images) like Javascript as part of Webpack depdendency management

- Talks about using css-loader and style-loader
- Other options to minimise css - postcss, sass
- Webpack 5 introduced Asset Modules to handle images, fonts and just about anything else that can sit in src

Loading data
- JSON, CSV, TSV, XML etc.
- JSON support built in with npm
- csv-loader and xml-loader are possible
- There are parsers for toml, yaml etc to convert to json

### [Output management](https://webpack.js.org/guides/output-management/)

- HtmlWebPackPlugin does some funky stuff with output management
- Will write it's own HTML file

### [Development](https://webpack.js.org/guides/development/)

- add ```mode: 'development'```
- source maps - mapping compiled code back to original

Choosing a development tool

### [Code splitting](https://webpack.js.org/guides/code-splitting/)

Sort of what entry points has been doing. Also *Prevent Duplication* and *Dynamic Imports*

But maybe not.  Also issues of sharing modules (e.g. lodash) across multiples

### Bundle analysis

Variosu tools to do this: analyze, webpack-chart, webpack-visualizer...bundle-stats

### [PRoduction](https://webpack.js.org/guides/production/)

Suggested to use separate configs for production and development.  But webpack-merge used to 

- Node environment variables mean we can check if we're in production/dev