---
title: Wood Duck observations
type: note
tags:
    - colophon
    - computational-components
description: Computational component to gather observations of animals, birds, insects, etc and weave and augment that information on this site.
---

!!! info "Current status"

    **11 Nov 2026** Initial version finally fully working. Still much to do to make it "nice"


??? note "Current To do"

    1. [ ] Update importObservations.py to add table of observations to plant-life-list (as initial test case)

        1. [x] Trying to save the updated file 
        
        2. [ ] Will need (probably) to add link data to linkDefs (currently working because I'm manually saving the life list files after the Python code updates - Foam is updating linkDefs)

            Probably add this displayObservationsIndex - generates the markdown, should generate the linkdefs as it has all the knowledge about where these files will be. Then just a question of adding to 
        
    3. [ ] Add some statistics before the tables on the life lists
            
    2. [x] Remove observation bubbles from graphing 

??? note "Further ideas"

    1. Individual observations can be updated both manually and automatically 

       - Automatically - as changes happen to host observations (e.g. iNaturalist observation has new data)
       - Manually - via an edit to the observation page through Foam

    2. Refinements to individual observation pages

       - [x] remove from title "iNaturalist|eBird observation"
       - [ ] provide an observation macro that provides the boilerplate intro text for observations, drawing from frontmatter
       - [ ] Add details about status of iNaturalist observations (e.g. needs ID, research grade, etc)
       - [ ] Support updating of iNaturalist observation pages (e.g. as status changes)

          - iNaturalist observations can be updated, need to check existing observation markdowns and update as necessary 
          - compare existing frontmatter with new and update as necessary from iNaturalist, don't update if frontmatter new
       - [x] change plant life list title to Plant life list - check other life lists
       - [ ] [[rhodosphaera]] - is a genus, not a species. Need to see if we can get specific - esp. with H&K's deep yellowwood

    3. Thinking about the nice to haves

       - [ ] iNaturalist pages that include confirmation counts
       - [x] Turn off life list generator and update documentation 
       - [ ] implement a `lifeListGallery` macro for different observations: extract relevant bubbles, extract images, construct gallery page content
       - [ ] Need to look into merging old plants that don't have observations, but have entries in the plants folder - adding observation macros to the bottom of each page
       - [ ] Ditto for the link to `individual-plants` and how [[individual-plants]] links with the species

           - individual plants arranged by zones
           - ways to link plant observations to zones
       - [ ] update species pages to include scientific name (in brackets)

    4. Replace/modify photo existing scripts to create observations with photos

       - [ ] `addBirdPhoto` 
       - [ ] `addPlantPhoto` 
       - [ ] Figure out whether to use the `add<Observation>` scripts to create observations for existing photos - or leave as is (probably leave)



## Purpose

With an interest in [[regeneration]] of the [[wood-duck-meadows]] ecosystem comes the desire to make and track various observations about the flora and fauna that inhabit the area. Plus there's the whole [[birding]] thing as well. There are some good tools for that (more details below). However, beyond simply making and recording these observations (what what amount to) external social networks I want to "own" and use some of those observations for my own purposes. I want to computationally [[gather-weave-augment|gather, weave, and augment]] this data into to my [[digital-garden]]. 

Currently, this includes the generation of

1. [life lists](https://en.wikipedia.org/wiki/Life_list) (e.g. [[bird-life-list]], [[plant-life-list]], and [[other-fauna-life-list]]) which list all the relevant species included in the observations and which point to...
2. Pages for each species (e.g. [[australasian-grebe]], [[brachychiton-rupestris]]) including background information and summaries of all the obervations.
3. Individual pages acting as a data container for each observation (e.g. [[S191595567|observation]] of an Australian Ibis), but not typically viewed directly (yet).

Future work

- refining the life lists;

    - Provide summary statistics of the various life lists (not just a long list)
    - Group lists into different categories (e.g. invasive, native, trees, shrubs etc)

- refining the species and observation pages

    - have both be (safely) updatable, both from the original observation data source and via local Foam edits
    - refine the observation data added to the page and how it is presented.
    - figure out if the observation pages should include backlinks to species page (and if they should appear in the network graph)
    - individual observation pages should use [[open-graph-per-page]]

## Usage

??? note "A reminder for self"

    Included here only to help me remember how if I get out of the habit.

1. Download latest observation data from external sources ([iNaturalist](https://www.inaturalist.org), [eBird](https://ebird.org)) into `~/memex_data`

    Yep, it's manual. A couple of CSV files: `ebirdData.csv` and `iNaturalist.csv`

2. Run the `importObservations` script within Memex

    `python util/generators/importObservations.py`

3. Edit and publish with Foam

    - Make additional edits using VsCode and Foam
    - Publish as normal

### The weaver scripts

The "weaver" scripts take the external data and weave into the Memex structure with two primary tasks

1. Convert each observation into a bubble (single markdown file) which links with the [[bubbles-as-objects]] idea.

    Observation bubbles are currently excluded from backlink generation and thus network graph.

2. Update "index" markdown files as required, including

    - individual species pages (e.g. [[acacia-salicina]]) grouping together all the observations of that species.
    - Life lists (e.g. [[bird-life-list]], [[plant-life-list]], and [[other-fauna-life-list]]) grouping together plants and observations thereof (maybe), but also providing additional information about that species.
    - regional lists (maybe) grouping together lists of plants 

## Conceptual Design

Built on [[bubbles-as-objects]] practice.

### Data entry and storage

- Individual observations are represented by individual markdown files with front-matter (see [data design](#data-design) below)
- Observations are generally stored in `docs/sense/observations` with sub-folders for different observation types e.g. `bird`, `insect`, `plant`, etc.
- Observation creation has two methods
  - Manual editing
  - Import from external data sources (e.g. eBird and iNaturalist) via "converters" to transform original data into markdown files
  - **TODO** Resolve if/how both manual editing and external data source import can co-exist (e.g. I want to add some annotation to an eBird observation) and/or an iNaturalist observation changes - how to update that?
- Each observation type has its own index (`docs/sense/Observations/bird-observations/bird-observations.md`) in a folder into which Markdown files are created for each observation.
    - **TODO** 
    
## Data design

!!! warning "Major re-design looming"

    What follows is very much an early exploration. Needs revisiting.

    - Include more source observation data in the front matter
    - Add open graph data to front matter
    - Consider replacing macros for observations with Python updating 


Each observation has a markdown file with following possible front matter fields that can be used for searching and filtering:

- type: observation

    All observations have this.
- subject: [ <wikiLink-of-subject>, ... ]
    Was originally `aka`. Specifies that this is an observation of a particular subject. e.g. a species of bird/plant, a individual plant, etc. 
- observation-type: <established observation type> 
    e.g. bird, insect, mammal, plant, fungi, etc
- And misc others as required
    - plant-type: [ native, exotic, weed, tree, shrub, groundcover, climber, aquatic, etc ] - only for plant observations
  - region: <wood-duck-meadows-region> (as appropriate)

Enabling macros like

```markdown
\{\{ observations( subject: "ficus-obliqua") \}\}
\{\{ observationsIndex( observation-type: 'plant') \}\}
\{\{ observations(region:'gatton-creek-frontage', observation-type: 'bird') \}\}
```

Real life requirements

- [[bird-life-list]] 

    Display a list of all the bird observations I've made ` \{\{ observationsIndex( observation-type: 'bird') \}\} `

    Perhaps the `observation-type` not only controls which observations are included, but also the display format?

- Display content of all bird observations of Black Swans

    ` \{\{ observations( subject: 'black-swan') \}\} ` 

- Display all list of trees that have been observed

    ` \{\{ observationsIndex( observation-type: 'plant', plant-type: 'tree') \}\} `

- Display list of all observations of ficus-obliqua

    ` \{\{ observationsIndex( subject: 'ficus-obliqua') \}\} `





## eBird importer

### [[life-list-generator]]

Existing practice 

- Retrieves data from eBird CSV export
- Makes some modifications to that data
- Checks to see if there's (a) photo(s) matching an observation in a given folder
    - Photos are added by `addBirdPhoto` script  
- Generates a 
  - life list and life list gallery as markdown files
  - individual bird page if there are photos for that bird species

### New practice

- ebird csv file is stored outside the memex project
- bird observations are stored as individual markdown files in `docs/sense/observations/bird-observations/`
  - Each eBird observation is a separate markdown observation file
    - metadata includes most of the eBird fields
    - content (by default) includes some boiler plate text
    - existing observation files are not updated - meaning user can manually add observations
    - if there are photos these are included in the page (as per existing practice)
- a new `ebirdToObservations.py` script is created to convert the eBird CSV file into individual observation markdown files
- a new `iNaturalistToObservations.py` script is created to convert iNaturalist data into individual observation markdown files
    - use the img URLs included in iNaturalist data
- [[life-list-generator]] is modified to 
    - work more explicitly as a [[computational-components]] - probably as macros
    - retrieving the `type: observation` and `aka: bird` bubbles
    - life list and life list gallery become macros to be embedded in relevant pages





[//begin]: # "Autogenerated link references for markdown compatibility"
[regeneration]: ../sense/landscape-garden/regeneration "Bush regeneration (Wood duck meadows)"
[wood-duck-meadows]: ../sense/landscape-garden/wood-duck-meadows "Wood duck meadows"
[birding]: ../sense/birdwatching/birding "Birding"
[gather-weave-augment|gather, weave, and augment]: ../sense/CASA/gwa/gather-weave-augment "Gather, Weave, Augment"
[digital-garden]: ../sense/computing/digital-garden "Digital Garden"
[bird-life-list]: ../sense/Observations/bird-life-list "Bird life list"
[plant-life-list]: ../sense/Observations/plant-life-list "Plant life list"
[other-fauna-life-list]: ../sense/Observations/other-fauna-life-list "Other-Fauna life list"
[australasian-grebe]: ../sense/birdwatching/bird-species/australasian-grebe "Australasian Grebe"
[brachychiton-rupestris]: ../sense/landscape-garden/plants/brachychiton-rupestris "Brachychiton rupestris (Queensland Bottle Tree)"
[S191595567|observation]: ../sense/Observations/bird-observations/australianIbis/S191595567 "Australian Ibis (Threskiornis molucca) - 2024-03-21"
[open-graph-per-page]: open-graph-per-page "Open graph per page"
[bubbles-as-objects]: bubbles-as-objects "Bubbles as objects"
[acacia-salicina]: ../sense/landscape-garden/plants/acacia-salicina "Willow Acacia"
[life-list-generator]: life-list-generator "Life list generator"
[computational-components]: computational-components "Computational components"
[//end]: # "Autogenerated link references"