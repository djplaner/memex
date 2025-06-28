---
backlinks:
- title: Orchestration
  url: /memex/sense/orchestration.html
- title: 'Orchestrating entangled relations to break the iron triangle: Observations
    from an LMS migration'
  url: /memex/share/conferences/ascilite-2022/observations-from-an-lms-migration.html
- title: Distribution
  url: /memex/sense/Distribution/distribution.html
title: Evaluating orchestration
---
Nascent attempt to extract meaning from [[role-of-relationships-breaking-the-iron-triangle]]

Assumption is that "orchestration" is key to educational technology - in the sense of Fawns' [[entangled-pedagogy]] and Dron's [[educational-technology-what-is-it-and-how-it-works]] and in particular Dron's quote from Arthur (2009) - something like
> Technology is the orchestration of phenomena for a purpose

Most of the focus of higher education educational strategy and literature is on the purpose and the phenomena. Where the phenomena are the building blocks that are used for actually doing something.  Doing anything requires orchestration.

Ellis & Goodyear (2019)
- why “most of the effort by L&T centres is directed to a small minority of willing academics” and such “centres are not equipped or motivated to operate strategically, at scale” (Ellis & Goodyear, 2019, p. 202).
- “privileges outcome measures at the expense of understanding the processes that generate those outcomes” (Ellis and Goodyear, 2019, p. 2).

## The aim

There are many ways to achieve a purpose in learning. Many ways to orchestrate. How do you judge which ones are good? Which ones are going to help your institution break the iron triangle? 

The aim is to develop some criteria/questions to ask about the orchestration informed by the cases mentioned in [[role-of-relationships-breaking-the-iron-triangle]]

## The questions

1. How much context and learning design specific information is stored digitally?

    Having it stored digitally is a pre-requisite for being able to analyse, manipulate and generally orchestrate this information using digital technologies. This is generally what is missing.

2. At what scale can the orchestration work?

	Does it have to be done manually? Course by course? Module by module? Can it be done automatically for 100s of courses.

3. How hard/soft or generative is the orchestration?

	Hard/soft is a measure of how much manual labour is required to orchestrate. Generative is a measure of how much the orchestration enables further orchestration.

## Links to the iron triangle

The iron triangle is based on the following three attributes and the idea that changing one (e.g. increasing access during COVID) will have an impact on the others (e.g. perceptions that quality suffered during COVID and cost a lot of effort from staff).

| Attribute | Description |
| --- | --- | 
| Quality | It's good. Educationally, disciplinary, societal, visually, information architecture, etc. |
| Access | As many people as possible, both in terms of scale (large classes) and diversity (accessibility, micro-credentials, on-campus, online, hybrid, etc. ) |
| Cost efficiency | It's cheap |

### Quality

Quality is dependent upon questions 1 and 3.

This is largely based on the argument behind the [[reusability-paradox]], [tpack](https://djon.es/blog/2015/01/06/tpack-as-shared-practice-toward-a-research-agenda/) etc. i.e. that the quality of L&T is typically related to its fitness for purpose. i.e. how well it fits the disciplinary knowledge and more importantly the context, the students etc.  The more specific an orchestration is the more pedagogically valuable it will be.

The more generative (softer) the orchestration the more it can be modified for different context and learning design requirements. Both by teachers and learners.

#### Example - [Canvas Modules view versus Canvas Collections](https://djon.es/blog/2022/07/05/orchestrating-entangled-relations-to-break-the-iron-triangle-examples-from-a-lms-migration/#3-making-teaching-and-learning-easier-better-using-a-vanilla-lms)

Canvas Modules view is vanilla. No explicit support for contextual design. It is, however, somewhat generative with two common examples:

1. People using the Module title to **manually** inject emojis or context specific text (e.g. _Module 1_)
2. The common Canvas community practice of creating visual Canvas pages to provide that context. An example of how a relatively hard technology (Module view) is softened by orchestration into a broader assemblage.

All three of [Canvas Collections' main features](https://djplaner.github.io/canvas-collections/features/) are designed to support the injection of more contextual design information into the Canvas module view. Generativity is built into Canvas Collections through the following

1. The representation of each collection can include the content of any specified Canvas page (called an _include page_)
2. There is a set of choices for the representation of each collection and Collections is designed to enable the easy inclusion of new representations.

### Access 

Dependent upon all three. Providing access means supporting a useful combination of both scale and diversity. Scale because you need to do lots (e.g. migrating all an institution's course sites) and supporting diverse needs (e.g. good course sites for sculpture are different to good course sites for numeric analysis). Thus

1. More contextual knowledge that is available digitally allows more use of digital technology to automate and handle diversity.
2. The more manual work required, the more it's going to cost.
3. The harder a technology is, the more likely it will require manual intervention.

#### Example - [Moving content from one LMS to another](https://djon.es/blog/2022/07/05/orchestrating-entangled-relations-to-break-the-iron-triangle-examples-from-a-lms-migration/#moving-content-from-one-lms-to-another-using-the-common-cartridge-standard)

Using the Common Cartridge standard to migrate course content means
1. Explicitly removing all contextual knowledge.

    By definition/purpose, Common Cartridge defines a generic standard.

2. Manual migration at course level and then lots of within course modification to achieve any quality.

    Most LMS are designed so that export/import is a manual process. Once imported, the limitation from #1 means that a lot of manually, ad hoc editing is required to retrieve the design intent. Especially because Common Cartridge - as implemented by different LMS - varies and fails to migrate all features.

3. Common Cartridge is a defined standard (hard) and its complexity means there are limited digital possibilities to orchestrate (beyond what is provided by the LMS)

The CAR process explicitly captures local context. i.e. that we're moving from Blackboard to Canvas. That our Blackboard course sites typically use this structure and that translates into Canvas this way.

Aspects of the process operate at scale (scripts that perform tasks for 100s/1000s of courses), but there are other aspects that do require manual course by course and task by task work. The CAR supports this work through various artefacts.

Those artefacts are designed to be generative. To allow individual migration teams to orchestrate them with other technologies as appropriate. The CAR process itself is generative and has evolved considerable in response to need.
	
### Cost efficiency

Dependent upon all three, but number two is increasingly important.

Much of the work involved with digital education requires manual orchestration. Which increases HR cost (hire more people) but also potentially increases cost due to increased chance of human error. Also, because "good" digital education typically requires complex "TPACK" which most teachers do not have, quality suffers.

### Example - [Migrate Echo360 videos from Blackboard to Canvas](https://djon.es/blog/2022/07/05/orchestrating-entangled-relations-to-break-the-iron-triangle-examples-from-a-lms-migration/#1-connect-the-lms-with-an-ecosystem-of-tools-using-the-lti-standard)

LTI means that the standard process required significant manual work from at least two people

- Migration officer; and,

    Manually identify exact names all echo360 videos in a Blackboard course site, generate a list and email to the helpdesk. Once the helpdesk returns the modified list of echo360 embeds, the migration officer has to manually update the Canvas course site with the new embeds.

- Helpdesk.

    Manually receive lists of echo360 videos from Migration officers. Manually search echo360 for the videos, generate a ne embed code, update the list and return to the migration officer.

The CAR process automates all of this. No manual work required

[//begin]: # "Autogenerated link references for markdown compatibility"
[role-of-relationships-breaking-the-iron-triangle]: ../Design/role-of-relationships-breaking-the-iron-triangle "Orchestrating entangled relations to break the iron triangle: Observations from an LMS migration"
[entangled-pedagogy]: ../Distribution/entangled-pedagogy "Entangled Pedagogy"
[educational-technology-what-is-it-and-how-it-works]: ../Affordances/educational-technology-what-is-it-and-how-it-works "Educational technology: what is it and how it works"
[reusability-paradox]: ../Bricolage/reusability-paradox "Reusability Paradox"
[//end]: # "Autogenerated link references"