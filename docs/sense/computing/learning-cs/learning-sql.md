---
tags:
- sql
- computing
title: Learning SQL
type: note
---
## Parts of SQL

| Part | Description |
|------|-------------|
| Data-definition language (DDL) | Commands for defining relation schemas, deleting relations, and modifying relation schemas |
| Data-manipulation language (DML) | Ability to query, insert into, delete from, and modify tuples in the database |
| Integrity | Specifying integrity constraints on data, updates are not allowed to violate these constraints |
| View definition | DDL commands for defining views |
| Transaction control | Commands for beginning, committing, and aborting transactions |

## Query types

Sources from [advanced SQL](https://15445.courses.cs.cmu.edu/fall2019/notes/02-advancedsql.pdf)

- aggregates COUNT, AVG etc

    Input is a bag of tuples conversion (via SELECT) to a single scalar value

- String operations - LIKE, || (concatention)

    Manipulate strings and be used anywhere in a statement

- Output redirection - INTO

    Redirect output from the terminal into a table

- Output control - ORDER BY, LIMIT, OFFSET

    Impose an order on a bag of tuples

- Nested queries - ALL, ANY, IN, EXISTS

    Invoke queries inside other queries. Inner query is able to access the attributes from the outer query

- Window functions ???

## Set operations

SQL provides operators equivalent to mathematical set operations. These appear to be used to join together two select statements using a process equivalent to the set operation. 

```sql
(select course_id from section where semester = 'Fall' and year= 2017) 
union 
(select course_id from section where semester = 'Spring' and year= 2018);
```

- _union_, 

    Find tuples that belong in either set. Duplicates are removed. Unless using _union all_

- _intersection_, and 

    Find tuples that belong in both sets. Duplicates are removed. Unless using _intersect all_

- _except_.

    Find tuples that belong in the first set but not the second. Duplicates are removed. Unless using _except all_

## Subqueries

Nest a **select-from-where** expression inside another

Common uses

### set membership 

Finding the intersection of two sets of tuples by using the **IN** operator and a nested subquery

### make set comparisons

Comparing value(s) from a set 

### determine set cardinality

## Views

A method of defining a "virtual" relation. This virtual relation is computed at execution time. A couple of methods:

- **with** clause 

    Named query creating the virtual relation is local to the query in which it is defined.

- **create view** statement

    Once created the view is available until explicitly dropped.

Creating a view requires a name and a query that computes the view. The name can used anywhere in a query where a relation name is expected.

## Integrity constraints

Ensure database changes do not result in a loss of consistency/integrity within the database. Essentially an arbitrary predicate applied to the database. Some predicates can be expensive to test.

Constraints applied in SQL during relation creation (`create table`) or after the fact (using `alter table`).

Types of constraints

- constraints on a single relation 
- not null constraint
- unique constraint - applied to a set of attributes
- check clause - comomonly used to ensure that attribute values satisfy some condition
- referential integrity
- Functional dependencies



## Resources

- [Awesome Database Learning](https://github.com/pingcap/awesome-database-learning?tab=readme-ov-file)

    Git repo with collaborative list of Database/SQL resources. More computer science and database engine implementation focused.

- [Sample databases](https://www.reddit.com/r/SQL/comments/s0tbnw/is_there_a_place_i_can_download_sample_databases/)

## References

Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). *Database system concepts* (Seventh edition). McGraw-Hill Education.