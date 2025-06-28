---
backlinks:
- title: ER modelling and SQL
  url: /memex/sense/computing/learning-cs/er-modelling.html
tags:
- normal-forms
- database-design
- computing
title: Normal Forms
type: note
---
Codd initially developed three normal forms (1NF, 2NF, 3NF) to help with the design of relational databases.

## First normal forms (1NF)

Requires all data in tables be two dimensional and atomic. In other words, each cell in a table must contain a single value, and each row must be unique.

## Second normal forms (2NF)

Requires that all non-key attributes in a table be fully functionally dependent on the primary key. In other words, there should be no partial dependencies of any non-key attribute on the primary key.

For example, consider the following table:

```Employee ( name, job, salary, address)```

where name + job determines salary, but address only depends on name. Address depends only on part (name) of the key (name, job)