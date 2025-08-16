---
title: Intro to Webpack
---
## Possible steps for pathway-planner

1. Set up a dist directory and src directory
2. Make sure the code is distributed appropriately
3. Modify package.json and webpack.config.js
4. npm install the various requirements
5. Maybe install css-loader and style-loader

## Step 1 - [getting started](https://webpack.js.org/guides/getting-started/)

### Set up

src directory

- each javascript file imports its dependencies which webpack will use to produce optimised bundle

dist directory
- include main.js 
    - as the bundle

- npx webpack
  - Takes src/index.js as entry point and generates dist/main.js

- modify package.json to make private
- install dependencies with npm
    - _npm install --save_ for production bundle
    - _npm install --save-dev__ for development purposes

### Dev - npm script

Add a line to the package.json so that "build" runs webpack

### Asset Management

i.e. images, css files etc.  webpack handles those.  

Practice to use bundle.js rather than main.js?

css - style-loader and css-loader used to import CSS file from javascript.  Needs to be installed with npm .. these are dev dependencies

webpack config is used to specify how to handle these dependencies. i.e find css file and run css-loader and style-loader

images - need file-loader
But there are also [image-webpack-loader](https://github.com/tcoopman/image-webpack-loader) and [url-loader](https://webpack.js.org/loaders/url-loader/) that can minify and optise images

Before using those, current bundle.js is 75.2kb

### Loading data

Loading data from JSON is built in - but I'm not really doing that.  There are also CSV and xml loaders

### [Output management](https://webpack.js.org/guides/output-management/)