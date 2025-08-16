---
title: Webpack essentials
---
## Background

Based [on this video](https://www.youtube.com/watch?v=lFjinlwpcHY)

Start with a npm project 

1. Install 
   1. webpack and webpack-cli 
   2. Loaders - transform various types of source files ready for bundling
   3. Plugins - transform the bundle after it's created
2. Configure
   1. The entry point - into the source code
   2. Loaders (from webpack)
   3. Individual loader configuration (e.g. babel)
   4. Output - where the bundle goes
   5. Mode - production or dev
   6. How to run webpack: npm run build OR npm run start

### Installation

1. Initialise the project - npm init
2. npm install webpack webpack-cli --save-dev
3. Loaders
   1. npm install svg-inline-loader --save-dev
   2. npm install css-loader style-loader --save-dev
   3. npm install babel-loader --save-dev
   4. npm install html-webpack-plugin --save-dev
4. Dev server
   1. npm install webpack-dev-server --save-dev
5. babel https://www.robinwieruch.de/webpack-babel-setup-tutorial
   1. npm i -D @babel/core @babel/present-env
   2. npm i -D babel-loader    (the webpack loader for babel)


### Configuration file

```javascript
// webpack.config.js 
const HtmlWebPackPlugin = require('html-webpack-plugin')
const webpack = require('webpack')

module.exports = {
    entry: './app/index.js',
    module: {
        rules: [
            { test: /\.svg$/, use: 'svg-inline-loader' },
            { test: /\.css$/, use: [ 'style-loader', 'css-loader'] },
            { test: /\.js$/, use: 'babel-loader' }
        ]
    },
    plugins: [
        new HtmlWebPackPlugin(),
    ],
    mode: process.env.NODE_ENV === 'production' ? 'production':'development',
    "scripts": {
        "build": "NODE_ENV='production' webpack",
    },
    output: {
        path: path.resolve( __dirname, 'dist'),
        filename: 'index_bundle.js' 
    }
}
```