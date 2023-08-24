# Pathway planner

Docs for the development of the pathway-planner component.

pathway-planner
1. Choose major/minor 
   1. *select-major-minor*
2. Courses Done
   1. *select-major-minor*
   2. *credit-point-progress*
   3. *program-structure*
      1. List of *course-progress*
3. Courses to do
   1. *select-major-minor*
   2. *credit-point-progress*
   3. *program-paths*

## Data structures

Required data structures
- Years, Majors and Minors
- Program structure for each major/minor/year
  - Including course categories
- Course code, names, credit point, labels and offerings

### TaffyDb

Simple object-based "database-like" retrieval.

Some early planning
- select major
  - majors({year:*default_year*}) .. major to populate list of majors
  - majors({year:*default_year*,major:*selected_major*}) ... minor to get minor
- "credit points" - would select from program structure (in memory) those completed courses and count credit points/counts
- taffDb has a method .store() which writes to localStorage 
- program structure 
  - Originally loaded from Javascript without user fields (or perhaps these are programmaticlly added the first time up -)
  - can add new fields as we go

### Implementation

1. Source Data
2. Get it checked
3. Put it in code

### program-structure

Could be a collection of three arrays. Year 1, 2, and 3.  Each array containing objects representing a course. 

## Current status/plans


### Implement pathway-planner custom element to encapsulate app

Use a [router](https://www.kevinsimper.dk/posts/single-page-app-with-webcomponents-and-router) between the different states, including local storage


## Look for other components for elements

- [heavy-navbar](https://github.com/HeavyLightStudios/heavy-navbar)

## Use generic HTML and CSS for styling. 

[how to](https://www.thinktecture.com/en/web-components/native-web-components-without-framework/#how-to-style-your-web-component)

## To do

- [X] Create repo - code/griffith/2020/pathway-planner
- [X] Implement hard wired initial version

## Resources

- [build wc with lit-html](https://dev.to/bennypowers/lets-build-web-components-part-5-litelement-906) - decent detailed overview/process
- [open-wc codelabs #2](https://open-wc.org/codelabs/basics/lit-html.html?index=/codelabs/#2)
- [open-wc code examples](https://open-wc.org/developing/code-examples.html) - good collection of short examples
- [Building componets (Google)](https://developers.google.com/web/fundamentals/web-components/)
- [All things lit-html](https://github.com/web-padawan/awesome-lit-html)

### Interface decisions and information

[Material Components Web (mdc)](https://github.com/material-components/material-components-web) - help developers implement Material design.

[Material Design Web Components (mwc)](https://github.com/material-components/material-components-web-components) - are a wrapper around MDC to create custom elements (web components)

- install component via npm
- import into web component (all css applied)

## Implement look and feel within shadow development

Web components often use the shadow DOM (by default?). Meaning it's hidden away. External CSS doesn't impact it?



## Insights

[Reactive property changes](https://open-wc.org/codelabs/basics/lit-html.html?index=/codelabs/#7) use properties and immutable approaches - create new arrays etc

[setting property syntax](https://open-wc.org/codelabs/basics/lit-html.html?index=/codelabs/#9)

## Related

- [[web-development]]

[//begin]: # "Autogenerated link references for markdown compatibility"
[web-development]: ../web-development "Web development"
[//end]: # "Autogenerated link references"