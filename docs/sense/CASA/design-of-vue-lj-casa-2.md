---
tags: web-development, javascript, vue, canvas, casa
title: Design of Canvas Learning Journal CASA 2
type: note
---
- [Choice of UI Framework](#choice-of-ui-framework)
  - [Integrate Quasar with user script](#integrate-quasar-with-user-script)
  - [Integrate Vuetify](#integrate-vuetify)
    - [UI Approach](#ui-approach)

## Choice of UI Framework

Choice seemed to be between 

- [Quasar](https://quasar.dev/)
- [Vuetify](https://vuetifyjs.com/en/)

Currently trying Quasar as more cross platform.

1. [x] Integrate Quasar component into current test **failed**
1. [ ] Integrate Vuetify component into current test **failed**

### Integrate Quasar with user script

Trying the [Vite plugin for Quasar](https://quasar.dev/start/vite-plugin) as first experiment

Problems getting this going, but then discover my GreaseMonkey dev environment uses [Ant Design Vue](https://antdv.com/docs/vue/introduce)

Couldn't get it to compile quickly

### Integrate Vuetify

- Early build working

    TO do 

        - [ ] [install icons](https://vuetifyjs.com/en/features/icon-fonts/#usage)

            Problem with the icons is that some of the pre-defined Canvas classes override the `v-icon` classes which vuetify relies upon. An early solution was to manually insert icons, but that doesn't work when we're moving to dynamic components (e.g. changing icons based on the state of an expansion panel)

            It appears the problem is something to do with the size of the icon.  i.e. removing the `v-icon--size-default` css class 
        - [ ] [consider vite plugin](https://www.npmjs.com/package/vite-plugin-vuetify)
- [X] Add a Vuetify component
- [ ] Add the expansion

#### UI Approach

1. Using [Quasar components](https://quasar.dev/vue-components)
2. icons - appears that the [quasar-extras-svg-icons](https://quasar-extras-svg-icons.netlify.app/all-about-quasar-extras-svg-icons/icon-finder) offer a way to work with Quasar