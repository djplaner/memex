---
backlinks:
- title: Exploring Oz Curriculum - Dev log 2
  url: /memex/sense/Python/exploring-oz-curriculum/002-exploring-oz-dev-log.html
tags: rdf, python, exploring-oz-curriculum
title: RDF Basics
type: note
---
Resources

- [W3C RDF Primer](https://www.w3.org/TR/rdf-primer/)
- [SPARQL OceanInfo tutorial](https://book.oceaninfohub.org/users/query.html)

## Basics

RDF 

- at a general level - can be used to represent information about things that can be identified on the web - even if not on the web.
- intended to be used by applications, rather than people

RDF's basic concept is that _things_ are

- identified using URIs; and
- described using simple properties and property values.

Data takes the form of a graph of nodes and arcs. For example, the following statements becomes the figure below

> "there is a Person identified by http://www.w3.org/People/EM/contact#me, whose name is Eric Miller, whose email address is em@w3.org, and whose title is Dr." 

Where nodes are URIs the args (properties) are also URIs and values of properties are different types of "nodes" containing values

![](https://djon.es/assets/memex/sense/Python/exploring-oz-curriculum/images/simpleRDFGraph.png)

### The RDF model

A statement consists of three parts

- _subject_ what the RDF statement is about
- _predicate_ - identifies/labels the property of the subject the statement is talking about
- _object_ - the value of the property

_subject_ and _object_ form nodes. The _predicate_ is the arc joining the nodes.

_subject_ and _predicate_ typically URIs. _object_ can be a URI or a literal value (e.g. string, number, date)

Statements can be represented visually as graphs, or as triples (subject, predicate, object)