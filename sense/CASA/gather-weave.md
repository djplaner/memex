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

# Gather and Weave

See also:  [[design]], [[gather-weave-literature]], [[data-portability-interoperability]], 

The "gather and weave" metaphor emerged from [work by Henry Cook, Steven Booten, and I](https://djon.es/blog/2023/02/09/gathers-weavers-and-augmenters-three-principles-for-dynamic-and-sustainable-delivery-of-quality-learning-and-teaching/) during an institutional LMS migration. Subsequently we started exploring how it may be useful for business as usual. Beyond that, perhaps a useful abstract way to think more broadly about educational design and development in an increasingly entangled/complex L&T context.  

This model starts with the observation that [educational-design and development](../../share/blog/2023/conceptualising-educational-design.md) is a process of gathering and weaving an increasingly large and entangled collection of knowledge and technologies in order to automate/augment the learning and teaching experience and outcomes.

## How to implement it practically?

Kuebler-Wachendorff et al (2021)

> Apart from progress in understanding which data are worth porting, the question remains as to how direct data portability is best implemented in practice. (p. 270)

Related projects 

- [[data-transfer-project]]

### Challenges/reflections 

Our work resembles this but in an informal way. Standards like "IMS" did not capture what was necessary. We had to put in a lot of work on company specific adapaters to capture more learning design and context specific requirements. 

- Standards appear to come and go and also not always capture the full reality, does this mean that a focus on standards bodies over code is problematic?
- Our task (migrating learning and teaching) is significantly more variable than most social media.

## Original thinking - Automating and augmenting gathering and weaving 

We found and argue that the value of digital technologies to education design and development is the ability to automate and augment the gathering and weaving process. Doing this is not just a question of choosing and using digital technology. Instead, we found it appears to work better when informed by these three principles:

1. On-going activity focused (re-)entanglement.

    Our work was focused on high level activities (e.g. analysis, migration, quality assurance, course design of 100s of course sites). Activities not supported by any single technology. Activities that can involve multiple disparate digital technologies. Each of those technologies with its own expectations and affordances. Consequently, educational design and development often involves significant manual gathering and weaving - i.e. the opposite of automating and augmenting. 
	
	By starting small and continually responding to changes and lessons learned, we automated and augmented educational design and development by figuring out how to digitally gather and weave the relevant strands. We used digital technology to create larger assemblages.

2. Contextual digital augmentation.

	In our experience, the available digital tools were either very limited or completely unable to store and use context specific knowledge. Requiring teachers and students to manually gather and weave context specific knowledge into their learning environments and tasks. Increasing the complexity and reducing the quality.
	
	Significant value was found by expanding the quantity and quality of contextual information available in digital forms and using that to automate and augment the design and support of learning environments and tasks. 

3.  Meso-level focus.

    Existing component technologies generally provide universal solutions for the institution or all users of the technology. Requiring manual gathering and weaving to fit contextual needs for each individual variation. By leveraging the previous two principles we were able to provide “technologies that were fit for meso-level solutions. For example, all courses for a program or a school. All courses, that use a complex learning activity like interactive orals.

## Examples 

- [Student confusion around assignment dates in Canvas](https://twitter.com/jsench/status/1655972564089315329)

	Academic sharing the confusion created by the clash between how within the Canvas LMS various dates (open, due, close) associated with assignments can contribute to confusion amongst students of when an assignment is due.  Consequently generating increased requests for extensions etc. Arguably an example of how the difficulty in gathering and weaving together disparate strands in a contextually appropriate manner is difficult. 
	
	The resulting twitter thread is full of others sharing similar experience and others explaining how to more effectively gather and weave the disparate strands to avoid/prevent this confusion. Part of the issue appears to be that there are different activities to be completed around the assignments. The student needs to know when to submit and the teacher wants to control when the assignment is open and closed for submission. These activities rely on the same data, but having the student calendar include the close date (perhaps not strictly required for the submission activity) causes the issue.  Is there no way to remove the "close" date from the student calendar?

	It's not something I've been able to recreate.



[//begin]: # "Autogenerated link references for markdown compatibility"
[design]: ../Design/design "Design"
[gather-weave-literature]: gather-weave-literature "Literature and quotes mentioning gather/weave concepts"
[data-portability-interoperability]: ../computing/data-portability-interoperability "Data portability and interoperability"
[data-transfer-project]: data-transfer-project "Data Transfer Project (Initiative)"
[//end]: # "Autogenerated link references"