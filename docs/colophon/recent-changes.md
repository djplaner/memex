---
title: Recent changes
type: computational-component
tags: 
    - colophon
    - computational-component
---

Recent changes defines a macro "function" `recentChanges` that takes the number of recent changes to display as a parameter. For example, using the macro `recentChanges(10)` appropriately will display a table of the 10 most recent changes in the published page.

Implemented using the [`mkdocs-macros-plugin`](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) for MkDocs.

## How

Include the macro anywhere in a Markdown file using the standard [`mkdocs-macros-plugin`](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) syntax. For example, the following (which is used on [the memex home page](../index.md))

```markdown
{{ '{{ recentChanges(5) }}' }}
```

Will produce the following table when the macro is expanded by the [[computational-components]] as the site is published.

{{ recentChanges(5) }}

## Implementation

Uses the Python [`GitPython`](https://gitpython.readthedocs.io/en/stable/) library to query git repo for most recent commits. Converts that data structure into a markdown table. See the [macros.py source file](https://github.com/djplaner/memex/blob/master/util/macros.py) for the implementation.


[//begin]: # "Autogenerated link references for markdown compatibility"
[computational-components]: computational-components "Computational components"
[//end]: # "Autogenerated link references"