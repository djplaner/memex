﻿---
tags: web-development, javascript, vue, canvas, casa
title: Design of Canvas Learning Journal CASA 3
type: note
---
## Adopted approach

### Development

| Aspect | Approach |
| --- | --- |
| Javascript framework | Vue |
| UI framework | Quasar using SVG icons |

### Broad design

The Vue app will be implemented as a user script which modifies the Canvas "people" and "groups" pages.

Inline help links implemented with tooltips linking to a mkdocs site hosted on the github repo.

## Tasks

- [ ] [Adopt/adapt the Collections tooltip/help approach](#tooltiphelp-approach)
- [ ] Implement the root components for [the people](#people-page-root-component) and [group set pages](#group-set-page-root-component)
- [ ] Implement [the reporting mechanism](#reporting-mechanism) for the group set pages

## Tooltip/help approach

Install and implement a basic [mkdocs docs site](https://djplaner.github.io/canvas-learning-journal/).

Collections used a Object defined in each component of the structure 

```javascript
const HELP = {
    "<tooltipname>" : {
        tooltip: "tooltip html",
        url: "url to the help page"
    }
}
```
May be better to put this into a separate file with a global object that can be imported. Providing a level of redirection to add multi-language support if that ever becomes necessary.

[Vue cheatsheet for rendering data into html](https://dev.to/kontent_ai/vue-js-cheat-sheet-rendering-data-into-html-4d8g) is very useful

**Problem** Quasar tooltip component won't allow HTML as a tooltip - at least not from a variable. For now, sticking with just text.

**Solution** Ended up going with Shoelace as the icons were also problematic in Quasar.

## People page root component

Early implementation

## Group set page root component

Early implementation

Todo 

- "waiting" spinner for course data
- check on group set id prop matching an actual group set id
- implement functions to check if a group set is configured as a learning journal
- implement simple reporting
- implement creation functionality


## Reporting mechanism