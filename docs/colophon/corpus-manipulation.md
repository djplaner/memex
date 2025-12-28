---
title: Corpus manipulation
type: note
tags:
- colophon
- computational-components
description: Documentation for methods used to retrieve and manipulate all or part of the corpus of bubbles.
---

`util/corpus.py` provides a Python class to retrieve all or some of the bubbles. Selection can be done using

- `type` only select bubbles that match the specific type
- `paths` only select bubbles that are in the specified paths (list of strings)
- `tags` only select bubbles that have at least one of the specified tags (list of strings)

## Examples

Retrieve all the `work-history` bubbles in the `sense/landscape-garden/work-files/` folder

```python
from corpus import corpus

workHistory = corpus( 
    type="work-history",
    paths=["sense/landscape-garden/work-files/"]
    )
```

Select all individual plants located in the `the-island` region 

```python
from corpus import corpus

plantsInTheIsland = corpus(
    type="single-plant",
    metadata={region:"the-island"}
    )
```
