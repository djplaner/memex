---
backlinks:
- title: Blog posts
  url: /memex/share/blog/blog-posts.html
title: 'Canvas Collection: Purpose, How, and Functionality'
---
```toml
post_title='Canvas Collections: why, how and what'
layout="post"
published=true
id=18226
link="https://djon.es/blog/2022/07/03/orchestrating-entangled-relations-to-break-the-iron-triangle-examples-from-a-lms-migration"
category="casa"
img_base_url="https://djplaner.github.io/memex/share/blog/2022/"
```


## Why?

[Canvas Collections](https://github.com/djplaner/canvas-collections#canvas-collections) is an open source exploration into enhancing [the Canvas Modules view](https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-are-Modules/ta-p/6) to improve the learning and teaching experience. Canvas Collections' purpose is to reduce the time and knowledge required to develop and maintain a Canvas course site that has a visible design intent, information architecture, and unique visual identity. By this Canvas Collections aims to aid in the creation of course sites that improve student wayfinding, efficacy, and experience. 

## <a id="_Toc108002814"></a><a id="_Toc108003738"></a>How

Canvas Collections leverages the inherent flexibility and generativity provided by Canvas's design and [API](https://canvas.instructure.com/doc/api/) and insights gained from existing practice both in the Canvas Community and at Griffith University (Jones, 2019). This is used to provide functionality long requested by the Canvas Community to address acknowledged limitations (visually unappealing and poor findability) with the Canvas Modules view. Canvas Collections is designed to meet Griffith's principles for the selection and deployment of educational technological solutions (see Table 1).

<a id="_Ref107907527"></a>Table - Canvas Collections evaluated against Griffith principles for ed tech selection and deployment

<table><tbody><tr><td><p><strong>Requirement</strong></p></td><td><p><strong>Canvas Collections</strong></p></td></tr><tr><td><p>Scalability</p></td><td><p>Canvas Collections can be installed in two ways</p><ol><li>Institutionally; or,<br/>Using <a href="https://community.canvaslms.com/t5/Admin-Guide/How-do-I-upload-custom-JavaScript-and-CSS-files-to-an-account/ta-p/253">standard Canvas and institutional practice</a> (e.g. Griffith course site template) installed via the Canvas theme editor. It has been tested with Griffith's dev Canvas server.</li><li>Individually.<br/>As a <a href="https://en.wikipedia.org/wiki/Userscript">userscript</a> in an individual's web browser and only seen by them. Typically for exploration or <a href="https://wp.wpi.edu/atc-ttl/2019/05/08/update-create-a-canvas-custom-home-page-with-buttons/">creating a visual home page</a>. </li></ol></td></tr><tr><td><p>Failsafe</p></td><td><p>Canvas Collections modifies the standard Canvas Module interface. If Canvas Collections is unavailable, no change is made and the the standard Canvas Module view is shown.</p><p>When used individually to create a visual home page Canvas Collections is used by teaching staff to generate HTML that is pasted into a Canvas page. After this, Canvas Collections is not used.</p></td></tr><tr><td><p>Designed for academic use</p></td><td><p>Canvas Collections is explicitly designed to be used by academic staff without requiring an educational designer. It is an adaptation and enhancement to the Card Interface, <a href="https://djon.es/blog/2021/03/12/reflecting-on-the-spread-of-the-card-interface-for-blackboard-learn/#the-spread-card-interface-usage-jan-march-2021">widely used</a> with minimal support by hundreds of Griffith courses and at other institutions across the world.</p></td></tr><tr><td><p>Opt-in</p></td><td><p>Whether Canvas Collections is used institutionally or individually, the teaching team for a course must opt-in to use Canvas Collections and can, at any time, opt-out.</p></td></tr></tbody></table>

#### <a id="_Toc108002815"></a><a id="_Toc108003739"></a>Design and implementation

Canvas Collections is written in Javascript and re-arranges the vanilla Canvas Modules view by adding support for three additional abstractions, these are:

1.   Collections � a way to group modules aligned with specific design intent.
2.   Representations � select from different visual representations and user experiences (e.g. Figure 7) for each collection.
3.   Meta-data � associate additional contextual and learning design oriented meta-data with each module for inclusion in representations to support design intent.

#### <a id="_Toc108002816"></a><a id="_Toc108003740"></a>Data storage

The additional metadata and configuration information managed by Canvas Collections is stored as a JSON data structure in either a specially named page or file within the Canvas course. This means that the Canvas Collection data uses exactly the same methods and services as every other Canvas resource (e.g. learning content). 

For Canvas Collections to work, the permissions on the page/file must be set to: teaching staff can read/write, and students can read.

## <a id="_Toc108002817"></a><a id="_Toc108003741"></a>Canvas Collections: Examples of Usage

The following examples of usage of Canvas Collections are drawn from a current Griffith University T2 Pilot course: [5254LAW, Canadian Administrative Law](https://lms.griffith.edu.au/courses/7757/pages/canvas-collections-configuration).

__NOTE:__ As Canvas Collections is a work-in-progress what follows is illustrative of current, limited functionality. There is significant scope and plans for re-design and expansion. A key success factor of the pre-cursor Card Interface was the ability to evolve functionality in response to need.

After explaining the spectrum usage scenarios for Canvas Collections, the rest of this document uses screenshots to demonstrate the Canvas Collections experience for staff and students.

### <a id="_Toc108002818"></a><a id="_Toc108003742"></a>Possible Canvas Collections Usage Scenarios

Canvas Collections can currently be used in three different ways. Table 2 summarises these three methods and maps out the subsequent usage scenarios for staff and students. Regardless of method, students only experience Canvas Collection if staff configure it for the Canvas course.

<a id="_Ref107983920"></a>Table - Mapping Canvas Collection Usage Scenarios

<table><tbody><tr><td><p>Method</p></td><td><p>Description</p></td><td><p>Staff</p></td><td><p>Students</p></td></tr><tr><td><p>Institutional</p></td><td><p>Institution installs Canvas Collections as part of their Canvas instance</p></td><td><p>Can choose to turn on Canvas Collections (Figure 2) and then configure Canvas Collections for the course. Then Canvas Collections will modify the Modules view.</p></td><td><p>If configured for course by teaching staff, Canvas Collections will modify the Modules view for all students (e.g. Figure 7)</p></td></tr><tr><td><p>Individual</p></td><td><p>Individual user installs Canvas Collections as a userscript in a particular web browser they use. </p></td><td><p>Opt-in by installing userscript and then choose to turn Canvas Collections on. Then configure Canvas Collections (e.g. Figure 4 and Figure 5) for the course. The userscript will then modify the Modules view for any user who has installed it.</p></td><td><p>If Canvas Collections configured for course by teaching staff, students who install the userscript will see a modified Modules view.</p></td></tr><tr><td><p>Offline (Claytons)</p></td><td><p>Using either institutional or individual methods, teacher uses Canvas Collection to generate HTML (e.g. Figure 5) which is then pasted into a Canvas page (e.g. Figure 6, Figure 10, Figure 11).</p></td><td><p>As per either institutional or individual methods teacher opts-in and then chooses if and how to paste HTML into the Canvas page.</p></td><td><p>If teaching staff paste Canvas Collections generated HTML into a Canvas page, all students will see it (Canvas Collections is not involved)</p></td></tr></tbody></table>

### <a id="_Toc108002819"></a><a id="_Toc108003743"></a>Teacher Experience with Canvas Collections

Whether using the institutional or individual method the teacher experience with Canvas Collections is the same.

#### <a id="_Toc108002820"></a><a id="_Toc108003744"></a>Canvas Collections is off by default

Canvas Collections is initially turned off for all course sites. When turned off, Canvas Collections will make one small change to the teacher view of the Modules page. It adds an off/on switch, circled in red in Figure 1. This "switch" also includes links to a Tier 0 resource on Canvas Collections.

When turned off, Canvas Collections makes no change to the student view.

<a id="_Ref107902793"></a>Figure 1 - Canvas Collections - turned off

#### <a id="_Toc108002821"></a><a id="_Toc108003745"></a>Turn Canvas Collections on 

Clicking on the switch circled in red in Figure 1 turns Canvas Collections on and modifies the Modules view. These changes are based on the existing Canvas Collections configuration. At a minimum, the teacher view will be modified to add the Canvas Collections configuration interface. If there is an existing Canvas Collections configuration, the teacher view will include visible evidence of Canvas Collections. 

The configuration interface viewed by teaching staff consists of three parts, in summary (see below for more detail):

1.   A course level configuration interface.  
    The Canvas on switch (as shown in Figure 1) provides access to the course level configuration interface which can be expanded (Figure 3).
2.   The actual Canvas Collections interface.  
    This mirrors the Canvas Collections interface viewed by students (Figure 2).
3.   A per module configuration interface.  
    Each Canvas module has a configuration interface to modify how it is represented (Figure 4).

Figure 2 shows the result of turning on Canvas Collections in a configured course. The configuration interfaces are explained in more detail in following sections.

The "actual" Canvas Collections interface includes the collections navigation bar allowing navigation between different collections, and the current collection's representation. Different representations can be chosen for different collections, and the representation changed at any time.

<a id="_Ref107903728"></a>Figure 2 - Canvas Collections - turned on (existing configuration)

#### <a id="_Toc108002822"></a><a id="_Toc108003746"></a>Configure Canvas Collections for the course 

There are configuration choices � the number and naming of collections; how each collection is represented; the order of collections etc. � that apply at the entire course level. These are configured via the expanded Canvas Collections on/off button. Figure 3 shows the expanded version of the on/off button, including the current configuration interface.

<a id="_Ref107906144"></a>Figure 3 - Course level configuration of Canvas Collection

#### <a id="_Toc108002823"></a><a id="_Toc108003747"></a>Configure Canvas Collections for an individual module

Scrolling further down the Modules page (underneath the current collection's representation) will show (in Teacher view) a list of the modules that belong to the current collection. In Teacher view, Canvas Collections will add a configuration interface for each module. Figure 4 illustrates this configuration interface (circled in red) in both expanded and collapsed modes. This interface is used to modify the module specific Canvas Collections metadata for each module. More detail on per module configuration options below.

<a id="_Ref107905766"></a>Figure 4 - Module specific Collections' configuration

#### <a id="_Toc108002824"></a><a id="_Toc108003748"></a>Create an "offline" (Claytons) Canvas Collection

Common advice within the broader Canvas Community is that creating a visual home page is a good way to improve the usability of a Canvas course site. Such advice is typically accompanied by advice on how to [manually create such a page](https://wp.wpi.edu/atc-ttl/2019/05/08/update-create-a-canvas-custom-home-page-with-buttons/). Canvas Collections is designed to help automate this process. However, if Canvas Collections is not installed institutionally students cannot (easily) benefit from Canvas Collections. The "offline" (aka Claytons) use of Canvas Collections is intended to help this situation by enabling teaching staff to:

1.   Copy HTML for a single collection into their browser's clipboard (Figure 5).
2.   Paste that HTML into a Canvas page that can be viewed without Canvas Collections installed (Figure 6).

<a id="_Ref107986752"></a>Figure - Using "Collections 2 Clipboard" button to copy collection HTML to the clipboard

The "offline" version of the Canvas Collection HTML (Figure 6) is stand-alone. It does not rely on Canvas Collections at all. It emulates much of the same functionality, but in a constrained way due to the limitations of the Canvas Rich Content Editor (RCE)

<a id="_Ref107986845"></a>Figure - An "offline" version of the Course Content collection as the course landing page

### <a id="_Toc108002825"></a><a id="_Toc108003749"></a>Student Experience with Canvas Collections

Students only experience the visual representations generated by Canvas Collections (online or offline). 

#### <a id="_Toc108002826"></a><a id="_Toc108003750"></a>Student experience with Canvas Collections: online method

The Canvas Collections online method modifies the Modules view for the course. The modifications provide a way for students to navigate between collections of modules and access specific modules. Figure 7 shows the online Canvas Collections view for the course 5254LAW. The annotations in Figure 7 point out the main components of the Canvas Collections student experience. Table 3 describes each of these components. Figure 8 and Figure 9 show the student view for the Assessment and Teaching Staff collections visible in Figure 7.

<a id="_Ref107988615"></a>Figure - Canvas Modules student view modified by Canvas Collections (online): Annotated

<a id="_Ref108000650"></a>Table - Description of Canvas Collections student experience components

<table><tbody><tr><td colspan="2"><p>Component</p></td><td><p>Description</p></td></tr><tr><td><p>Collections Navigation Bar</p></td><td colspan="2"><p>A list of all collections. A module belongs to one collection. Clicking on different collections shows the representation of that collection (Cards in this case) and a list of all modules within that collection.</p></td></tr><tr><td><p>Current collection</p></td><td colspan="2"><p>The currently visible collection is highlighted in the navigation bar.</p></td></tr><tr><td><p>Module Date</p></td><td colspan="2"><p>Optionally, each module can have a date or date range associated with it (e.g. to indicate due date for an assignment, a starting date for a module etc). Dates can be specific or they can be specified using Griffith study period weeks. e.g. Figure 7 includes cards with dates specified as "Week 1". This is automatically converted to July 18 based on the University calendar and the Griffith course code within the Canvas course id.</p></td></tr><tr><td><p>Module Image</p></td><td colspan="2"><p>Each module can have an associated image specified by a URL</p></td></tr><tr><td><p>Module Name</p></td><td colspan="2"><p>The title of the card matches the name of the Canvas Module</p></td></tr><tr><td><p>Module label and number</p></td><td colspan="2"><p>Optionally, a module can have a label identifying the "type" of module (common examples include workshop, module, assignment) and a number.</p></td></tr><tr><td><p>Module Description</p></td><td colspan="2"><p>Each module can have an additional collection of HTML typically used to summarise the purpose and engage student activity.</p></td></tr><tr><td><p>Coming Soon</p></td><td colspan="2"><p>Optionally, unpublished modules (normally not visible to students) can be designated as coming soon. Allowing the students to see the overall planned structure, but not access the content.</p></td></tr><tr><td><p>Completion Progress</p></td><td colspan="2"><p>A visual summary of the student's progress against any requirements that have been configured for the module.</p></td></tr></tbody></table>

<table><tbody><tr><td><p></p><p><a id="_Ref108000968"></a>Figure  - Assessment collection representation</p></td><td><p></p><p><a id="_Ref108000975"></a>Figure  - Teaching staff collection representation</p></td></tr></tbody></table>

#### <a id="_Toc108002827"></a><a id="_Toc108003751"></a>Student experience with Canvas Collections: offline method

The Canvas Collections offline method provides the ability for students to view individual Canvas pages that contain the representation of a single collection. These pages provide access to the corresponding Canvas modules. The Canvas Collections offline method semi-automates the widely recommended [manual process of creating a visual home page](https://wp.wpi.edu/atc-ttl/2019/05/08/update-create-a-canvas-custom-home-page-with-buttons/).

The offline method is currently being used in T2 pilot courses as part of the course site template. Figure 6 shows a landing page integrated with the course site template for 5254LAW. This landing page contains a representation of the _Course Content_ collection shown in Figure 7. Similarly, Figure 10 and Figure 11 show offline versions of the _Assessment_ (Figure 8) and _Teaching Staff_ (Figure 9) collections.

<table><tbody><tr><td><p></p><p><a id="_Ref108001634"></a>Figure  - Offline representation of the 5254LAW assessment collection</p></td><td><p></p><p><a id="_Ref108001643"></a>Figure  - Offline representation of the 5254LAW Teaching Staff collection</p></td></tr></tbody></table>

## <a id="_Toc108002828"></a><a id="_Toc108003752"></a>References

<div class="apa"><p>Jones, D. (2019). Exploring knowledge reuse in design for digital learning: Tweaks, H5P, CASA and constructive templates. In Y. W. Chew, K. M. Chan, &amp; A. Alphonso (Eds.), <em>Personalised Learning. Diverse Goals. One Heart. ASCILITE 2019</em> (pp. 139�148). https://djon.es/blog/2019/08/08/exploring-knowledge-reuse-in-design-for-digital-learning-tweaks-h5p-constructive-templates-and-casa/</p></div>