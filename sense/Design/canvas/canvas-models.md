# Canvas models

Attempt to distill the models that underpin Canvas

## Canvas limitations/concerns

- Rich Text Editor (RTE) configuration 
    - Currently removes all Javascript, non-standard HTML (e.g. web components) and "advanced" CSS (inline or not)
- Javascript can be added at admin/account level (i.e. IT department) - will they?
- Will we have access to the Canvas REST  and other APIs

## Misc notes

- Canvas does not have folders - uses Modules and Pages to organise content and assessments
- Rich Text Editor strips Javascript - ??workaround??

## [Thinking in Canvas](https://educational-innovation.sydney.edu.au/teaching@sydney/thinking-in-canvas/) Danny Liu's intro from USyd

- pages
    -  primary way to provide content 
    -  has version control
    -  permissions on pages is flexible e.g. students can be given edit access
    -  pages are used to embed all things, including Canvas features???

- modules - as the new organiser
    - replacement for folders
    - provide a linear pathway through a unit 
    - also provide the conditional release ability

## Modules

Intended to make organisation and navigation easier [source](https://sites.rmit.edu.au/sister/2020/06/29/designing-a-module-in-canvas/). A focus on creating flow.

## Templates

Canvas has the ["Ready-Made Template" suite](https://community.canvaslms.com/t5/Canvas-Instructional-Designer/2020-Course-Design-Essentials-Ready-Made-Template-Refresh/td-p/278763)
> help reduce stress load, encourage growth and help course creators design an engaging Canvas experience by turning a blank course shell into a fill-in-the-blank Canvas course.

- [Canvas style guides (deprecated?)](https://griffith.instructure.com/styleguide) being replaced by [some REACT thing](https://instructure.design/)
- [Three approaches to creating a Canvas template](https://www.unicon.net/insights/articles/three-approaches-to-creating-a-canvas-template)
- e.g. [USyd](https://lx.uts.edu.au/collections/examples-canvas-sites/resources/how-can-i-structure-my-canvas-subject-site-effectively/) provides templates for pages in Canvas
- [More detail on USyd templates](https://lx.uts.edu.au/blog/2020/07/21/get-moving-with-canvas-templates-and-shells/)



## Work arounds

- Apparently embedding web pages from a secure server is one workaround [source](https://wordpress.miracosta.edu/joyfulteaching/2017/07/22/lisas-dozen-tips-for-canvas/)
- [Embedding javascript](https://community.canvaslms.com/t5/Canvas-Question-Forum/How-do-I-add-javascript-in-the-HTML-editor/m-p/120884/highlight/true#M41789) - Laura's published workaround.  JS and call to JS in a page, included in an iframe

## User scripts

A [lot more on github](https://github.com/search?q=canvas+userscripts)

- [sukotsuchido/CanvasUserScripts](https://github.com/sukotsuchido/CanvasUserScripts) - collection of mostly teacher management type scripts (some recent updates)
    - [related post to Canvas forum](https://community.canvaslms.com/t5/Canvas-Developers-Group/Print-Canvas-Quizzes-UserScript/ba-p/243044)
- [UCBoulder](https://github.com/UCBoulder/canvas-userscripts) - rubrics, attendance, word count...
- [paulbui](https://github.com/paulbui/canvas-tweaks) - modules, gradebox, course shortcuts...
- [studentViewAnywhere](https://github.com/cesbrandt/canvas-javascript-studentViewAnywhere)
- [LJMUsoE](https://github.com/LJMUSoE/CanvasHacks) - includes a [page editor beautifier](https://github.com/LJMUSoE/CanvasHacks/tree/master/Editor) works with the HTML editor (not the RTE)
- [cotitto](https://github.com/cotitto/canvas-userscripts) - static course menu, add icons... 
- [matthewstrasiotto](https://github.com/matthewstrasiotto/canvas_userscripts) - project groups