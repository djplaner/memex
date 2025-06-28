---
backlinks:
- title: CASA Gallery
  url: /memex/sense/CASA/casa-gallery.html
- title: Use of reveal.js for presentations
  url: /memex/sense/Teaching/Mathematics/use-of-revealjs-for-presentations.html
- title: 'MATH081C Unit 1, Lesson 1: 2024'
  url: /memex/sense/Teaching/Implementation/2024/MAT081C/mat081c-2024-u1l1.html
tags: casa, teaching, visibly-random-groups, complex-instruction
title: Random Group Allocator
type: note
---
Explorations to develop a web page based (Javascript) method for randomly allocating groups by 

- Copy and pasting a collection of student names;
- Setting group size; and 
- visibly displaying the group allocation.

[Repo complete](https://github.com/djplaner/GroupGenerator) and [deployed via GitHub Pages](https://djplaner.github.io/GroupGenerator/).

## [GroupGenerator](https://github.com/togarci/GroupGenerator)

Plan to adapt this one

- Translate to English
- Replace manual addition of names with text area

### Implementation details

- `addName` called on button press - to be removed
- `generateGroup` does the work
- `updateCurrentAllocation` - add a feature that shows a calculation of the number of groups as names are added

#### Add storage of group allocations

- Only store the current allocation - only one, not multiple
- Add "Save" button - on group allocation page
- Add "Load" button on initial page - but only if there is a saved allocation
    - On start, call `isSaveGroupAllocation` and change the display for the button