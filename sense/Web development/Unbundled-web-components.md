# Unbundled web components

## TODO

1. Can the magic script be used in a Blackboard page
1. Should Card/Content Interface be refactored to this approach?
2. How can this be done?

## PSU Context

HAXTheWeb aims to provide **H**eadless **A**uthoring e**X**perience. i.e. WYSIWYG editor built out of web componets. But HAX principles aim to make the web components able to stand without HAX.

## Bundling versus unbundling

Outlines [pros & cons of REACT type dev](https://dev.to/btopro/unbundled-web-components-part-2-bundling-vs-unbundled-movements-597i) compares this worldview with that of [A future without Webpack](https://www.pika.dev/blog/pika-web-a-future-without-webpack)

Adopting the latter, unbundling approach

## The Magic Script

[The magic script](https://github.com/elmsln/unbundled-webcomponents) does the work to allow

- ingesting of web components into any application
- eliminate bundling
- resolve platform capabilities on the front end
- only serve polyfills to those that need them



## Sources

Bryan Ollendyke, [Unbundled web components part 1: Context of WCs @ PSU](https://dev.to/btopro/part-1-how-penn-state-unbundles-web-components-for-cdn-deployments-20di) -- and the rest of the 7 part series