---
title: "GraphQL basics"
type: note
tags: ["Web development", "GraphQL"]
---



## [Introduction to GraphQL](https://graphql.org/learn/)

GraphQL - an API query language.

| GraphQL Concept | Description |
| --- | --- |
| Schema | Defines the types and fields that can be queried |
| Fields | The properties/attributes of objects |
| Query | A request for data specifying fields `{ hero { name }}`. Fields can be of any type (e.g. strings, arrays, objects etc.) |
| Arguments | Fields (everyone) can be given parameters to modify the data returned `{ human(id: "1000") { name }}` with some ability to modify the data returned  |
| Aliases | Method to query the same field multiple times by defining a new "field" using standard field syntax.  Those aliases are then returned `hero1: hero(episode: NEWHOPE) { name } hero2: hero(episode: EMPIRE) { name }` |
| Fragments | Method to specify a set of fields that can be reused multiple times within a query.  |


