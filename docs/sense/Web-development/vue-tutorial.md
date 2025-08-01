﻿---
tags: web-development, javascript, vue
title: Vue Tutorial
type: note
---
## [Vue Tutorial](https://vuejs.org/tutorial/#step-1)

Not exhaustive - a taster.

Vue has two broad settings

1. API styles: options or composition (more Svelte like?)
2. modes: SFC (with a build step) and HTML (without)

Overview

- [Vue Tutorial](#vue-tutorial)
  - [SFCs and declarative rendering](#sfcs-and-declarative-rendering)
  - [Attribute bindings](#attribute-bindings)
  - [Event listeners](#event-listeners)
  - [Form bindings](#form-bindings)
  - [Conditional rendering](#conditional-rendering)
  - [List rendering](#list-rendering)
  - [Computer property](#computer-property)
  - [Lifecycle and template refs](#lifecycle-and-template-refs)
  - [Watchers](#watchers)
  - [Components](#components)
  - [Props and slots](#props-and-slots)
  - [Events](#events)

### SFCs and declarative rendering

A Vue SFC is reusable, self-contained block code code encapsulating HTML, CSS and JSS. Extends HTML to allow declarative description of HTML based on Javascript state

e.g.  

```vue
<script setup>
import { ref } from 'vue'

// component logic
// declare some reactive state here.
</script>

<template>
  <h1>Make me dynamic!</h1>
</template>
```

Variables made reactive with `ref` (turns into an "object" with a `value` attribute for use in Javascript, but not HTML) and `reactive` (for objects)

### Attribute bindings

Use `v-bind:<attribute-name>` (shortcut `:<attribute-name>`) to bind an attribute to a variable. i.e. `:id` matches the `id` attribute

```vue
<script setup>
import { ref } from 'vue'

const titleClass = ref('title')
</script>

<template>
  <h1 :class="titleClass">Make me red</h1> <!-- add dynamic class binding here -->
</template>

<style>
.title {
  color: red;
}
</style>
```

### Event listeners

Use `v-on:<event-name>` (shortcut `@<event-name>`) to bind an event to a function. i.e. `@click` matches the `click` event

### Form bindings

`v-on` and `v-bind` can be used to bind form inputs to variables

Also, `v-model` acts as a shortcut. Automatically synching form element value with the bound state. 

### Conditional rendering

Use `v-if` and `v-else` to conditionally render elements. These are attributes to HTML tags.

### List rendering

HTML list elements can use the `v-for` attribute to render a list of items. Including support for a `:key` attribute to specify an id for each list element to help vue.

### Computer property

A property (e.g. array of objects in a `v-for`) can be computed as a function and becomes reactive.

### Lifecycle and template refs

To access the DOM of a VUE component can use the `ref` attribute on an element. The matching variable is initialised as a null. It only becomes accessible after the component is mounted. 

`onMounted` is a lifecycle hook that can be used to access the DOM after the component is mounted.

### Watchers

Way to take action reactively to a change e.g. logging a number to the console when it changes.

### Components

Include Vue SFC files to use components as child components within another.

### Props and slots

Parent passes data to child components using props. The child must declare the props it accepts. Props are then passed within the HTML using the `v-bind` syntax

Data can be passed also using slots. With the child having fall back content

### Events

Child components can emit events using `emit` and the parent can listen using `@response` syntax.