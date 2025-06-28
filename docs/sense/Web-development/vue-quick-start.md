---
backlinks:
- title: Learning Vue
  url: /memex/sense/Web-development/learning-vue.html
tags: web-development, javascript, vue
title: Vue quick start
type: note
---
Reference: [Vue quick start](https://vuejs.org/guide/quick-start.html)

## Creating a Vue Application

### Locally with a build tool 

Use the Vue project scaffolding tool `npm create vue@latest` and then `npm install` and away you go all the structure provided.

The HTML file has two main steps

1. Define a `div` element for the app 
2. Include the `main.js`

    Which in turn uses a `createApp` function to create the app and then `mount` it to the `div` element.

The SFC (Single File Component) is (typically) a `App.vue` file that contains the template, script and style all in one file. i.e. defining a component for the application.

Child components are defined in the `components` folder.

### Using a CDN

The Vue library can be included via a CDN and then the `Vue.createApp` function can be used to create the app and mount it to the `div` element.