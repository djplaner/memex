---
name: "Javascript REST API Client"
type: "note"
tags: javascript, web-development, rest-api, client
---

See also: [[web-development]]

Figuring out good methods - and choosing one to use in [[canvas-collections]] - for making REST API requests from a web application.

Possible resources

- [API Client patterns](https://medium.com/js-dojo/api-client-patterns-every-front-end-developer-need-to-know-b0957e05b134) - medium article, may be useful
- [axios library tutorial](https://dev.to/bajcmartinez/how-to-master-http-requests-with-axios-1b3l) - seems a common alternative to other methods, including an abort controller

## Exploration 1 - API Client patterns (with Axios)

Couldn't use dummyapi so trying with jsonplaceholder. To work through [this tutorial](https://medium.com/js-dojo/api-client-patterns-every-front-end-developer-need-to-know-b0957e05b134)

Moved to use [MockAPI](https://app.wiremock.cloud/) as it provides more configuration options

### Pure asynchronous call

Making a single call to the API

Two versions 

1. A straight call from the tutorial

    - Returns almost straight away and continues with operation 
2. Using async/await

    - Works basically the same, but much cleaner

### Orchestration

Need to make several different calls in a sequence or parallel

The model here is to use the `await` keyword and just implement them sequentially

The default implementation is simply a sequence of `await` calls.  Any of which may fail raising issues of how to deal with progressive failure/progress.

## Exploration 2 - Moving to using Vue userscript dev

In [[design-of-vue-lj-casa-1]] stumbled across the "vite-plugin-monkey" project that generates vite projects for userscripts. A version is working with Canvas. Going to explore the use of that for developing/testing the REST API client. Idea being that Canvas is the immediate play ground.

### Vite-plugin-monkey doing simple Canvas REST API calls

Plan is to emulate some of the standard Canvas REST API calls used by [[canvas-collections]] as a first step to implementing [[vue-canvas-learning-journal]]

- What's a simple Canvas REST API call?
    requestCourseObject 
    - BASE_URL/api/v1/courses/:course_id
- Implement it

Done.  The pattern used was

- Update the `main.ts` of the vite-plugin-monkey project to include the REST API call
- After grabing the course ID and csrfToken use an async function and promise

```javascript
requestCourseObject(courseId, csrfToken).then((data) => {
  console.log(`Course Data: ${data}`);
  console.log(data);
  updateCourseData(data);
});
```

The function itself uses `await` on both the fetch and response

**TODO**

- [X] Is the CSRF token needed? - **no**
- [X] Can't update the Vue component from the `main.ts` as the component is not in the same scope. Need to call from within the Vue component
- [X] orchestration - the need to handle multiple sequential calls
- [ ] passing objects (reactively) between components
- [ ] using GraphQL to get Canvas data

### Test integration with Vue components

Two methods available - both work within library files used from within the component

1. Use an `async` function 

    The component has to use a `.then` to handle the promise and update the reactive variable. Also allows/requires the component to handle any errors. It does make what's happening more visible in the component.

2. Use a normal function, but pass in the reactive variable

    Creates an illusion of a synchronous call, but the function's internals operates asynchronously with promises internal.  But these aren't functions. 

Currently learning toward using the `async` function approach

### Orchestration

The need to make numerous calls in sequence. The sample userscript is now doing this.

The API client patterns work

### Passing objects reactively

Issue here is that the parent component gets the Canvas data, but which child components will make use of. That use needs to be able to reactively change.  Child -> Parent -> Child.

Questions 

- How to have changes made in child auto update the parent?

    - One approach is to use `v-model` on a component but that has specific constraints. The child must bind the value attribute of a native input element to the prop and use @input to emit
- How changes made in parent can be passed and used in the child? 

    e.g. Canvas API data retrieved in parent and passed to child.  But parent eventually changes that content when the API returns, which needs to modify any copies of the data.

From [[vue-components-props]] the idea is to create a global singleton.  For Canvas work that might be

- CanvasCourse object 
- Plus specific objects for each major focus e.g. Group Set, Group, Modules etc. Perhaps matching the Canvas API endpoints

#### Method used

Singleton created in a separate file.

```javascript
let canvasCourse: canvasAPICourse = reactive(new canvasAPICourse());

export default function getCanvasCourse(): any {
    if (canvasCourse.id === -1) {
        canvasCourse.parseCurrentURL();
        canvasCourse.retrieveCourseObject();
    }
    return canvasCourse;
}
```

Included into any component that needs it.

```javascript
import getCanvasCourse from '../lib/canvasAPICourse';
const canvasCourse = getCanvasCourse();
```

and then used reactively in the template

```html
 <p>Name: \{\{ .name \}\} </p>

  <ul>
    <li> Change course name: <input v-model="canvasCourse.name" /> </li>
    <li> course code: <input v-model="canvasCourse.courseObject.course_code" /> </li>
```

### Using GraphQL to get Canvas data

Starting with [[graphql-basics]] - done

### Refining and testing singeltons

- [ ] Multiple pages same browser 
- [ ] Check online for approaches (static?)

[//begin]: # "Autogenerated link references for markdown compatibility"
[web-development]: web-development "Web development"
[canvas-collections]: ../CASA/CASA/canvas-collections "Canvas Collections"
[//end]: # "Autogenerated link references"


[//begin]: # "Autogenerated link references for markdown compatibility"
[web-development]: web-development "Web development"
[canvas-collections]: ../CASA/CASA/canvas-collections "Canvas Collections"
[design-of-vue-lj-casa-1]: ../CASA/design-of-vue-lj-casa-1 "design-of-vue-lj-casa-1"
[vue-canvas-learning-journal]: ../CASA/vue-canvas-learning-journal "vue-canvas-learning-journal"
[vue-components-props]: vue-components-props "vue-components-props"
[graphql-basics]: graphql-basics "graphql-basics"
[//end]: # "Autogenerated link references"