---
backlinks:
- title: Canvas work arounds
  url: /sense/Design/canvas/canvas-workarounds.html
title: Import rubrics to Canvas - userscript
---
[import-rubric](https://github.com/jamesjonesmath/canvancement/tree/master/rubrics/import-rubric) ([detailed documentation](https://community.canvaslms.com/t5/Canvas-Instructional-Designer/Importing-Rubrics-from-a-Spreadsheet/ba-p/264527)) is one of a collection of [Canvas/rubric userscripts](https://github.com/jamesjonesmath/canvancement/tree/master/rubrics) included in the [canvancement "project"](https://github.com/jamesjonesmath/canvancement/)

## Canvas rubrics model

Collection of criterion - one per row - containing

- _Description_ and _Long description_
- a sequence of ratings

Each rating is defined by

- Rating points/score 
- Rating title 
- Rating description

**Problem:** It doesn't appear to have support for for both rating descriptions and titles ([this message](https://community.canvaslms.com/t5/Canvas-Instructional-Designer/Importing-Rubrics-from-a-Spreadsheet/bc-p/264577/highlight/true#M921)). The solution is to manually enter it. Someone else has a [pull request](https://github.com/espertus/canvancement) to address this.




## How it works

1. Create rubric in Excel.
2. Copy to a textbox inside Canvas.
3. Auto convert to rubric


## Questions

1. Does it support ranges?