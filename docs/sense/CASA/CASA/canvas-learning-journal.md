---
title: Canvas Learning Journal
---
Document exploration and design of a [[learning-journal]] [[casa]] for Canvas.

- 1701LHS, 1712LHS, 7714LAW

## Spark

Increasing need to support a more "learning process" focus in assessment leading to need for a learning journal type tool.  Issues with the _Response Tool_ and absence of similar functionality unsuitable. PebblePad too heavyweight an option for a light tough learning journal.

## Design

- [[log-1-canvas-learning-journal]]
- [[log-2-canvas-learning-journal]] - initial concrete design
- [[log-3-canvas-learning-journal]] - report design and implementation - working version of report complete
- [[log-4-canvas-learning-journal]] - implement the creation/maintenance of the groupset/groups for students.

## Exploration of Canvas community practices

In summary,

- Canvas doesn't provide a learning journal tool.
- Various external vendors provide options.
- Common "kludge" used by Canvas users is to use a (single student) group discussion topic, one for each student.
- Implementation is not entirely straight forward.
- In Canvas, each group gets their own "mini-Canvas" site, including discussion topics and much more. 
- May be some value in designing a CASA to create and manage a single student group based learning journal

### Vendors

- [Stackle request for feedback](https://community.canvaslms.com/t5/Higher-Ed-Canvas-Users/Request-for-Feedback-Learner-Portfolios-Learning-Journals-and/m-p/570644)
    - Learner Portfolios
    - Learning Journals 
    - Course workbooks
- [Atomic Jolt](https://community.canvaslms.com/t5/Partner-Listings/Partner-Listing-Atomic-Jolt-Search-Assessments-Journals-Polls/ta-p/434810) - partner listing
  - [Atomic Journals](https://www.atomicjolt.com/atomic-journals)

- [LTI solution - The Learning Journal](https://community.canvaslms.com/t5/Idea-Conversations/Implementing-private-journals-into-Canvas/idc-p/465326/highlight/true#M51367) includes student reflections going beyond the course
    - [The Learning Journal](https://thelearningjournal.co/)

### Is there a journal?

- [2018 request](https://community.canvaslms.com/t5/Canvas-Question-Forum/Is-there-a-journal/m-p/124779)

> I need to create a way for students to collect a number of bi-weekly writing assignments in a private journal, or logbook, or portfolio.The complete collection of assignments will eventually be graded, but they will not necessarily be read or marked as soon as they are written.Students should also be able to go back and add to, or change their posts, or at least comment on them, and I need to do that too. I used to use the journal function in Blackboard for this, but can't find an equivalent in Canvas. In a response to another question I saw the suggestion to create individual discussions for each student, and that might work, although it will not be possible to set this up until the students have been added to the course because until then I cannot be sure how many they are. I would like to be able to do most of the setting up before term starts. :slightly_smiling_face: The e-portfolio looked promising, but that is not something I can assign and grade in a course, is it? An open assignment would work, I suppose, but that would mean opening six or seven different submissions per student, instead of just scrolling down, wouldn't it? And students would not be able to go back and change anything, would they? Perhaps discussions is the best option? Grateful for any suggestions .

### Implementing private journals in Canvas

[2021 idea conversation](https://community.canvaslms.com/t5/Idea-Conversations/Implementing-private-journals-into-Canvas/idi-p/444842)

> Private journals are hard to create though on Canvas. In the current system, one has to create group sets (e.g Private Journals) under “People” and assign students one by one. Then under discussion, a new discussion for each topic (Private Journal 1, Private Journal 2…) must be created, and importantly one should also remember to check “this is group discussion” (private journals etc) to make them private before saving…This process can be cumbersome  

- [support for the request](https://community.canvaslms.com/t5/Idea-Conversations/Implementing-private-journals-into-Canvas/idc-p/463663/highlight/true#M50979)
- [more support](https://community.canvaslms.com/t5/Idea-Conversations/Implementing-private-journals-into-Canvas/idc-p/483072/highlight/true#M54869) ...and many others

### Amazement

- [find it amazing there still isn't one](https://community.canvaslms.com/t5/Canvas-Question-Forum/Journalling-in-Canvas/m-p/471790/highlight/true#M158063) and more just after it
    - [Instead of having faculty spending so much precious time creating the pseudo-journal alternatives?](https://community.canvaslms.com/t5/Canvas-Question-Forum/Journalling-in-Canvas/m-p/463665/highlight/true#M156299)

## solutions

- [One student groups and discussion](https://community.canvaslms.com/t5/Canvas-Question-Forum/Is-there-a-journal/m-p/124780/highlight/true#M44716)
  - [Bit more detail on process](https://community.canvaslms.com/t5/Idea-Conversations/Student-Journal-or-Blog-Feature/idc-p/320217/highlight/true#M6251) 
    - Using group set with a few clicks
  - [ANother take - including some limitations](https://community.canvaslms.com/t5/Idea-Conversations/Student-Journal-or-Blog-Feature/idc-p/320218/highlight/true#M6252)
  - [query leading to more discussion on how](https://community.canvaslms.com/t5/Canvas-Question-Forum/Journalling-in-Canvas/m-p/182714)
  - [recipe solution](https://community.canvaslms.com/t5/Canvas-Question-Forum/Private-journal-discussions/m-p/175097/highlight/true#M81421)
- [Laura offers the blog and other external solutions](https://community.canvaslms.com/t5/Canvas-Question-Forum/Is-there-a-journal/m-p/124784/highlight/true#M44720)
- [2016 suggestion to use Google doc with assignment submission](https://community.canvaslms.com/t5/K12-Canvas-Users/Online-Journaling-for-Better-Learning-and-Teaching/ba-p/273213)
- [Canvas eportfolio tool](https://community.canvaslms.com/t5/Idea-Conversations/Student-Journal-or-Blog-Feature/idc-p/320152/highlight/true#M6186)
- [Per student page editing](https://community.canvaslms.com/t5/Idea-Conversations/Student-Journal-or-Blog-Feature/idc-p/320155/highlight/true#M6189)

## In operation

The group that is set up can have an entire "view" of Canvas - pages, discussions, files etc. Not just the discussion. Could be useful for setting up background, but using the discussion for submission? [Canvas explanation](https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-are-Groups/ta-p/16) is that groups "are a small version of a course".

Or perhaps by using multiple marked discussions for different tasks.

- [ ] Learn more about how groups work.
  - [better group navigation](https://community.canvaslms.com/t5/Higher-Ed-Canvas-Users/Better-Group-Discussion-Navigation/ba-p/263064)




[//begin]: # "Autogenerated link references for markdown compatibility"
[learning-journal]: ../../Teaching/learning-journal "Learning Journal"
[casa]: ../casa "Contextually Appropriate Scaffolding Assemblages (CASA)"
[log-1-canvas-learning-journal]: log-1-canvas-learning-journal "log-1-canvas-learning-journal"
[log-2-canvas-learning-journal]: log-2-canvas-learning-journal "Canvas learning journal - log 2"
[log-3-canvas-learning-journal]: log-3-canvas-learning-journal "Log 3 - Canvas learning journal"
[log-4-canvas-learning-journal]: log-4-canvas-learning-journal "Log 4 - Canvas learning journal dev"
[//end]: # "Autogenerated link references"