--- 
title: "Dev log - 003: Exploring Oz Curriculum"
type: devLog
tags: python, v9ozCurriculum, curriculum
---

## Purpose

Basically try and get something useful out of the RDF version of version 9 of the Australian Curriculum.

Thoughts are

- [ ] Make sense of what is there

  - [ ] Using Neo4j
- [ ] Figure out the available Python methods for manipulating that data

    - [redflib-neo4j](https://github.com/neo4j-labs/rdflib-neo4j) - might be useful

- [ ] Figure out how it might be used 

  - [ ] With memex
  - [ ] For lesson planning etc

## ToC



## Neo4j

A Java implemented graph database (in the sense of nodes, edges). Has a limited Commuity (free) version. A [decent intro to Neo4j and graph databases](https://www.graphable.ai/software/what-is-neo4j-graph-database/), including a feature list for Neo4J which includes

- Cypher - an query language for graph databases
- native graph - as a labelled property graph
- Data browser
- ACID compliant
- REST API and Javascript access

### Local installation

Neo4j corporate site pushes you to the cloud, but there is [desktop version](https://neo4j.com/download/?gad_source=1). Requires contact details.

[How to import RDF into Neo4j](https://teepika-r-m.medium.com/how-to-import-rdf-data-into-neo4j-68f051a3cfd5)

- Install [Neosemantics plugin](https://neo4j.com/labs/neosemantics/4.1/introduction/) to enable use of RDF
    - Sadly that is looking [more difficult](https://community.neo4j.com/t/neosemantics-n10s-graph-app-problems-with-install/58816/2) than it might otherwise be
        - [Some suggestion](https://community.neo4j.com/t/problem-installing-neosemantics-on-neo4j-desktop/20825) that `APOC` plugin needs installing first

