﻿---
title: 004-exploring-oz-dev-log
---
Intent is to start generating markdown pages using Foam format for eventual inclusion in memex.

## To do

- [x] Develop `acLearningArea.py` class to start creating
  - [X] Handle learning areas without sub strands
  - [X] Implement better inheritance
  - [x] add ability to load multiple learning areas/files
- [x] Initial design of pages
- [ ] Refine memex pages
  - [X] add in accordions or similar of achievement standards
  - [X] exclude primary - do just high school
  - [ ] improve the individual content descriptions pages by
    - [X] add details of the subject, year level, strand/sub-strand that is related
    - [x] perhaps also add any related elaborations
    - [X] experiment adding in memex meta data (see below)
    - [X] use a toml heading
    
`---
title: <cd id>
type: "note"
tags: v9ac, <subject>, <year level>, <strand>, <sub-strand>
---



<subject> / <year-level> / <strand> / <sub-strand> / <cd id>
`

- [ ] Design of "view" to implement

## `australianCurriculum.py`

Intent is to have a Python class that 

- takes one or more learning area/subject RDF file from the Australian Curriculum, and
- breaks it up into a Python data structure
  - Ability to access each of the components of the curriculum

- `learningAreas` 

  dict keyed on learning area name, contains information about all the learning areas that have been added to this object (by parsing different RDF files)

- `subjects` 

  dict keyed on subject name, containing all info about the subjects

    - `subjectId`, `title`, `abbreviation`,`dateModified`
    - `yearLevels` 

      dict keyed on year level

      - `subjectId`, `title`, `abbreviation`,`dateModified`
      - `achievementStandard` 

        acAchivementStandard object
        - `subjectId`, `title`, `abbreviation`,`dateModified`
        - `components`

          dict keyed on AC id and values acAchivementStandardComponent

      - Strand

        - subStrand (optional)
      
      - `contentDescriptions` - dict keyed on content description code
        - `elaborations` - list of strings
        - `relatedContent` - list of strings
        - `description` - string

### structure


#### Other top level information

Maybe

- `contentDescriptions` top level dict with all content descriptions (across multiple learning areas/subjects) keyed by code

#### Learning/areas subjects

Dict `subjects` to contain objects of `acSubject` holding all information about the subjects in a learning area. In a learning area like mathematics which has no subjects, there's just the one subject.

Keyed on the name of the subject as per the Australian Curriculum

Each learning area contains

- ??? what subject level stuff goes here???
- `yearLevels` keyed on numeric/string year level foundation to year 10.
  - `levelDescription` string
  - `achievementStandard` dict keyed on
    - `text` string
    - `components` array of strings
  - `contentDescriptions` dict keyed on the content description code
    - `elaborations` - list/dict of strings
    - `relatedContent` - list/dict
  - ``



## Initial design

Page structure

- v9-australian-curriculum.md - "home" page

  Initially generate a list of learning areas/subjects (my subset). Learning areas and subjects will be used interchangeably. As the main unit for descriptions etc.

- _learning area_.md - all details for a given learning area/subject

  Organised by year level - preceeded by any learning area level information. Each year level contains the general year level information (not context descriptions) as accordions or similar. Then a table of content descriptions that are links to individual pages. Use of tooltips to contain the descriptions' summaries

  See also: v9-australian-curriculum.md

- _content description code_.md - all information for the content description

  Detail, elaborations, related content and my own notes.

  See also: _learning area_