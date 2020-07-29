```toml
post_title='Pondering if/how Hax & web components fit in Blackboard'
layout="post"
published=false
id=
link=""
category="casa"
```

So look what I've done inside my [Blackboard Learn](https://en.wikipedia.org/wiki/Blackboard_Learn) sandpit site.

** replace with animated gif **

It probably doesn't look that exciting. A bit of HTML and a couple of images. Anyone could do that, right?

## It's not the what, it's the how

...And what the how makes possible

The core of this image is enabled by three different [web components](https://developer.mozilla.org/en-US/docs/Web/Web_Components)
1. [grid-place](https://www.npmjs.com/package/@lrnwebcomponents/grid-plate) - provides an easy way to display the three SpongeBob images in a grid
2. [meme-maker](https://www.npmjs.com/package/@lrnwebcomponents/meme-maker) - overlays the meme-like words (i.e. ARE, YOU, READY?) onto the SpongeBob images (no image manipulation required)
3. [hax-logo](https://www.npmjs.com/package/@lrnwebcomponents/hax-logo)
4. [type-writer](https://www.npmjs.com/package/@lrnwebcomponents/type-writer) - provides the "type-writer" animation of "Any tag you type here that is listed..." 

I use this functionality just like any other HTML tag. For example, if I wanted to add another SpongeBob "meme" (e.g. a __Hello World__ "meme") I would add the following "HTML" to my page.

```HTML
<p><meme-maker alt="happy dance GIF by SpongeBob SquarePants" 
  image-url="https://media0.giphy.com/media/nDSlfqf0gn5g4/giphy.gif" 
  top-text="Hello" bottom-text="World" 
  imageurl="https://media0.giphy.com/media/nDSlfqf0gn5g4/giphy.gif" 
  toptext="happy dance GIF by SpongeBob SquarePants"></p>
```
 
*** insert image sponge bob hello world ***

The **meme-maker** web component includes code that knows how to take the values I've placed in the **top-text** and **bottom-text** attributes and overlay them onto the image I've specified in **image-url**.  Change those attributes and I can create a new "meme".  For example, something a little more HAX.

***insert image of joker hello world***

## But wait, there's more

But I'm not limited to those four tags/web components. I can use any of the 560+ web components listed in [this JSON file](https://cdn.webcomponents.psu.edu/cdn/wc-registry.json). A list that includes: various types of charts; more layout components like the grid; players for various types of multimedia; a discussion form; rich text editor; and, much, much more.

Thanks to [the magic script](https://dev.to/btopro/uwc-part-3-the-magic-script-122a) I just include the right HTML tags and I'm away. 

**TODO** I do need to find out if and where the docs are for the various components. The NPM pages and git repo aren't doing it for a lowly end user.

## Broader implications: the NGDLE and the VLE 

Bryan's writing on the NGDLE https://psu.app.box.com/s/gk6013odcl3115j3ibfzudj3bqar059v

Link to the VLE

Something here about breaking out of the LMS...but what about my work with tweaks and links to the design principles of CASA and/or my ISDT

## How it works in Blackboard, currently


## Options for making this more widespread

