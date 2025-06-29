---
backlinks:
- title: Exploring australian curriculum
  url: /sense/Python/exploring-australian-curriculum.html
title: '# 001 - Exploring Australian Curriculum - Dev log'
---
## 001 - Exploring Australian Curriculum - Dev log



## Cleaning data to sqlite-utils and Datasette

Following the [cleaning data tutorial](https://datasette.io/tutorials/clean-data) from DataSette to convert the Excel spreadsheet provided into a database. The spreadsheet contains multiple sheets. 

| Sheet/table | Description |
| --- | --- |
| CD Elb-table | Includes the details on the content descriptors - the core data|
| CD CCP tagging | Link content descriptors to cross-curriculum priorities |
| CD GC tagging | Link content descriptors to general capabilities  |
| AS-table | The achievement standards |
| Copyright table | Copyright information, including note that [Oz Curriculum is released](https://www.australiancurriculum.edu.au/copyright-and-terms-of-use/) under Creative Commons|

!!! note "VSCode - network of tools helpful"

    With the CSV files added to the repo, I was able to use VSCode to view the files. The plugins integrated into VSCode are helpful. The assemblage of tools being helpful, but not immediately available to others. 

### sqlite-utils to create database

To create initial version of the database

```sh 
sqlite-utils insert oz_curriculum.db content_descriptors \
  "../data/F-10 CD Elb-Table 1.csv" --csv -d
```

All the fields of the CSV become TEXT columns. `sqlite-utils` can be used to query and examine the table, but time to use it in Datasette. 

sqlite-utils also offers ways to transform the data and the database.

<figure markdown>
[![](https://djon.es/assets/memex/sense/Python/exploring-oz-curriculum/../images/dataSetteOzCurr.png)](https://djon.es/assets/memex/sense/Python/exploring-oz-curriculum/../images/dataSetteOzCurr.png)
<figcaption>Initial Datasette visualisation of Australian Curriculum (click to see larger)</figcaption>
</figure>

## Datasette and immediate exploration

Datasette automatically identifies facets through which to examine the data through the lens of Learning Area, Pathway, Sequence, level, Topic, Depth Study, and Elective.

For example, learning area helps identify the 9 learning areas in the data and the number of rows for each. Each of these learning areas (e.g. Mathematics) can be drilled down. For example, drilling down on Mathematics and Datasette breaks down the 447 rows into year levels - year 7 having the most with 51!

| Learning area | # rows |
| --- | --- |
| Languages 12,612 |
|    Humanities and Social Sciences 1,513 |
|    English | 788 |
|    Science | 698 |
|    The Arts | 684 |
|    Technologies | 468 |
|    Mathematics | 447 |
|    Health and Physical Education | 426 |
|    Work Studies | 175 |

Datasette plugins add other visualisation options - e.g. map location data.

## sqlite-utils for tidying up the database

Exploration reveals some questions, more detail in the data and its structure

### Should the content descriptors table be split further? 

Initially, I thought I wouldn't do this, but when I tried to make CdCode the primary key it failed, because...

Use Datasettes ability to run custom SQL and identify that some CdCodes are appear in multiple rows.  Yes, because some content descriptors have multiple elaborations ([ACADAM001](https://australiancurriculum.edu.au/f-10-curriculum/the-arts/dance/?&capability=ignore&priority=ignore&year=12719&elaborations=true&cd=ACADAM001&searchTerm=ACADAM001#dimension-content))

!!! warning "The data appears to be v8.4 - not 9"

    Sadly, the Excel file (based on the content descriptor codes) is for the v8.4, not v9.

Ended up suggesting a need for a fair bit of splitting.  Leading to [a shell script](https://github.com/djplaner/exploring-australian-curriculum/blob/main/datasette/generate.sh) to automate the process of combining (perhaps inefficiently) multiple `sqlite-utils` commands to produce a more correct database with the following schema.

```SQL
CREATE TABLE "content_descriptors" (
   [id] INTEGER,
   [CdCode] TEXT PRIMARY KEY,
   [ContentDesc] TEXT
);
CREATE TABLE "elaborations" (
   [CdCode] TEXT REFERENCES [content_descriptors]([CdCode]),
   [Elaboration] TEXT
);
CREATE TABLE "learning_areas" (
   [LearningArea] TEXT,
   [Subject] TEXT,
   [Pathway] TEXT,
   [Sequence] TEXT,
   [Level] TEXT,
   [Strand] TEXT,
   [Substrand] TEXT,
   [Topic] TEXT,
   [Depth Study] TEXT,
   [Elective] TEXT,
   [CdCode] TEXT REFERENCES [content_descriptors]([CdCode])
);
CREATE TABLE "achievement_standards" (
   [LearningArea] TEXT,
   [Subject] TEXT,
   [Pathway] TEXT,
   [Sequence] TEXT,
   [Level] TEXT,
   [AchStd] TEXT
);
CREATE TABLE "general_capabilities" (
   [LearningArea] TEXT,
   [Subject] TEXT,
   [Pathway] TEXT,
   [Sequence] TEXT,
   [Level] TEXT,
   [Strand] TEXT,
   [Substrand] TEXT,
   [CdCode] TEXT REFERENCES [content_descriptors]([CdCode]),
   [ContentDesc] TEXT,
   [GC] TEXT,
   [Element] TEXT,
   [Subelement] TEXT
);
CREATE TABLE "cross_curriculum_priorities" (
   [LearningArea] TEXT,
   [Subject] TEXT,
   [Pathway] TEXT,
   [Sequence] TEXT,
   [Level] TEXT,
   [Strand] TEXT,
   [Substrand] TEXT,
   [CdCode] TEXT REFERENCES [content_descriptors]([CdCode]),
   [ContentDesc] TEXT
   [CCP] TEXT
);
```

## Datasette and sharing

There is a [JSON API](https://docs.datasette.io/en/stable/json_api.html) built into Datasette. Once deployed you could make calls.  Appears to be table based.

There is a [graphql plugin](https://datasette.io/plugins/datasette-graphql)...nice.  Install the plugin via pip, restart datasette and the interface is modified to include option to use GraphiQL to interact with

And there are various options for [publishing](https://docs.datasette.io/en/stable/publish.html) and [deploying](https://docs.datasette.io/en/stable/deploying.html) and [DataSette cloud](https://datasette.substack.com/p/datasette-cloud-and-the-datasette) is designed to make that easier.