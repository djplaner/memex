---
backlinks:
- title: Blog posts
  url: /share/blog/blog-posts.html
title: 'Robotic Process Automation (RPA) in L&T in tertiary education: LMS migration
  examples'
---
```toml
post_title='"Robotic Process Automation" (RPA) in L&T in tertiary education: LMS migration examples'
layout="post"
published=false
id=??
link="https://djon.es/blog/??"
category="casa"
img_base_url="https://djplaner.github.io/memex/share/blog/"
```

# Introduction

Robotic Process Automation (RPA) is a billon dollar software and services market being actively leveraged by large organisations (including universities) to make administrative processes more efficient and effective. RPA is just one example of how traditional IT systems and development are not sufficient for contemporary digital transformation/innovation. Especially when it comes to an activity as diverse as learning and teaching. A problem which learning technologists, educational designers, and others involved in university L&T have been working around for years. This work has typically occurred in spite of institutionally approved processes. Work that is necessary not just because it works around inefficient or ineffective systems but because it is also seen as key to enabling the creative recombination of the technical and social components of contemporary digital infrastructures necessary for digital transformation (Leonardi, 2011; Yoo, 2013)

The following introduces RPA and explains why after years of expensive enterprise information systems it is required. RPA is then positioned within the broader idea of lightweight IT development. This is positioned within university L&T through an example of work we're doing as part of an LMS migration (Blackboard Learn to Canvas). Other examples from the Canvas community are then used to argue that within universities RPA and its like needs to broaden appropriately. Its formal organisational application needs to move appropriately beyond just administrative tasks. Its application in L&T needs to move appropriately beyond the "lone rangers" playing in the shadows toward becoming an integral part of how universities strategic approach to contemporary L&T. 

# Introducing Robotic Process Automation (RPA)

Robotic Process Automation (RPA) is a label applied to software that can emulate how humans interact with software. RPA software can click menu items and buttons, open windows, "type" in information, "read" other information, and make decisions about what to do next based on that data. RPA software can do most of what a human can do with other software - hence "robotic". Most RPA vendors also claim the magic ingredient of AI adding to the "robotic" flavour. RPA software supports the creation of "scripts" of direct the "robot's" activities. Scripts that can be repeated without human intervention as often as required - hence "process automation". If you're doing a software intensive task once, you probably don't need RPA. If you're performing the task 20+ times every Monday morning RPA can save time and hassle.

The Google Books Ngram viewer has ["robotic process automation" first appearing](https://books.google.com/ngrams/graph?content=robotic+process+automation&year_start=2010&year_end=2019&corpus=26&smoothing=3) in 2012. [A recent media release](https://www.globenewswire.com/news-release/2022/01/06/2362208/0/en/robotic-process-automation-market-to-hit-usd-23-9-bn-by-2030.html) estimates the 2021 RPA market size at $USD2.65 billion suggesting it will grow to $USD23.9 billion by 2030. 

Consulting companies have been [writing descriptions](https://www.ey.com/en_us/government-public-sector/how-universities-are-using-robotic-process-automation) of how universities can use RPA "across the student value chain". Universities have projects using RPA, e.g. the [University of Melbourne](https://www.automationanywhere.com/resources/customer-stories/university-of-melbourne), the [Australian National University](https://services.anu.edu.au/information-technology/software-systems/robotic-process-automation), [Griffith University](https://intranet.secure.griffith.edu.au/work/robotic-process-automation), and the [University of Auckland](https://www.uipath.com/resources/automation-case-studies/university-of-auckland). However, almost all visible/espoused use of RPA in universities appears focused on administrative processes such as financial reporting, HR, and admissions. Not learning and teaching.

# Why RPA?

van der Aalst, Bichler & Heinzl (2018) introduce RPA and describe its place within the much broader and longer history of process automation with digital technologies. A part of that description uses the following diagram to position RPA and traditional process automation along the "long tail of work" (suggesting a Paeto distribution). They suggest that traditional process automation - typically large scale information systems projects - address the large number of cases that use the same structured process (the left-hand end of the graph). Where there's an economy of scale. At the other end of the graph are processes that can only be done by manually people. They are too infrequent and ad hoc to be efficiently or effectively automated.  

This leaves a lot of cases in the middle of the graph. These cases involve (often painfully inefficient) repetitive work. But can't be automated because the cost/benefit trade-off doesn't work. There's not quite enough of these cases to justify large enterprise process automation. In particular, when these cases often rely on proprietary or legacy information systems that enterprise automation can't work with. Traditional process automation - like all traditional enterprise information systems - require long and expensive implementations resulting in relatively inflexible systems, whereas RPA aims for "quick wins that require little investment" (van der Aalst, 2018, p. 271). There is a mismatch between the purpose of enterprise automation tools and the purpose of RPA.

![Positioning RPA (van der Aalst et al, 2018 p. 270)](https://djon.es/assets/memex/share/blog/images/positioningRPA.png)  

## Lightweight IT 

RPA is just one example of what Bygstad (2017) defines as lightweight IT defined as
> a socio-technical knowledge regime, driven by competent users’ need for solutions, enabled by the consumerisation of digital technology, and realised through innovation processes (p. 181)
Lightweight IT (RPA) is positioned as a very different but complementary "socio-technical knowledge regime" to traditional heavyweight IT (traditional process automation/BPM).

| Characteristics | Heavyweight IT | Lightweight IT |
| -------------- | ------------- | ------------- |
|           | A knowledge regime, driven by IT professionals, enabled by systematic specification and proven digital technology and realised through software engineering | A knowledge regime, driven by competent users' need for solutions, enabled by the consumerisation of digital technology and realised through innovation processes |
| Profile | Back-end: supporting documentation of work | Front-end: supporting work processes |
| Owner | IT Department | Users and vendors |
| Systems | Transaction systems | Process support, apps, BI |
| Technology | PCs, servers, databases, integration technology | Tablets, electronic whiteboards, mobile phones | 
| IT architecture | Fully integrated solutions, centralised or distributed architecture | Non-invasive solutions, frequently meshworks (heterogeneous networks) |
| Development culture | Systematics, quality, security | Innovation, experimentation |
| Problems | Increasing complexity, rising costs | Isolated gadgets, security |
| Discourse | Software engineering | Business and practice innovation|

The ["citizen developer" label](https://monday.com/blog/builders/citizen-developer/) beloved of Gartner and Micrsoft (PowerBI, PowerAutomate etc) is another example of lightweight IT. Further evidence that vendors and organisations are increasingly recognising the need and value of actively supporting what used to be [labelled as feral or shadow systems](https://dl.acm.org/doi/10.1145/1461928.1461960).

# The need for RPA and lightweight IT development in a LMS migration

Where I currently work we're in the process of migrating from Blackboard Learn to Canvas. I work with one part of the institution responsible for migrating 1400 courses (some with multiple course sites) over 18 months. As you may imagine, LMS migration is an important project with much of the organisation expending effort to make sure it succeeds. This includes heavyweight IT through the new LMS vendor, our organisational IT division, and various other enterprise systems and practices. For example, the [common cartridge standard](https://www.imsglobal.org/activity/common-cartridge) for exporting content from one LMS to another; and, the [Learning Tools Interoperability (LTI) standard](https://www.imsglobal.org/lti-advantage-overview) for establishing "one-click, seamless" connections between an LMS and external learning tools. All should be good, right?

What the following illustrates is that the heavyweight IT approach is insufficient for an effective and efficient migration. Echoing the enterprise automation/RPA figure above the following illustrates that migrating an LMS migration involves a "long tail" of work. That heavyweight IT approaches work fine for part of the tail, but not so good elsewhere. As I stand in the middle of an LMS migration, I'd also argue that the part of the "long tail" covered by heavyweight IT is significantly smaller than what is represented in the diagram above. The following illustrates the lightweight IT work we're doing to fill the gap.

The notion of [umwelt](https://pluralistic.net/2022/06/07/more-than-human/#umwelt) from cybernetics. The idea that enterprise software's umwelt is for a certain type of problem. Perhaps the not type of problem that we now need to solve in L&T.  Or pointing at the type of problem which enterprise L&T has ignored/been incapable of dealing with e.g. the following

## Problem: Migrating echo360 embeds from Blackboard to Canvas

Currently we're working on migrating ~500 Blackboard course sites. [Echo360](https://echo360.com/) is used in these course sites for lecture capture and for recording and embedding other videos.  Echo360 is an external tool, it's not part of the LMS (Blackboard or Canvas). Instead, the Learning Tools Interoperability (LTI) standard is used to embed and link echo360 videos into the LMS. You might assume that because of LTI and common cartridge exports you could just export content from Blackboard, import it to Canvas, and through the magic of LTI all would still work. You would be wrong.

If I use Blackboard's Echo360 LTI plugin to embed an echo360 video into Blackboard it will use a very specific id (e.g. f34e8a01-4f72-46e1-XXXX-105064c3f75f). If I use the Canvas Echo360 LIT plugin to embed the very same video into Canvas it will use a very different id (e.g. 49dbc576-XXXX-4eb0-b0d6-6bbeaa800707). That is, for each echo360 video embed you wish to migrate from Blackboard to Canvas you need to regenerate a new id. Reinforcing that the purpose of LTI is to connect a particular LMS to a particular external tool. The purpose of LTI is *not* to make it easy to migrate content from one LMS to another.

Of the ~500 course sites we're currently working on there are 2162 echo360 embeds. Those are spread across 98 of the course sites. Those 98 course sites have on average 22 echo360 videos. 62 of the course sites have 10 or more echo360 embeds. One course has 142 echo360 embeds. With 2000+ videos deciding which videos require Canvas specific ids and generating the required ids is a lot of work. Especially since echo360 makes this more difficult.

The way echo360 works makes 
- only the video owner can access it
- except for the "root" user - who can access everything


Problem - echo360. Diagram showing echo360, Bb and Canvas.  Same video in echo360, but different ids in Bb than Canvas.

**Question** Can I get a graph of courses with echo360 videos in DW2?

Manual solution. The "RPA" solution - but someone still needs to manually gather the list of video titles in a course. Send it to someone with permission and get the response back and then integrated into Canvas

explain
- Pickle - already have the list
- coursePages - old echo360 iframes modified to new
- word2canvas - upload into Canvas


This type of work is not new, I imagine there are staff all over doing this work which a quick look at github and Canvas community forums confirms.

# "RPA" as part of digital transformation

"Digital transformation" increasingly features in the strategic plans for many universities. Personally observed plans for achieving "digital transformation" currently appear to largely focused on the IT department implementing lots of big enterprise platforms. As highlighted above those platforms are probably going to struggle to meet the purposes of the learners, teachers, and other staff trying to implement "digital transformation".

Anne-Marie Scott writes about a [very different take on digital transformation](https://ammienoot.com/brain-fluff/digital-transformation-and-why-it-cant-be-done-without-learning-technologists/). One where digital transformation won't work if all the digital expertise is constrained in the IT department. Or - linke to Col's post about taking tech as given

Scott talks about "vary widly between disciplines and institutions"....touch on this

Migration is a one-off process, but these requirements will continue...something about purpose and assemblage

# References

Bygstad, B. (2017). Generative Innovation: A Comparison of Lightweight and Heavyweight IT: *Journal of Information Technology*. <https://doi.org/10.1057/jit.2016.15>

Leonardi, P. M. (2011). When Flexible Routines Meet Flexible Technologies: Affordance, Constraint, and the Imbrication of Human and Material Agencies. *MIS Quarterly*, *35*(1), 147--168.

van der Aalst, W. M. P., Bichler, M., & Heinzl, A. (2018). Robotic Process Automation. *Business & Information Systems Engineering*, *60*(4), 269--272\. <https://doi.org/10.1007/s12599-018-0542-4>

Yoo, Y. (2013). The Tables Have Turned: How Can the Information Systems Field Contribute to Technology and Innovation Management Research? *Journal of the Association for Information Systems*, *14*(5), 227--236.