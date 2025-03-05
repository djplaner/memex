# Gatherers, Weavers and Augmenters: Three principles for dynamic and sustainable delivery of quality learning and teaching
#### by admin, [djon.es](https://djon.es/blog/2023/02/09/gathers-weavers-and-augmenters-three-principles-for-dynamic-and-sustainable-delivery-of-quality-learning-and-teaching/) ▪ Thursday, February 9, 2023, 10:13 AM

See also: [[paper-ideas]]

Henry Cook, Steven Booten and I gave the following presentation at [the THETA conference](https://theta.edu.au/) in Brisbane in April 2023.

Below you will find

*   Summary – a few paragraphs summarising the presentation.
*   Slides – copies of the slides used.
*   Software – some of the software produced/used as part of the work.
*   References – used in the summary and the slides.
*   Abstract – the original conference abstract.

### Summary

The presentation used our experience as part of a team migrating 1500+ course sites from Blackboard to Canvas to explore a broader challenge. A challenge recently expressed in the [Productivity Commission’s “Advancing Prosperity” report](https://www.pc.gov.au/inquiries/completed/productivity/report) with its recommendations to grow access to tertiary education while containing cost and improving quality. This challenge to maximise all cost efficiency and quality and access (diversity & scale) is seen as a key issue for higher education (Ryan et al., 2021). It has even been labelled the “Iron Triangle” because – unless you change the circumstances and conditions – improving one indicator will almost inevitably lead to deterioration in the other indicators (Mulder, 2013). The pandemic emergency response being the most recent example of this. Necessarily rapid changes to access (moving from face-to-face to online) required significant costs (staff workload) to produce outcomes that are perceived to be of questionable quality.

Leading to the question we wanted to answer:

How do you stretch the iron triangle? (i.e. maximise cost efficiency, quality, and accessibility)?

In the presentation, we demonstrated that the fundamental tasks (gather and weave) of an LMS migration are manual and repetitive. Making it impossible to stretch the iron triangle. We illustrated why this is the case, demonstrated how we addressed this limitation, and proposed three principles for broader application. We argue that the three principles can be usefully applied beyond LMS migration to business as usual.

#### Gatherers and weavers – what we do

Our job is to help academic staff design, implement, and maintain quality learning tasks and environments. We suggest that the core tasks required to do this is to gather and weave disparate strands of knowledge, ways of knowing (especially various forms of design and contextual knowledge and knowing), and technologies (broadly defined). For example, a course site is the result of gathering and weaving together such disparate strands as: content knowledge (e.g. learning materials); administrative information (e.g. due dates, timetables etc); design knowledge (e.g. pedagogical, presentation, visual etc); and information & functionality from various technologies (e.g. course profiles, echo360, various components of the LMS etc).

An LMS migration is a variation on this work. It has a larger (all courses) and more focused purpose (migrate from one LMS to another). But still involves the same core tasks of gathering and weaving. Our argument is that to maximise the cost efficiency, accessibility, and quality of this work you must do the same to the core tasks of gathering and weaving. Early in our LMS migration it was obvious that this was not the case. The presentation included a few illustrative examples. There were many more that could’ve been used. Both from the migration and business as usual. All illustrating the overly manual and repetitive nature of gathering and weaving required by contemporary institutional learning environments.

#### Three principles for automating & augmenting gathering & weaving  – what we did

Digital technology has long been seen as a key enabler for improving productivity through its ability to automate processes and augment human capabilities. Digital technology is increasingly pervasive in the learning and teaching environment, especially in the context of an LMS migration. But none of the available technologies were actively helping automate or augment gathering and weaving. The presentation included numerous examples of how we changed this. From this work we identified three principles.

1.  On-going activity focused (re-)entanglement.  
    Our work was focused on high level activities (e.g. analysis, migration, quality assurance, course design of 100s of course sites). Activities not supported by any single technology, hence the manual gathering and weaving. By starting small and continually responding to changes and lessons learned, we stretched the iron triangle by digitally gathering and weaving disparate component technologies into assemblages that were fit for the activities.
2.  Contextual digital augmentation.  
    Little to none of the specific contextual and design knowledge required for these activities was available digitally. We focused on usefully capturing this knowledge digitally so it could be integrated into the activity-based assemblages.
3.  Meso-level focus.  
    Existing component technologies generally provide universal solutions for the institution or all users of the technology. Requiring manual gathering and weaving to fit contextual needs for each individual variation. By leveraging the previous two principles we were able to provide “technologies that were fit for meso-level solutions. For example, all courses for a program or a school. All courses, that use a complex learning activity like interactive orals.

#### Connections with other work

Much of the above is informed by or echoes related research and practice in related fields. It’s not just we three. The presentation made explicit connections with the following:

*   Learning and teaching;  
    Fawns’ (2022) work on entangled pedagogy as encapsulating the mutual shaping of technology, teaching methods, purposes, values and context (gathering and weaving). Dron’s (2022) re-definition of educational technology drawing on Arthur’s (2009) definition of technology. Work on activity centered design – which understands teaching as a distributed activity – as key to both good learning and teaching (Markauskaite et al, 2023), but also key to institutional management (Ellis & Goodyear, 2019). Lastly – at least in the presentation – the nature and need for epistemic fluency (Markauskaite et al, 2023)
*   Digital technology; and,  
    Drawing on numerous contemporary practices within digital technology that break the false dilemma of “buy or build”. Such as the project to product movement (Philip & Thirion, 2021); Robotic Process Automation; Citizen Development; and the idea of lightweight IT development (Bygstad, 2017)
*   Leadership/strategy.  
    Briefly linking the underlying assumptions of all of the above as examples of the move away from corporate and reductionist strategies that reduce people to “smooth users” toward possible futures that see us as more “collective agents” (Macgilchrist et al, 2020). A shift seen as necessary to more likely lead – as argued by Markauskaite et al (2023) – to the “even richer convergence of ‘natural’, ‘human’ and ‘digital’ required to respond effectively to global challenges.

There’s much more.

### Slides

The presentation does include three videos that are available if you [download the slides](https://docs.google.com/presentation/d/1D5Fcuw4EPa14dDOzAeBLmOdZf73TYtjV/edit?usp=sharing&ouid=110869324164028184563&rtpof=true&sd=true).

### Related Software

[Canvas QA](https://github.com/StevenBooten/CanvasQA) is a Python script that will perform Quality Assurance checks on numerous Canvas courses and create a QA Report web page in each course’s Files area. The QA Report lists all the issues discovered and provides some scaffolding to address the issues.

[Canvas Collections](https://djplaner.github.io/canvas-collections/) helps improve the visual design and usability/findability of the Canvas modules page. It is Javascript that can be installed by institutions into Canvas or by individuals as a userscript. It enables the injection of design and context specific information into the vanilla Canvas modules page.

[Word2Canvas](https://djplaner.github.io/word-to-canvas-module/) converts a Word document into a Canvas module to offer improvements to the authoring process in some contexts. At Griffith University, it was used as part of the migration process where Blackboard course site content was automatically converted into appropriate Word documents.  With a slight edit, these Word documents could be loaded directly into Canvas.

### References

Arthur, W. B. (2009). _The Nature of Technology: What it is and how it evolves_. Free Press.

Bessant, S. E. F., Robinson, Z. P., & Ormerod, R. M. (2015). Neoliberalism, new public management and the sustainable development agenda of higher education: History, contradictions and synergies. _Environmental Education Research_, _21_(3), 417–432. [https://doi.org/10.1080/13504622.2014.993933](https://doi.org/10.1080/13504622.2014.993933)

Bygstad, B. (2017). Generative Innovation: A Comparison of Lightweight and Heavyweight IT. _Journal of Information Technology_, _32_(2), 180–193. [https://doi.org/10.1057/jit.2016.15](https://doi.org/10.1057/jit.2016.15)

Cassidy, C. (2023, April 10). ‘Appallingly unethical’: Why Australian universities are at breaking point. _The Guardian_. [https://www.theguardian.com/australia-news/2023/apr/10/appallingly-unethical-why-australian-universities-are-at-breaking-point](https://www.theguardian.com/australia-news/2023/apr/10/appallingly-unethical-why-australian-universities-are-at-breaking-point)

Ellis, R. A., & Goodyear, P. (2019). _The Education Ecology of Universities: Integrating Learning, Strategy and the Academy_. Routledge.

Fawns, T. (2022). An Entangled Pedagogy: Looking Beyond the Pedagogy—Technology Dichotomy. _Postdigital_ _Science and Education_, _4_(3), 711–728. [https://doi.org/10.1007/s42438-022-00302-7](https://doi.org/10.1007/s42438-022-00302-7)

Hagler, B. (2020). _Council Post: Build Vs. Buy: Why Most Businesses Should Buy Their Next Software Solution_. Forbes. Retrieved April 15, 2023, from [https://www.forbes.com/sites/forbestechcouncil/2020/03/04/build-vs-buy-why-most-businesses-should-buy-their-next-software-solution/](https://www.forbes.com/sites/forbestechcouncil/2020/03/04/build-vs-buy-why-most-businesses-should-buy-their-next-software-solution/)

Inside Track Staff. (2022, October 19). Citizen developers use Microsoft Power Apps to build an intelligent launch assistant. _Inside Track Blog_. [https://www.microsoft.com/insidetrack/blog/citizen-developers-use-microsoft-power-apps-to-build-intelligent-launch-assistant/](https://www.microsoft.com/insidetrack/blog/citizen-developers-use-microsoft-power-apps-to-build-intelligent-launch-assistant/)

Lodge, J., Matthews, K., Kubler, M., & Johnstone, M. (2022). _Modes of Delivery in Higher Education_ (p. 159). [https://www.education.gov.au/higher-education-standards-panel-hesp/resources/modes-delivery-report](https://www.education.gov.au/higher-education-standards-panel-hesp/resources/modes-delivery-report)

Macgilchrist, F., Allert, H., & Bruch, A. (2020). Students and society in the 2020s. Three future ‘histories’ of education and technology. _Learning, Media and Technology_, _45_(0), 76–89. [https://doi.org/10.1080/17439884.2019.1656235](https://doi.org/10.1080/17439884.2019.1656235)

Markauskaite, L., Carvalho, L., & Fawns, T. (2023). The role of teachers in a sustainable university: From digital competencies to postdigital capabilities. _Educational Technology Research and Development_, _71_(1), 181–198. [https://doi.org/10.1007/s11423-023-10199-z](https://doi.org/10.1007/s11423-023-10199-z)

Mulder, F. (2013). The LOGIC of National Policies and Strategies for Open Educational Resources. _International Review of Research in Open and Distributed Learning_, _14_(2), 96–105. [https://doi.org/10.19173/irrodl.v14i2.1536](https://doi.org/10.19173/irrodl.v14i2.1536)

Philip, M., & Thirion, Y. (2021). From Project to Product. In P. Gregory & P. Kruchten (Eds.), _Agile Processes in Software Engineering and Extreme Programming – Workshops_ (pp. 207–212). Springer International Publishing. [https://doi.org/10.1007/978-3-030-88583-0\_21](https://doi.org/10.1007/978-3-030-88583-0_21)

Ryan, T., French, S., & Kennedy, G. (2021). Beyond the Iron Triangle: Improving the quality of teaching and learning at scale. _Studies in Higher Education_, _46_(7), 1383–1394. [https://doi.org/10.1080/03075079.2019.1679763](https://doi.org/10.1080/03075079.2019.1679763)

Schmidt, A. (2017). Augmenting Human Intellect and Amplifying Perception and Cognition. _IEEE Pervasive Computing_, _16_(1), 6–10. [https://doi.org/10.1109/MPRV.2017.8](https://doi.org/10.1109/MPRV.2017.8)

Smee, B. (2023, March 6). ‘No actual teaching’: Alarm bells over online courses outsourced by Australian universities. _The Guardian_. [https://www.theguardian.com/australia-news/2023/mar/07/no-actual-teaching-alarm-bells-over-online-courses-outsourced-by-australian-universities](https://www.theguardian.com/australia-news/2023/mar/07/no-actual-teaching-alarm-bells-over-online-courses-outsourced-by-australian-universities)

### Abstract

The pandemic reinforced higher educations’ difficulty responding to the long-observed challenge of how to sustainably and at scale fulfill diverse requirements for quality learning and teaching (Bennett et al., 2018; Ellis & Goodyear, 2019). Difficulty increased due to many issues, including: competition with the private sector for digital talent; battling concerns over the casualisation and perceived importance of teaching; and, growing expectations around ethics, diversity, and sustainability. That this challenge is unresolved and becoming increasingly difficult suggests a need for innovative practices in both learning and teaching, and how learning and teaching is enabled. Starting in 2019 and accelerated by a Learning Management System (LMS) migration starting in 2021 a small group have been refining and using an alternate set of principles and practices to respond to this challenge by developing reusable orchestrations – organised arrangements of actions, tools, methods, and processes (Dron, 2022) – to sustainably, and at scale, fulfill diverse requirements for quality learning and teaching. Leading to a process where requirements are informed through collegial networks of learning and teaching stakeholders that weigh their objective strategic and contextual concerns to inform priority and approach. Helping to share knowledge and concerns and develop institutional capability laterally and in recognition of available educator expertise.

The presentation will be structured around three common tasks: quality assurance of course sites; migrating content between two LMS; and, designing effective course sites. For each task a comparison will be made between the group’s innovative orchestrations and standard institutional/vendor orchestrations. These comparisons will: demonstrate the benefits of the innovative orchestrations; outline the development process; and, explain the three principles informing this work – 1) contextual digital augmentation, 2) meso-level automation, and 3) generativity and adaptive reuse. The comparisons will also be used to establish the practical and theoretical inspirations for the approach, including: RPA and citizen development; and, convivial technologies (Illich, 1973), lightweight IT development (Bygstad, 2017), and socio-material understandings of educational technology (Dron, 2022). The breadth of the work will be illustrated through an overview of the growing catalogue of orchestrations using a gatherers, weavers, and augmenters taxonomy.

### References

Bennett, S., Lockyer, L., & Agostinho, S. (2018). Towards sustainable technology-enhanced innovation in higher education: Advancing learning design by understanding and supporting teacher design practice. British Journal of Educational Technology, 49(6), 1014–1026. https://doi.org/10.1111/bjet.12683

Bygstad, B. (2017). Generative Innovation: A Comparison of Lightweight and Heavyweight IT: Journal of Information Technology. https://doi.org/10.1057/jit.2016.15

Dron, J. (2022). Educational technology: What it is and how it works. AI & SOCIETY, 37, 155–166. https://doi.org/10.1007/s00146-021-01195-z

Ellis, R. A., & Goodyear, P. (2019). The Education Ecology of Universities: Integrating Learning, Strategy and the Academy. Routledge.

Illich, I. (1973). Tools for Conviviality. Harper and Row.

---


[//begin]: # "Autogenerated link references for markdown compatibility"
[paper-ideas]: paper-ideas "Paper Ideas"
[//end]: # "Autogenerated link references"