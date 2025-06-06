---
categories:
- colophon
date: 2025-05-23 14:17:25.821396+00:00
next:
  text: Home
  url: /blog/index.html
previous:
  text: What now?
  url: /blog/2025/01/12/what-now
publishedPath: /2025/05/23/a-new-day
template: blog-post.html
title: A new day
type: post
---
## Introduction

A new day dawns. The [planned technology migration](https://djon.es/blog/2025/01/12/what-now/) of my blog is complete.  Goodbye to "big tech" Wordpress and its (IMHO) horrid authoring environment and bloated performance. 

Hello to a markdown based static site generated through Python and numerous open source tools. The blog is reasonably functionally complete, but tinkering will continue. After all, enabling tinkering was a key motivation for the migration. 

This post celebrates that move and:

1. [Introduces the new technology stack](#the-new-technology-stack);
2. [Shares the migration method](#the-migration-method);
3. [Outlines the new authoring process](#the-authoring-process);
4. [Reflects on the process](#reflections); and,
5. Lists some initial ideas for [next steps](#next-steps).

!!! note "Linking the stream and the garden"

    Many of the links below demonstrate a linkage between my ["garden and the stream"](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/). Another key motivation for the migration.
    
    The published version of this blog post is part of my _stream_. A serialisation of more complete ideas I'm explicitly sharing with others. 

    Some of the links below point to some of the formative and still under construction ideas/work that underpin this published post. These formative ideas exist in my [memex site](https://djon.es/memex). My _garden_ of ideas. The space where I iteratively develop, refine and share ideas in ways that are tentative and interconnected. A space where I document experiments and slowly grapple with ideas. Experiments like this migration.

## The new technology stack

First, a quick overview of the technology stack for the new blog.

### Content and authoring

The new blog starts as a collection of markdown files saved in a git repository (currently [hosted on GitHub](https://github.com/djplaner/blog)). There markdown files are created/edited using VSCode leveraging the [Foam extension](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode). 

Foam is an assemblage of existing VSCode extensions configured to provide [Roam Research](https://roamresearch.com) like functionality. I've been using Foam for Memex and authoring Wordpress blog posts since 2020. The aim is to continue/improve this process for the new blog - see below for more details.

### Publishing the blog

The markdown files are converted into a collection of HTML files using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). A template (extension) of the Python based [MkDocs static site generator (SSG)](https://www.mkdocs.org). MkDocs reads the markdown files and generates a collection of HTML files. The HTML files are added to another git repository hosted on my personal web server. From which you've retrieved what you're reading.

Material for MkDocs also runs additional Python scripts I've written to generate additional HTML (inserted into existing HTML files) and new HTML files. The [archive](/blog/archives/index.html) and [category](/blog/category/index.html) pages are generated by these Python scripts. A Python script also generates the "blog stats" table on the [About page](/blog/about.html). "Blog stats" is implemented as a macro that can be inserted into any page. For example, here it is on this page.

{{ blogStats() }}

This use of Python is an expansion of the [[computational-components]] approach I've started using in Memex. 

### Serving the blog

As the published blog is just HTML, it is served by the standard web server (Apache) used by my hosting service and consumer by your browser (and numerous crawlers etc).

## The migration method

The task of [[convert-wordpress-into-memex|converting my Wordpress blog to Markdown]] worked through the following steps:

1. [[export-wordpress-to-markdown|Export]] the contents of the Wordpress blog to markdown.

    - Use Wordpress' in-built export functionality to download an XML file with all of the blog's content. 
    - Use ["Wordpress export to Markdown"](https://github.com/lonekorean/wordpress-export-to-markdown) to generate a structured collection of markdown files.

2. [[modify-markdown-files|Modify the markdown files]] to mirror the old blog structure, fix outdated content, and create blog functionality. 

    In order to retain the same URLs for individual blog posts, the markdown files produced by step 1 had to be placed into a different folder structure. The content of the markdown files was modified to tidy up and correct outdated content (e.g. Slideshare links I now longer use, outdated links etc) and to add blog functionality to MkDocs (e.g. category pages, archives, RSS feeds, comments/pingbacks).
    
3. [[modify-interface|Tweak the default SSG template]] to better suit the design of my new blog.

    Mostly involving tweaking [Material for MkDocs](https://squidfunk.github.io/mkdocs) HTML and CSS templates.

4. [[comparing-wordpress-to-memex|Compare and refine]] the new blog against the old and expectations.

    Analyse the speed and accessibility of the new blog HTML to compare with Wordpress. Confirming it is faster, but not without some issues to address.

5. Replace Wordpress.

    Modify the the web server configuration to move the Wordpress blog to its [new location](https://djon.es/wordpress-blog) and replace it with [the new blog](https://djon.es/blog/).

## The authoring process

!!! failure "Too big for a merged garden and stream"

    I had hoped to merge my stream (blog) and garden ([memex](https://djon.es/memex/)) into a single Foam workspace. Sadly the size of the combined content exceeded the limitations of Foam's wikilink autocompletion. Waiting tens of seconds for link suggestions was not conducive to a smooth writing experience. 

    Hence the stream and garden exist in separate Foam workspaces.

Given that I wanted to continue my existing practice of [writing blog posts in my garden](http://djon.es/blog/2020/07/07/getting-started-with-memex/index.html#writing-blog-posts-in-memex), and Memex and the blog are in separate repositories I needed a script to "publish" a post from Memex to the blog. In essence keeping the process I've using since 2020 to "publish" posts from Memex to Wordpress. In the absence of Wordpress the new _pubish_ script also needed to add some blog functionality to the Memex markdown files. 

## Reflections

Overall, the migration has met my expectations. The blog is faster. The content is in a more interoperable format. The authoring process remains embedded in Memex. The linkages between the blog and Memex have improved. The MkDocs ecosystem seems to be a good foundation for extensibility and personal tinkering.

Hopefully that translates to a bit more writing.

Misc. other reflections follow.

### Everything old is new again - static sites

Moving away from Wordpress to static site generation using a scripting language generate nostalgia for my early days publishing on the web with [Webfuse](/blog/2010/03/10/webfuse-is-dead-long-live-webfuse/index.html). A bespoke "LMS" that formed much of my work in the late 1990s and early 2000s and was the basis of my [PhD](/blog/category/phd.html). Unlike other LMS, Webfuse generated static HTML for speed reasons. A very different approach to my recent, no longer active forays into Javascript frameworks and dynamic sites.

The nostalgia for the good old days may be one reason why I liked the return to static sites. However, another big factor has to be the ever-changing fluidity of the Javascript ecosystem. The Svelte projects I worked on a few years ago have become obsolete due (amongst other things) to changes in the Svelte ecosystem. Python and MkDocs aren't static, but they aren't running pell mell into the future either.

### All models (e.g. software) are wrong

Not that all is perfect, [all models are wrong](/blog/2015/08/28/all-models-are-wrong-but-some-are-useful-and-its-application-to-e-learning/index.html). As mentioned above, Foam has limitations on the number of documents. Material for MkDocs also has a similar limit (though much larger). MkDocs was designed to manage online documentation. Stretching it for blogs and Memex starts to reveal more of the mismatch between capability and need. For example, the blog isn't as responsive/fast as I'd like. A major part of that is how Material for MkDocs implements its search engine (via a large JSON file). 

There are other problems (e.g. I haven't yet been able to get the [URL for the Wordpress RSS feed](/blog/feed/) to point to the [new blog's feed](/blog/feed/feed.rss)). 

For now, I'm happier to live with this collection of _wrongness_, rather than the _wrongness_ of Wordpress. Largely because...

### Some assemblage required and enabled, fighting the reusability paradox

As the tag line for this blog says, some [[assemblage]] is always required. The migration and authoring sections above describe some of the assemblage required so far. The _wrongness_ is a pointer to some further required assemblage. My ability to engage in that assemblage has been better enabled by the migration. Foam and MkDocs are extensible open source projects in technologies I'm familiar with. Having my blog content in Markdown also enables this ongoing assemblage.

Which provides the opportunity to engage more directly with the [[reusability-paradox]]. The notion that the more generic a tool/resource (e.g. MkDocs, Wordpress) the less useful it will be for a specific purpose (e.g. my personal knowledge management). However, the ability to leverage interoperability and the extensibility of some tools means I can add some personal utility. At the cost of genericity.

### House of cards, Web of complexity

That personal utility also comes at the cost of complexity. The extensibility of the tools I'm using is not really just inherent in the tool. It's an affordance. A relationship between the tool and my background, knowledge, and context. If I weren't retired (time) with a background in scripting languages (knowledge) and engaging in PKM on the web (purpose), I wouldn't be able to do this.

## Next steps

The tinkering - assemblage - will continue. Some existing ideas follow. Suggestions welcome.

### Further reduce reliance on big tech

The migration has reduced my reliance on big tech, but not eliminated it. The git repositories for both this blog and Memex are hosted on GitHub. I'm editing this post in VSCode.

GitHub can be easily replaced to any other server (including self-hosted) supporting git. The only issue is likely to be the connection with the Foam project. Not a big issue.

Since Foam is a VSCode extension, replacing it could be significantly harder. However, the relationship between VSCode and [VSCodium](https://vscodium.com) means it could be quite straight forward.

The main challenge being the mundane nature of this type of change, versus something involving more coding.

### Comments and pingbacks

Interaction is a key argument for a blog. At the moment, the new blog has a record of past comments and pingbacks, but has not functionality to accept new comments and pingbacks. Enabling this is important.

Some possible approaches:

- Mastodon and ActivityPub

    An approach [Tim uses on some posts](https://heartsoulmachine.com./blog/2025/04-29-a-value-proposition-and-outcomes-focus/) is to ask for comments as replies to a [matching Mastodon toot](https://mastodon.social/@timklapdor/114420226599573017). It does seem somewhat limiting to require comments via a specific platform, but it is a good platform (and protocol). There appears to be [code and advice](https://cassidyjames.com/blog/fediverse-blog-comments-mastodon/) on how to do this. 

- [Gicus](https://giscus.app)

    Material for Mkdocs has [direct support for Gicuss](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/?h=comments#giscus-integration). An open source system built on top of GitHub discussions. Given my interest in moving away from big tech, increasingly my reliance on GitHub is a concern. Not to mention requiring commenters to have a GitHub account.

- [Another 6 alternatives](https://www.brianliddell.com/blog/six-comments-apps-for-personal-blogs)

    Another 6 alternatives, none of which seems to be a perfect fit.

In terms of ping(track)backs, need to think about both [sending](https://www.brianliddell.com/blog/six-comments-apps-for-personal-blogs) and receiving pingbacks.

### Statistics and analytics

Knowing more about the structure of the blog and its content (analytics) and what people are reading from the blog (logging) strike me as useful additions.

The `blogStats` macro shown above is a start on logging. [Jim Nielsen](https://blog.jim-nielsen.com/about/) has a nice collection of statistics that might be interesting to explore. In particular, the [internal links visualisation](https://blog.jim-nielsen.com/about/internal-links/) and tracking the most referenced internal links.

In the past, I've taken the easy route and relied either on Wordpress analytics or Google Analytics. Moving away from big tech suggests something like [these suggestions for small analytics](https://benhoyt.com/writings/the-small-web-is-beautiful/#small-analytics). Or, maybe I should just start analysing log files.

### Visual design

The visual design is functional (at best). Being prettier would be nice, especially if it was [combined with interesting functionality](https://www.joshwcomeau.com/about-josh/). But this is far into the future.


[//begin]: # "Autogenerated link references for markdown compatibility"
[computational-components]: ../../../colophon/computational-components "Computational components"
[convert-wordpress-into-memex|converting my Wordpress blog to Markdown]: ../../../colophon/convert-wordpress-into-memex "Convert Wordpress into Memex"
[export-wordpress-to-markdown|Export]: ../../../colophon/export-wordpress-to-markdown "Export Wordpress to Markdown"
[modify-markdown-files|Modify the markdown files]: ../../../colophon/modify-markdown-files "Modify Markdown files"
[modify-interface|Tweak the default SSG template]: ../../../colophon/modify-interface "Modify blog interface"
[comparing-wordpress-to-memex|Compare and refine]: ../../../colophon/comparing-wordpress-to-memex "Comparing Wordpress to Memex"
[assemblage]: ../../../sense/Distribution/assemblage "Assemblage"
[reusability-paradox]: ../../../sense/Bricolage/reusability-paradox "Reusability Paradox"
[//end]: # "Autogenerated link references"