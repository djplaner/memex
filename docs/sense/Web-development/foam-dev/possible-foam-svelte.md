---
backlinks:
- title: Colophon
  url: /colophon/colophon.html
title: Possible ideas for a SvelteKit Foam site
---
Random collection of thoughts about if and how this might work.

## Routes/page structure

- Perhaps (early) the Foam md files are in the routes folder?
- Or, that gets generated manually or automatically - to provide some flexibility.
- i.e. the Svelte code can take various config files to provide a structure and combined different Foam stuff into different web sites/interfaces
- dynamic parameters could be used perhaps to generate the HTML on the fly - which could in turn be used to generate navigation files

Current idea
- Foam files remain in their folders
- SvelteKit project uses dynamic parameters as part of route to specify the "path" for the Foam file
- This is used to located the markdown file and then generate the HTML for the page
- Also to modify the navigation appropriately