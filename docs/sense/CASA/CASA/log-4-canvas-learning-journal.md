---
backlinks:
- title: Canvas Learning Journal
  url: /memex/sense/CASA/CASA/canvas-learning-journal.html
tags:
- canvas-learning-journal
- casa
title: Log 4 - Canvas learning journal dev
type: note
---
## Requirement

Method to create and maintain a group set and groups for a course.

- if the group set does not exist, create it
- once the group set exists, check to see that all students have their own group created and they are allocated to the group

## Background

CanvasAPI 

- [course object](https://canvasapi.readthedocs.io/en/stable/course-ref.html?highlight=group) provides a `create_group_category` method wrapping around the [Canvas API call](https://canvas.instructure.com/doc/api/group_categories.html#method.group_categories.create). But can't create a single person group
- [GroupCategory object](https://canvasapi.readthedocs.io/en/stable/group-ref.html#groupcategory) includes ability to

  -  create a group - wrapping [Canvas API](https://canvas.instructure.com/doc/api/groups.html#method.groups.create)

- Group object has a create_membership method that works

## Questions



### How to add a single student to a group?


## Design

Required input

- group set name
- description for group