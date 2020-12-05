# Peak consistency in Digital Education 

Consistency is the new black for digital education. Some have even argued that it is "key in online learning" (Scutelnicu, Tekula, Gordon, Knepper, 2019). That it is the #1 thing that students want ([Sankey, 2018](https://www.slideshare.net/michaelsankey/online-learning-transformation)).

I'm not a fan. Proponents claim that consistency is not sameness. My problem is that consistency is also not quality. 

Given the diversity inherent in learning, learners, teachers and what is being learned - listen to Dede's (2008 pp. 57-58) ["sleeping, eating and bonding" metaphor](https://djon.es/dede.mp3)) - any attempt to gain consistency in learning and learning environments limits pedagogical quality (see the [[reusability-paradox]]). Further limits on quality arise from the ways in which institutions attempt to implement (and police) consistency.

I'm concerned we're heading for peak consistency. That the tools and methods that are increasingly dominating institutional approaches are enshrining this push for consistency. That this push for consistency devalues and at worse ignores the need for variation to respond to diversity. Largely because the push for consistency is easier than figuring out how to deal with diversity and achieve quality, rather than consistent, learning and teaching.

- Institutionalisation something creates inertia which makes it hard to change
- That inertia comes from a variety of places

To explore this the following touches on some history of consistency, some of the practices driving increases in consistency, indicators of trouble, and an alternative.
## Second generation distance education: When consistency was king

My start in higher education was at a dual-mode university in the early 1990s. We taught courses on-campus and via second generation distance education. Second generation distance education involved an industralised approach to the design and production of study material packages that were mailed out to students. Students who never set foot on a campus and rarely talked directly to another student or teacher. 

Teachers designed the study materials, sometimes with the help of a team. A central organisational unit produced and distributed the study materials. A key role for that central unit was ensuring consistency and improving quality. [Dekkers and Kemp (1995)](https://books.google.com.au/books?hl=en&lr=&id=OfWfHcUmbnYC&oi=fnd&pg=PA311&dq=kemp+dekkers+distance+education&ots=gB94qN_8jG&sig=qpY9IQ2H4fwrongl-xpc6jWPLSs&redir_esc=y#v=onepage&q=kemp%20dekkers%20distance%20education&f=false) describe the thinking that went into the production of this study material. 

Dekkers and Kemp were senior leaders in the unit that produced and distributed the study materials I produced. Their chapter (Dekkers and Kemp, 1995) raises an issue that was a concern to them in the mid 1990s. They note that technologies emerging at the time enabled the development of "learning materials to suit a range of learner settings, styles and other individual requirements" (p. 313). Their concern was that the material developed with these technologies gave little thought to "legibility, readability and, importantly, how the materials will be used" (p. 313). Instead, these materials were design on the basis of "the develoepr's own beliefs about what consistitutes 'good' typographical layout" (p. 313).

The solution adopted at my institution (and I assume elsewhere) was the adoption of consistent typographical standards informed by research. Dekkers and Kemp (1995) provide a long table outlining these typographical standards. Standards that were enforced by the industralised approach inherent in second generation distance education. Teachers provided the raw content for the study material. The distance education unit applied the research informed typographical standards to transform those raw materials into consistently legible and readable study materials.

Consistency wins. Diversity hits back.

The following is code written in the [Prolog programming language](https://en.wikipedia.org/wiki/Prolog) (taken [from this page](https://cse.sc.edu/~ahein/330/example.html)). In the early 1990s I was tutor in a Machine Intelligence course using Prolog taken by on-campus and distance education students. A few weeks into the course there was problems. Distance education students were complaining that none of the programs in the study material would run when they entered them into their computers.

A problem caused by the research informed typographical standards and their consistent application to all materials.

```prolog
main :-
    nl,
    write('>   Enter a selection followed by a period.'), nl,
    write('>   1. Run a query'), nl,
    write('>   2. Exit'), nl, nl,
    read(Choice),
    run_opt(Choice), main.
```

One of the typographical standards was, thou shall not use single quotes. All quotes had to be double. Hence the desktop publishers/copy editors in the distance education unit would automatically change all single quotes in provided study material to double quotes.

They forgot to tell the makers of the Prolog programming environments that they shouldn't be using single quotes.
## The rise of online learning: When diversity was king

The rise of online learning through the 1990s and 2000s killed second generation distance education. Mainly because it offered the opportunity for institutions (i.e. senior leaders of those institutions) to save money. Online learning meant that the people, resources and infrastructure created for industralised distance education were surplus to requirements.  Technologies like the course management system (CMS aka LMS) were seen to enable teachers to finally achieve what was foreshadowed by Dekkers and Kemp (1995) to develop "learning materials to suit a range of learner settings, styles and other individual requirements" (p. 313). Sure there would be a need for some change management, support and training but we could remove the barrier between learner and teacher.

We all know how that worked out.

## Standards, templates and learning - re-inserting consistency


## The return of homogenisation - learning design

__hark back to the reference_  consistency returned. More design.

Perhaps MOOCs played a part. For a time, offering a course as a [xMOOC](https://en.wikipedia.org/wiki/Massive_open_online_course#cMOOCs_and_xMOOCs) was a "strategic priority" (aka [FOMO](https://en.wikipedia.org/wiki/Fear_of_missing_out)). This meant resourcing that enabled design teams working together to fit a particular xMOOC model. A model often built into the platform the MOOC was offered on. MOOC platforms tended to be more explicit about their focus on a particular set of affordances. For example, at a more technical level, the [Future Learn design system](https://design-system.futurelearn.com/). At the same time there's been increased adoption of activity-based learning design approaches such as [ABC Learning Design](https://abc-ld.org/). More recently, there's been [talk about the value](https://www.youtube.com/watch?v=iBU76mlA0_w&feature=youtu.be) gained from combining activity-based learning design and design systems. Approaches that provide a consistent language and focus for effort to address the difficulty of designing digital education. 

## The return of homogenisation - sterile technologies and aping social media

The web-based LMS of the 90s/00s were generative technologies, as defined by Zittrain (2008). Technologies that could - almost entirely due to their use of generative web technologies (e.g. Javascript, CSS etc) - be modified by a broad array of people in response to specific needs. It required some knowledge of those technologies but it was fairly widely spread and was done (e.g. Abhrahamson & Hillman, 2016; [Jones, 2019](https://djon.es/blog/2019/08/08/exploring-knowledge-reuse-in-design-for-digital-learning-tweaks-h5p-constructive-templates-and-casa/); Plaisted & Tkachov, 2011). As Zittrain (2008) points out generativity can be a plus and a minus. For every effective customisation of an LMS, there's some horrendous combination of Comic Sans, poor colour choices, blinking text, poor contrast backgrounds, paragaphs of bolded text, and some Javascript/CSS that breaks something.

The new generation of digital education systems are increasingly more sterile. Blackboard Ultra explicitly prevents the use of web technologies like HTML, CSS and Javascript. To ensure that you can't negatively impact the mobile-first, responsive, simpler, and stream-based activity design of Ultra. Similarly, it [removes the choice teachers](https://www.jasonrhode.com/my-initial-thoughts-on-blackboards-ultra-new-learning-experience-lms) may have had around how to structure their choice. Apparently aiming for more a Facebook/social media interface than an open web interface.

At the same time, the rise in Australian Higher Education of Microsoft Teams reinforces this move from the web to social media. The move to becoming like social media 

... Garden and the Stream https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/

But increasingly consistnecy is baked into the technology

## The return of homogenisation - cost and strategy

Point to the systems blog post.  The increasing centralisation linking to homogenisation

Mention about course profile systems, standards, etc other organisational issues

## The return of homogenisation - A paucity of software develop(ers|ment)

Move to cloud systems meant we don't employ software developers. We employ people that explain how to use cloud services and maybe people to stich them together at the back end.

People solving specific institutional tasks by writing software are disappearing.



## Problems with consistency - learning and teaching is diverse and complex

__quote the fast food guy__

introduce the diagram from the 2020 paper and talk about the need to change

Prolog problem (hark back to above mention)

Bearman et al (2020) argue that approaches to encourage consistency are complex interventions that have plusses and minuses. That the benefits provided come at a cost. For example, focusing on following the common micro pattern of learning activities (idea, activity, discussion) led to an overly atomistic design where some learners felt they lost the big picture relevance of what they were learning. 

Another example arises from the Future Learn platform's explicit decision to ape social media style discussion which "tended to enable information sharing but not critical thinking within group interactions" (Bearman et al, 2020, p. 10)

There is no silver bullet.

## Problems with consistency - workarounds

Talk about these as evidence of the model

## Problems with consistency - aping the wrong thing (social media)

The spaces quote from the redesigning internet podcast

## Peak homogenisation?

The homogenisation above is driven by 

- aping a successful social media
- aping organisational practices (e.g. strategy etc)

Giving into fast thinking, rather than engaging with slow.

Because it requires effort. I worry that we wont stop climing the peak of homogenisation until we reach the top.

I wonder what the tumble down the other side will look like?

## Is there an alternative?

Almost 10 years ago Morris and Hiebert (2011) identified three features of a solution that would solve the 
> One reason that jointly created products can effectively help to solve a profession’s problems is that the knowledge used to build the products is harvested from participants across the system, participants who likely possess different kinds of knowledge.

_There are other links between Bearman and the work of Morris and Hiebert_

Bearman et al (2020, p. 10)
> review of learning design patterns post teaching is critical

IN Bearman's cascade model each level is an opportunity to "take account of the complex problems introduced previously"

> Designers at each level should take account of the existing tensions but also leave enough room for the designers of the next level to customise a solution to a specific circumstance.

Bearman suggest that centalised pattern design could be usefully conceptualised as providing an opportunity for teachers to create their own design.  Suggesting the pattern design should be **looser rather than tighter**


## References

Abhrahamson, A., & Hillman, D. (2016). Cutomize Learn with CSS and Javascript injection. Presented at the BBWorld 16, Las Vegas, NV. Retrieved from [https://community.blackboard.com/docs/DOC-2103](https://community.blackboard.com/docs/DOC-2103)

Bearman, M., Lambert, S., & O'Donnell, M. (2020). How a centralised approach to learning design influences students: A mixed methods study. *Higher Education Research & Development*, *0*(0), 1--14\. <https://doi.org/10.1080/07294360.2020.1792849>

Dede, C. (2008). Theoretical perspectives influencing the use of information technology in teaching and learning. In J. Voogt & G. Knezek (Eds.), *International Handbook of Information Technology in Primary and Secondary Education* (pp. 43--62). Springer.

Dekkers, J., & Kemp, N. A. (1995). OPEN AND DISTANCE LEARNING. *Open and Distance Learning Today*, 311.

Morris, A. K., & Hiebert, J. (2011). Creating Shared Instructional Products: An Alternative Approach to Improving Teaching. *Educational Researcher*. <https://doi.org/10.3102/0013189X10393501>

Plaisted, T., & Tkachov, N. (2011). Blackboard Tweaks: Tools for Academics, Designers and Programmers. Retrieved July 2, 2019, from [http://tweaks.github.io/Tweaks/index.html](http://tweaks.github.io/Tweaks/index.html)

Scutelnicu, G., Tekula, R., Gordon, B., & Knepper, H. J. (2019). Consistency is key in online learning: Evaluating student and instructor perceptions of a collaborative online-course template. *Teaching Public Administration*, *37*(3), 274--292\. <https://doi.org/10.1177/0144739419852759>

[//begin]: # "Autogenerated link references for markdown compatibility"
[reusability-paradox]: ../../sense/Bricolage/reusability-paradox "Reusability Paradox"
[//end]: # "Autogenerated link references"