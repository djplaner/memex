```toml
post_title='Visualising and pruning my Memex'
layout="post"
published=false
id=17918
link="https://djon.es/blog/2020/08/09/visualising-and-pruning-my-memex/"
category="memex"
img_base_url="https://djplaner.github.io/memex/share/blog/"
```

> ### Update - now with automated memex links
> In writing the following I stumbled across the idea that writing blog posts in Foam would enable the merging of content from Memex and blog posts. I then discovered it didn't work out of the box. More work was needed. But the nature of the technology involved meant that it wasn't that hard and is now complete.
>  You'll see links below followed by the spider web emoji (🕸️), those are links to my Memex.
> Meaning I this bit of bricolage can be linked to my Memex's page on [[bricolage]]. It's this type of capability that might address the [[reusability-paradox]] in digital learning technology, but more on that soon. 

Just [over a month ago](https://djon.es/blog/2020/07/06/designing-a-personal-memex-with-foam/) I started exploring the use of [Foam](https://foambubble.github.io/foam/) as my next attempt at developing a Personal Knowledge Management process. This has evolved into using Foam to curate [my personal "Memex"](https://djplaner.github.io/memex/) and (amongst other things) [populating it with](https://djon.es/blog/2020/07/07/getting-started-with-memex/) notes from my experiments with [Smallest Federated Wiki](https://en.wikipedia.org/wiki/Smallest_Federated_Wiki) and [Wikity](https://hapgood.us/2015/12/09/introducing-wikity/).

Foam has only been under development for just over a month and not surprisingly this brings with a few rough edges. Rough edges are the quickly being sanded down by a combination of the rapidly growing Foam community, the nature of the technologies underpinning Foam, and increasing knowledge on my part. Foam is quickly becoming core to my practice e.g. I'm writing this blog post in Foam ([here's the Foam/Memex version](https://djplaner.github.io/memex/share/blog/visualising-and-pruning-my-memex) of the post). 

The animated GIF below illustrates the utility of Foam. It shows me using [Foam's graph visualisation](https://foambubble.github.io/foam/graph-visualisation) feature to 
1. View the network of connections between the notes I've placed into Memex.
2. Identify an outlier note that isn't connected to anything (the first blog post I wrote in Foam/memex).
3. Click on the graph node to view the content of the associated file.
4. Figure out how that file should be connected.
6. Add in a appropriate connection to the note.
7. See the graph visualisation change to represent the new connection.

![Visualising and pruning my memex](gifs/Pruning%20my%20memex.gif)

## Further reflections 

### Breaking down categories

From the visualisation, I've also been able to make some observations reflect on my PKM process. For example, the network shows my use of Seek > Sense > Share as an initial organising metaphor limits connections. Strongly reinforced by the fact that the blog posts I've written have yet to connect back to the other notes in memex (e.g. those connected to [[sense]]). Given [Foam's link auto-completion feature](https://foambubble.github.io/foam/link-formatting-and-autocompletion) this is actually quite easy to do. e.g. [[seek]] > [[sense]] > [[share]]

Or at least I thought. It doesn't. More on this below.

Illustrating my IT nerdish tendency to be categorising notes as I place them into memex. Starting with seek/sense/share and flowing from there. Even though I've argued against hierarchical (tree-like) structures (e.g. [[set-mindset]]). I've still not yet fully grasped the advantage of [associative ontologies to hierarchical taxonomies](https://notes.andymatuschak.org/%C2%A7Note-writing_systems?stackedNotes=z29hLZHiVt7W2uss2uMpSZquAX5T6vaeSF6Cy)

Foam's ability to produce a public "secondbrain" on github pages (e.g. [memex](https://djplaner.github.io/memex/)) further breaks down the [original conceptions of seek > sense > share](https://jarche.com/2014/02/the-seek-sense-share-framework/). Rather than [[share]] being the focus for "exchanging resources, ideas, and experiences with our networks" this is happening with [[seek]] and [[share]] as well

### Mindtools, concept maps and learning

All of which appears to be a perfect example of the graph visualisation of Memex providing me with a concept map. A concept map that allows me to reflect on my own thinking (as captured in Memex) and subquently learn and change my practice. An example of Jonassen's (1996) idea of mindtools. Digital technologies that enable representation of what is known and using that representation to think about what is known.

### An important technical difference (affordance) between Foam, Smallest Federated Wiki and Wikity

All of what is happening in the GIF is occuring within [Visual Studio Code](https://code.visualstudio.com/) Microsoft's open source code editor. It's VSCode's open architecture and its [marketplace of extensions](https://marketplace.visualstudio.com/VSCode) that enable Foam's development and functionality. For example, it's [the Markdown links extension](https://marketplace.visualstudio.com/items?itemName=tchayen.markdown-links) that provides the functionality to visualise the graph and use it to navigate through the notes. It's not something that the Foam community had to develop.

In addition, while I am not a fan of [Markdown](https://en.wikipedia.org/wiki/Markdown) it does provide a very good interoperability platform. For example, the *Markdown* links extension enabling the visualisation. Hence there being [Python module for markdown](https://python-markdown.github.io/) that will convert markdown to HTML. Allowing me to convert [this Markdown file in memex](https://djplaner.github.io/memex/share/blog/visualising-and-pruning-my-memex) into [this blog post](https://djon.es/blog/2020/08/09/visualising-and-pruning-my-memex/).

As mentioned above I've experimented with [Smallest Federated Wiki](https://en.wikipedia.org/wiki/Smallest_Federated_Wiki) and [Wikity](https://hapgood.us/2015/12/09/introducing-wikity/). These are related but also different approaches to Foam. There are many differences in functionality (e.g. Foam doesn't support federation) and technical platforms (e.g. Wikity is a Wordpress plugin). But for me there appears to be a more important difference.

Foam appears more inherently more protean. More protean with how the tool itself is built. More protean in terms of how the content within it can be manipulated. Subsequently, more protean in how it can be integrated into the ad hoc assemblage of technology and practices that is my PKM process. Hence it appears more useful and it becoming (slowly) more integrated into and transforming my practice.

Though *appears* is the important word in the previous paragraph. YMMV. The protean nature of Foam is an affordance that arises from the combination of the technology, who I am, and my environment/assemblage. If you've not done much web development and through that developed knowledge of markdown, github and other technologies...YMMV.

### The cost of protean flexibility

The protean nature comes at a cost. The different tools being cobbled together here have different expectations. Differing expectations that clash. e.g. Foam's [link autocompletion](https://foambubble.github.io/foam/link-formatting-and-autocompletion) works a little differently than a normal markdown link. Differently enough that the Python markdown converter doesn't know how to handle it.  Hence the broken [[seek]] type links above.

Can it be fixed? Not a question I can answer now. 

## References

Jonassen, D. H. (1996). Computers in the Classroom: Mindtools for Critical Thinking. Merrill.


[//begin]: # "Autogenerated link references for markdown compatibility"
[bricolage]: ../../sense/bricolage "Bricolage"
[reusability-paradox]: ../../sense/Bricolage/reusability-paradox "Reusability Paradox"
[sense]: ../../sense/sense "Sense"
[seek]: ../../seek/seek "Seek"
[share]: ../share "Share"
[set-mindset]: ../../sense/Bricolage/set-mindset "SET Mindset"
[//end]: # "Autogenerated link references"