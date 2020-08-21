# My First LitElement Web Component

Description and reflections of create a very simple web component using [LitElement's live tutorial](https://lit-element.polymer-project.org/try)

## Impressive first impression

First reactions, impressive. Produces a VSCode looking code editor and matching "browser" output all in the browser window. Though it's a bit of pain that it doesn't have the vim bindings.

![](Web%20development/litElementLiveEditor.png)

## Creating a component

In summary,

A component lives in its own JS file, with three main sections

1. Import various "includes"
2. Define a class for the component (the code)
3. Register the element with the browser

## Properties

Looks like basics of contemporary Javascript OO.

1. Properties implemented as a hash/object
2. Declare a getter for properties
   ```Javascript
    static get properties() {
   return { message: { type: String } };
 }```
3. Initialise the property with a constructor
    ```Javascript
    constructor() {
   super();
   this.message = 'Hello world! From my-element';
 }```
 4. Use it as an attribute


