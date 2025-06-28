---
backlinks:
- title: Learning Vue
  url: /memex/sense/Web-development/learning-vue.html
tags: web-development, javascript, vue
title: Vue components/props in depth
type: note
---
- [Vue components in depth props](https://vue-community.org/js/vue-js-components-in-depth-props.html)
- [State management](https://vuejs.org/guide/scaling-up/state-management.html)

## State management

Three possible approaches discussed

1. Lifting state to common ancestor and passing down as props

    Problematic in component trees with deep hierarchies ending up with [prop drilling](https://vuejs.org/guide/components/provide-inject.html#prop-drilling)

2. Using template refs and direct parent/child instances. 

    But also brittle and become unmaintainable

3. Extract shared state out of components and manage via a global singleton.

    Component tree becomes a big view with any component able to access state or trigger actions.

### Shared state

Vue's reactivity system is decoupled from the component model.

Use `reactive` to create a reactive object. Value and functions to modify.


## Components

> Components in Vue.js can be thought of as custom HTML elements that you can define and reuse throughout your application. They can have their own internal state, properties, and methods, and can communicate with other components using events and props.

| Component topic/part | Description |
| --- | --- |
| Props | Data passed from parent to child. Props are immutable, they cannot be modified by the child |
| Data | Internal state about the component. Can by modified |
| Computed Properties | Derived from component's state and cached. Re-evaluated when their dependencies change |
| Methods | Functions that can be called from the template or other methods.  |
| Lifecycle hooks | Methods called at specific stages of the component's lifecycle: e.g. mounted, updated, destroyed |
| Directives | Special attributes to attach behaviour to elements in the DOM, Vue provides built-in directives: v-if, v-for, v-bind and the ability to create custom directives |
| Event handling | The v-on directive enables Vue components to listen to user-generated events and trigger methods etc |
| Component communication | Ways for parent/child components to communicate: v-on and emit |
| Transitions and animation | Vue specific transitioning systems for when components are added, updated or removed |
| Slots | Method to accept arbitrary content from parent component |
| Mixins | Reusable code snippets that can be shared across multiple components|
| Render functions | method for defining a components template using Javascript, rather than HTML |
| Single file components | Recommended approach for defining components |
| Global vs local registration | Whether components are registered within a specific component or at the global/App level. Local is recommended |

## Props

Custom attributes defined on a component. Can be any Javascript data type.