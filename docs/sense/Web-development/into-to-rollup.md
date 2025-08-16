---
title: Into to Rollup
---
## [rollup-starter-app](https://github.com/rollup/rollup-starter-app)

Two folders: src (where the code sits) and public - HTML that includes bundle.js

rollup.config.js explains how to buil

npm run dev provides a live update

## [rollup-guide](https://rollupjs.org/guide/en/)

- Entry point for application - main.js
- imports etc - bundle.js

Uses ES Modules, not commonJS.  But commonJS can be used through plugin

### [Tutorial](https://rollupjs.org/guide/en/#creating-your-first-bundle)

Create the project folder, including src.

Create the entry point - main.js in src - including a supporting library

At that stage, they start running rollup manually

## [rollup-start-app](https://github.com/rollup/rollup-starter-app) applied to pathway planner

1. [X] Add and perhaps modify rollup.config.js
   - use PathWayPlanner.js for entry point 
2. [ ] Update package.json and perhaps .gitignore
3. [X] add **public** folder
4. [X] Copy index.html from src to public
6. [ ] Can taffydb be installed via npm?
7. [X] Update when and how the pathway-planner.css is imported
8. [ ] Install all the stuff that's included
   1. [ ] lit-element, lodash, accordion-container-component, navigo
10. [X] npm run build
11. [ ] npm run start