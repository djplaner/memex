---
title: Announcing (finally) Canvas Collections
---
```toml
post_title='Announcing (finally) Canvas Collections'
layout="post"
published=false
id=18413
link="https://djon.es/blog/2023/08/18/announcing-finally-canvas-collections/"
category="casa"
img_base_url="https://djplaner.github.io/memex/share/blog/"
```



## Introduction 

Canvas Collections is an open source tool that helps to transform the Canvas modules index page by adding [structure](https://djplaner.github.io/canvas-collections/#structure), [visuals](https://djplaner.github.io/canvas-collections/#visuals), and [context](https://djplaner.github.io/canvas-collections/#context). Doing so helps improve the organisation, aesthetics, usability, and findability of a Canvas course. Improvements known to [enhance student self-efficacy, motivation, and retention](https://djplaner.github.io/canvas-collections/#why).

The following offers a summary of how and what you can do with Canvas Collections. See the [Canvas Collections' site for much more](https://djplaner.github.io/canvas-collections/).

## How do you use it?

Collections is most useful when [installed institutionally](https://djplaner.github.io/canvas-collections/getting-started/install/institutional/). But you need to be an administrator to do that. That might not be an option for you.

Collections can also be [installed individually](https://djplaner.github.io/canvas-collections/getting-started/install/individual/) (most useful for teachers or designers of Canvas course sites) in two steps:
1. Install the [Tampermonkey browser extension](https://tampermonkey.net/)
2. Install the [Canvas Collections userscript](https://github.com/djplaner/canvas-collections/raw/main/dist/canvas-collections.user.js). 

Once installed, you can:
1. [Check it is installed](https://djplaner.github.io/canvas-collections/getting-started/install/is-it-installed/).
2. [Configure Collections](https://djplaner.github.io/canvas-collections/configure/overview/) for your course.
3. [Navigate your course](https://djplaner.github.io/canvas-collections/navigate/navigate-options/) using Collections.

## What can you do with it?

### Start with vanilla Canvas modules

The following image is an example (vanilla) Canvas modules index page. Showing the standard linear structure and a visually limited interface with little contextual information of that page.  

From what you see here, can you identify the three driving questions behind the design of this course? 

<figure markdown>
<figcaption>Scrolling through a sample (vanilla) Canvas modules index page</figcaption>
<a href="https://github.com/djplaner/canvas-collections/blob/main/docs/assets/vanillaModules.gif"><img style="width:50%" alt="Scrolling through a Canvas modules index page. Showing 13 modules and all their items in one long linear scroll. Each module visualised with a 'windows-95' like folder with a list of items." src="https://github.com/djplaner/canvas-collections/raw/main/docs/assets/vanillaModules.gif" /></a>
</figure>

### Add live (dynamic) Canvas Collections

The following image is the same course as above. However, the Canvas Collections code is live and is dynamically modifying the Canvas modules index page to add

- Structure - modules have been allocated to four _collections_ with only the modules belonging to the currently selected collection visible at any one time.
- Visuals - each collection is using a different _representation_ (and also including content from a Canvas page) which allows direct navigation to a module.
- Context - additional contextual data (e.g. description, banner image/iframe, date etc.) is visible for each module. (What isn't shown is that this data can include [requirements completion](https://djplaner.github.io/canvas-collections/reference/conceptual-model/representations/griffith-cards/#progress-ring))

Can you identify the three driving questions behind the design of this course from this view?

<figure markdown>
<figcaption>Scrolling through the same module page but with Canvas Collections turned on</figcaption>
<a href="https://github.com/djplaner/canvas-collections/blob/main/docs/assets/withCanvasCollections.gif"><img width="50%" src="https://github.com/djplaner/canvas-collections/raw/main/docs/assets/withCanvasCollections.gif" alt="Canvas modules page configured with four collections (why, what, how, and questions & suggestions). Changing between different collections, showing only that collection's modules at any one time. Navigating directly to a module by clicking on its specific representation. Showing off the representations which include cards for each module. Cards with images/iframes, descriptions, dates, labels and other contextual data" /></a>
</figure>

### Create a Claytons (static) Canvas Collections page

Live Collections requires installing the Canvas Collections code (institutionally or individually). If installed individually, then you probably can't use live Collections with students.

As an alternative, you can use your individual installation of Collections to create a Canvas page that contains a static ([Claytons](https://australianfoodtimeline.com.au/claytons-enters-australian-vernacular/)) version of Canvas Collections. Echoing the common Canvas community practice of creating a visual home page for a Canvas course. The difference being that Collections does the design work for you.

The following demonstrates a Claytons Collections version of the live Collections above. Same (similar) collections, representations, and contextual data. However, all saved onto a Canvas page that is being used as the course home page.

(NOTE: Due to [limitations of the Canvas RCE](https://community.canvaslms.com/t5/Canvas-Resource-Documents/Canvas-HTML-Editor-Allowlist/ta-p/387066) at least one of the current representations shown does require external CSS to work.)

<figure markdown>
<figcaption>Using a Claytons Collections home page</figcaption>
<a href="https://github.com/djplaner/canvas-collections/blob/main/docs/assets/claytonsCollections.gif"><img width="50%" src="https://github.com/djplaner/canvas-collections/raw/main/docs/assets/claytonsCollections.gif" alt="Animation showing how a Canvas page has been updated to contain a sequence of tabs for each collection. Allowing the visitor to see different representations of Canvas modules (but not the modules themselves). Representations that are basically the same as live Canvas Collections. Clicking on the representation for a module will take you directly to that module.">
</figure>

### Modify Canvas Collections

Canvas Collections is explicitly designed to add more [generativity](https://djplaner.github.io/canvas-collections/#generativity). That is, to improve the capacity of the community ["to produce unprompted change driven by large, varied, and uncoordinated audiences"](https://en.wikipedia.org/wiki/Generative_systems). By making it simpler (though perhaps not simple) for others to make changes. [The rationale](https://djplaner.github.io/canvas-collections/about/rationale/) behind Canvas Collections is that generativity is a key enabler for providing [usable short arc design tools that scale](https://djplaner.github.io/canvas-collections/about/rationale/#usable-short-arc-design-tools-that-scale)

To achieve this Canvas Collections is:

1. [Distributed](https://github.com/djplaner/canvas-collections) under an [open source licence (GPLv3)](https://github.com/djplaner/canvas-collections/blob/main/LICENSE).
2. Written using [Svelte](https://svelte.dev/)
3. Designed with an architecture that (hopefully) allows simple additions.

## More information

The [Canvas Collections site](https://djplaner.github.io/canvas-collections/) provides more detail.

Enjoy.

David.