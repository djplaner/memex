﻿---
backlinks:
- title: Python
  url: /sense/Python/python.html
title: streamlit
---
Getting started with [streamlit](https://streamlit.io/) an open-source app framework?

- [Documentation](https://docs.streamlit.io)

## First impressions

The "hello" demo gives a good impression of capabilities. -- could be useful

Focus more on data, rather than full on web development.

There is [free hosting](https://streamlit.io/cloud)

Has a growing list of components - from the community?

## Experimentation

Plan now is some quick experimentation using the [[exploring-australian-curriculum]] project

### Basic Concepts

[Main concepts](https://docs.streamlit.io/library/get-started/main-concepts)

And in summary - [App model](https://docs.streamlit.io/library/get-started/main-concepts#app-model)

1. Streamlit apps are Python scripts that run from top to bottom
2. Every time a user opens a browser tab pointing to your app, the script is re-executed
3. As the script executes, Streamlit draws its output live in a browser
4. Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast
5. Every time a user interacts with a widget, your script is re-executed and the output value of that widget is set to the new value during that run.
6. Streamlit apps can contain multiple pages, which are defined in separate .py files in a pages folder.

Provides [simplified ways to connect to data](https://docs.streamlit.io/library/advanced-features/connecting-to-data)


[//begin]: # "Autogenerated link references for markdown compatibility"
[exploring-australian-curriculum]: exploring-australian-curriculum "Exploring australian curriculum"
[//end]: # "Autogenerated link references"