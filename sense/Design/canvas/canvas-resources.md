# Canvas resources

Collection point for misc Canvas resources - see also [[canvas-models]] and [[canvas-api]]

# to do   
 
 - [[canvas-api]]
- Does Canvas support cards? How?
- Canvas Commons and other Canvas communities?
- Canvas user scripts

## Misc resources

- [Rebuilding a Bb course in Canvas: What to expect](https://docs.google.com/document/d/1Jl-b9iH-_R4Rf1NZBHHv1wqGW4mKO5LxfaywiQ395qk/edit) - decent overview of the issues and advice
- [Lisa Lane's dozen tips for Canvas](https://wordpress.miracosta.edu/joyfulteaching/2017/07/22/lisas-dozen-tips-for-canvas/)
- [Canvas hacks](https://sites.google.com/asu.edu/sgsup-instructional-design/instructor-resources/webinars/canvas-hacks) - not very useful, specific to an institution

## Canvas resources

- [install Canvas](https://www.lmspulse.com/2021/how-to-install-canvas-lms/) and actual [instructions on using git repo](https://github.com/instructure/canvas-lms/wiki/Quick-Start#using-git)

### [Awesome CanvasLMS](https://community.canvaslms.com/t5/Community-Users/Awesome-CanvasLMS/ba-p/259722)

Curated list of Community and open source contributions. A fair number out of date/broken links

## Examples

Lists
- [Sample layouts from NorthWestern](https://canvas.northwestern.edu/courses/44486/pages/sample-canvas-course-layouts?module_item_id=520943)
- [Collection of home page designs](https://community.canvaslms.com/t5/Canvas-Instructional-Designer/Template-for-Canvas-Homepage/m-p/79770/highlight/true#M2523)

## Course design

- [How can I...structure my Canvas subject effectively?](https://lx.uts.edu.au/collections/examples-canvas-sites/resources/how-can-i-structure-my-canvas-subject-site-effectively/) - USyd page with some good content

### [Canvas course design overview](https://miracosta.instructure.com/courses/7500)

A focus on rebuilding a Bb course in Canvas, includes
- benefits of switching
- principles
- lessons learned

### [RMIT's designing a module in Canvas](https://sites.rmit.edu.au/sister/2020/06/29/designing-a-module-in-canvas/)

RMIT have specific "Canvas elements" and "uplift elements" to help structure and ensure consistent presentation. All apparently hidden behind the intranet.

> as a lecturer you only have a couple of points at which you can inject your personality and give your course an identity

Explicitly used to use modules. Push the use of "clear instructions can help students know what you expect of them and when"

## Canvas Hacks

- [5 Canvas hacks you can't live without](https://www.leveragingelearning.com/lelblog/5canvashacks) - awful overly promotional pages
- [CanvasHacks Demo Course](https://resources.instructure.com/courses/443) - demo course that introduces various approaches, from very simple to more advanced.  But not really coding level??
    - the navigation of this course sucks, not able to return to the top of a module, either on a page or all modules
- [Canvas LMS "Unpublish All" hack](https://daveeargle.com/2019/10/25/canvas-unpublish-hack/) - describes problem that Canvas doesn't all to unpublish all, explains using developer tools to work around it.

### [Hacking the Canvas User Interface](http://www.waol.org/javascript)

[Presentation](https://docs.google.com/presentation/d/1Y-BxHO2KZdFUkVmfePrfmVpZm4kMa3iTRz9adHyuKcM/edit#slide=id.p)

- Apparently Canvas is "built for the web", will the institution allow this
- **Let sub-accounts define additional includes** - will this be useful
- Basically an "how to" to include your own javascript with a little on "why"

### [Hacking Canvas](https://sites.udel.edu/bkinney/2013/11/22/hacking-canvas/)

>  because Canvas lets you mount custom css and javascript at the level of the account or sub-account. This gives administrators a remarkable amount of power, perhaps even too much.

### Python and Canvas

- [py3-canvaslms-api](https://github.com/dgrobani/py3-canvaslms-api) - python3 wrapper for canvas API with examples (e.g. generating an inventory of courses, find and replace text in Canvas pages)


## Canvas UX approach

UX design from University of Birmingham

- ux design - removing friction and confusion standing between customers and their end goals
- put users first 
- Did mention teachers/academics and students
- Mentioned a design system as an approach
    - digital assets??
- Consistency gets a mention

UX First approach in Canvas - still largely principles and Design
1. Remove choice paralysis
2. Guide and steward our users
- led to design of home page, using content audit and hierarchy exercises - fairly standard 
- leading to 4 or 5 links
    1. Enter module
    2. assessments
    3. overview
    4. Support/help
3. Reducing cognitive load
    - mention system 1 and system 2 (some very problematic explanations of this e.g. sides of the brain)
    - want students to be in system 1 (i.e. be easy) but then into system 2
4. Mental models
    - Aesthetics - i.e. match the brand of Uni of Birmingham
    - Functionality - how websites work
    - Halo effect - what the above is attempting to achieve. i.e if it's all positive, the halo will continue

Live example
- Consistent look and feel  
- usability practice 
- centralised design and control of pages
- wanted to **eradicate choice**
- Collection of pages with specific templates linked to functionality
   - **problem** it's all done in Canvas, so no external management or use.

Measuring success
- not a shelf product (i.e. taken on and off and used next time)
   - focus on the idea that it's an evolving product
- Using empathy mapping to measures
- regular online user interviews

But only at Part 1.  Need to measure.


## Introduction to the Canvas API

Why?
- reasons given are mostly administrative tasks - mostly not teaching
- allow you to do batch actions in Canvas
- "Click less and do more"

REquirement
- Canvas bearer token - from Canvas profile
- some level of admin access - **problem**
- some sort of language

- Everything has an id, which can be hard to find
- better ways to get ids 
    - run a report
    - use the API

- https://yourschool.instructure.com/doc/api/live - enter access token and then save token

## Embeddability - it's a word - reality it is

"Canvas cheerleaders" 

> Other LMSs/Systems are like an airport. Canvas is an all-inclusive cruise ship. -- Matt Miller
Not something that supports the idea of a VLE and goes against the whole purpose of the presentation

Two ways to add to the buffet 
- embeddable

RCE - embedding PDFs, images, audio, video

## Quick quality guide - to make the course sexy

Assessment, outcomes and accessibility
- which they proceed to read out objects

Home page

Syllaus


Module overviews

1. Course overview and introduction - "knock em dead"
    - course home page - relevant and useful
    - instructor biography
    - student self-introductions
    - syllabus 
3. Course technology
4. Learning support
5. accessibility
6. Usability








[//begin]: # "Autogenerated link references for markdown compatibility"
[canvas-models]: canvas-models "Canvas models"
[canvas-api]: canvas-api "canvas-api"
[canvas-api]: canvas-api "canvas-api"
[//end]: # "Autogenerated link references"