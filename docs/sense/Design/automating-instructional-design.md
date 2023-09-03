<!--
 Copyright (C) 2023 David Jones
 
 This file is part of memex.
 
 memex is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 memex is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with memex.  If not, see <http://www.gnu.org/licenses/>.
-->

# Automating instructional design

See also: [[design]]

## Background

Exploration into the literature on automating instructional design. First sparked by [[goodyear-patterns-design-practice]]'s reference of Tennyson (1994)

## Some key themes and lessons

- attempts to automate improve understanding of what's being automated

	> The main theme of this chapter is that regardless of success or failure (in the sense of continued funding or market success), attempts to automate a complex process nearly always provide a deeper understanding of the complexities of that process. (Spector & Ohrazda, 2004, p. 685)

- instructional computing tends to be a generation behind software engineering arguably because
  - ID and training are less important than other arrangements
  - "educational applications are typically more complex and challenging than applications in many business and industry settings" (Spector & Ohrazda, 2004, p. 685)

Spector & Ohrazda (2004, p. 696)
> In the process of attempting to automate ID, key lessons include the following: 
> 1. Strong systems work only in narrow and well-defined domains; there will continue to be opportunities to develop intelligent agents in support of learning, more so in the delivery domain (downstream activities) and less so in the planning and analysis phases (upstream activities). 
> 2. Knowledge management systems are by nature weak systems and have a definite place in ID, which is by nature complex and often involves teams and enterprise-level learning and performance issues; some components of a knowledge management system for ID may involve strong and intelligent support, as in an intelligent agent to perform a particular task. 
> 3. The value of knowledge objects and reuse is likely to be realized only when humans are kept involved and systems kept open. 
> 4. We learn a lot about a process by trying to automate it; we find out how much human involvement is required and when and why such involvement is advisable. We should not discourage or denigrate attempts to automate more ID processes—we always learn something in the process. 
> 5. The temptation will be to base strong automated support for ID on knowledge objects and metatagging. 
> 6. Human involvement in the ID process will still be necessary and the real value of reusability and knowledge management in support of ID will be realized only if humans are involved in the process (Ganesan et al., 2001).

### Findings

- Evaluating automated ID systems is complex
- Arguments for the evaluation of automated systems to consider uses by novices; experts; and also organisational considerations
- Productivity improvements have been found in systems that provide performance support or automate portions
- Improvements in learning outcomes can results from systems that enable designers to adapt systems to particular needs - see [[generativity]], [[protean]]
- Significant improvements in learning outcomes largely found where there are well-structured learning goals (e.g. beginning programming, or simple troubleshooting)
- No published research findings on the organisational impact of these systems - only anecdotal

### Trends and issues

Heavy focus on object-oriented approaches - knowledge modelling, tagging etc. Knowledge objects.

### Phases of instructional design and automation

Organising the phases of ADDIE/waterfall design models into "sets of processes" (Spector & Ohrazda, 2004, p. 686)

1. _front-end_ - analysis and planning
2. _middle-phase_ - design, development, refinement and delivery
3. _follow-through_ - summative and confirmative evaluation, life-cycle management, and maintenance

Goodyear (1994) uses _upstream_ (analysis and planning) and _downstream_.

Types of automation

1. _strong support_ - replacing human activity with automation
2. _weak support_ - "aimed at extending what humans can do, often to make less experienced practitioners perform more like experts" (Spector & Ohrazda, 2004, p. 686) - moving more towards a performance support system e.g. job aids.

Weak systems are generally more successful.  Though narrowly focused strong systems have met with success.

### Types of automated id systems

1. _Advisory/critiquing ID systems_

	- given a design and a set of outcomes offer a critique
	- Planned, some early attempts, never really done, too complex - framed as a desirable long-term goal 
	- Would need sophisticated pattern recognition and significant expert knowledge
	- Obviously more possible now with LLMs

2. _Expert ID systems_

	- Old style expert systems used to support specific tasks e.g. developming materials or ITS (intelligent tutoring systems)
	- Numerous examples provided

3. _Information Management and ID systems_

	- Focused more on the process of scaffolding/managing the information required for ID
	- e.g. development of a knowledge model for a solution domain; development of a method of instruction; develop the environment for the delivery of instruction
	- LMS get at the last one, but so much the others - but the authors place LMS in the last type

4. _EPSSs for ID_

	- Providing targetted support for specific tasks within a larger system

5. _ID Authoring tools_

	- Focused on the authoring process


## Spector & Ohrazda (2004)

Distill questions from the automation of software engineering to apply to the automation of instructional design.

_Instructional Design_ - a broad design - "is interpreted broadly and includes a collection of activities to plan, implement, evaluate, and manage events and environments that are intended to facilitate learning and performance" (p. 687)

But focus is on the "upstream" tasks (largely planning and prototyping) and "largely ignores that area of instructional delivery" for two reasons 

1. Too many systems for instructional delivery for their brief discussion
2. "most notable aspect of automation in instructional delivery concerns intelligent tutoring systems"

## references

Tennyson, R. (Ed.). (1994). Automating instructional design, development and delivery. Berlin: Springer Verlag.

Spector, J. M., & Ohrazda, C. (2004). Automating Instructional Design: Approaches and Limitations. In *Handbook of Research on Educational Communications and Technology* (2nd ed.). Routledge.

[//begin]: # "Autogenerated link references for markdown compatibility"
[design]: design "Design"
[generativity]: ../nodt/generativity "Generativity"
[protean]: ../concepts/protean "Protean"
[//end]: # "Autogenerated link references"
[//begin]: # "Autogenerated link references for markdown compatibility"
[design]: design "Design"
[goodyear-patterns-design-practice]: <../Paper Summaries/goodyear-patterns-design-practice> "Patterns, pattern languages and design practice"
[generativity]: ../nodt/generativity "Generativity"
[protean]: ../concepts/protean "Protean"
[//end]: # "Autogenerated link references"