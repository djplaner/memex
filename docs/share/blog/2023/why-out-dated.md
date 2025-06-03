---
title: No title found
---
```toml
post_title="Why are Universities digital development practices so out-dated? (especially when it comes to L&T)"
layout="post"
published=false
id=18400
link="https://djon.es/blog/2023/07/14/why-out-dated/"
category="casa"
img_base_url="https://djplaner.github.io/memex/share/blog/"
```

Dave Farley and Kent Beck discuss stuff including why waterfall is making a come back, never really went away.  My interpretation is due to there being different epistemic views (e.g. people doing wireframe , management etc) and management techniques that can't handle gathering/weaving.



In his post - [*How do we design the need for design?*](https://beerc.wordpress.com/2023/07/10/how-do-we-design-the-need-for-design/) - Col muses on challenges involving learning, teaching, and digital technology in learning and teaching. The post closes with this

**Laurillard tool quote**

Perhaps the question here is an organisational question more than a philosophical or technology-related question; how do we shift our thinking away from heavy-weight approaches to technology to light-weight, generative, and perhaps federated technology (Bygstad, 2017)? I think we have some understanding of the problem, but how do we move beyond the [dogma](https://www.merriam-webster.com/dictionary/dogma) of the status quo?

(note: Col and I are both writing in the context of Australian higher education)

I'm wondering if a better question is why that shift hasn't happened already? Or perhaps it's a useful question for identifying how to encourage the shift?

Why do University digital development practices remain so out-dated? Given all the talk of digital transformation from institutional senior and digital leaders, why do their institutions continue to not have adopted industry best practice? Especially given...

## Current industry practice is lightweight

When I look at industry practice I see two major (recent) trends: DevOps etc; and, Citizen Development. Both of these major trends represent shits from heavy-weight to light-weight and generative approaches.

[DevOps](https://www.atlassian.com/devops)  arose from the need to close the gaps between the development and operations teams within digital/IT teams. It lead to practices such as as [continuous integration, delivery and deployment.](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment) All focused on increasing the agility of IT teams capability to respond to organisational and user needs. [Team topologies](https://djplaner.github.io/memex/sense/computing/team-topologies) is the one of the more recent iterations on this work and comes with the tag line "Organizing business **and** technology teams for **fast** flow".

The other trend - citizen development - must be important given the push from [various large scale vendors](https://www.microsoft.com/insidetrack/blog/citizen-developers-use-microsoft-power-apps-to-build-intelligent-launch-assistant/) and [big consulting firms](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjpsLKln4WAAxWMbWwGHXo3BkgQFnoECAwQAQ&url=https%3A%2F%2Fwww.gartner.com%2Fen%2Finformation-technology%2Fglossary%2Fcitizen-developer&usg=AOvVaw0RwqV7NceZDoTtYidhQIUm&opi=89978449). Even [the Project Management Institute](https://www.pmi.org/citizen-developer/) recognises the value and place of citizen development. It arose from organisations finding that they didn't have enough IT professionals and software developers to keep up with the demands of digital transformation (Binzer & Winkler, 2022).

## There's evidence of this practice in higher education

DevOps is increasingly being used in Universities. I've (very limited) first hand experience of using a university dev ops platform (Microsoft). Professional bodies representing university IT professionals have communities focused on devops. For example, [CAUDIT (Australia)](https://caudit.edu.au/dev-ops-community/) and [EDUCAUSE (US)](https://connect.educause.edu/community-home?CommunityKey=12647590-8d4e-41d9-8332-d437c98b22d2).

As for citizen development, any university that's adopted Microsoft 365 has made available Microsoft's citizen development tools (PowerBI etc). Above and beyond that numerous universities are experimenting with Robotic Process Automation (RPA) platforms - a particular type of citizen development. The following image includes logos from Australian Universities with such projects early in 2023.

So the shift has happened? It has,.....

[![Headline from Gartner group predict world-wide spending on RPA will reach $2.9Billion in 2022. Along with logos of Oz universities with RPA programs](https://djon.es/blog/wp-content/uploads/2023/07/Screenshot-2023-07-14-150127-300x78.jpg)](https://djon.es/blog/wp-content/uploads/2023/07/Screenshot-2023-07-14-150127.jpg)

## But not in learning and teaching

Dron Blackboad and ASCILITE template paper

As Col's original post suggested this shift to more lightweight approaches isn't overly visible in learning and teaching.

All of the RPA projects illustrated in the image above have a primary focus on applying RPA to improve administration processes ([for example](https://www.uipath.com/resources/automation-case-studies/university-of-auckland)).

The learning management system remains the core digital L&T platform in higher education. One of the more popular LMSs is Canvas. Canvas' primary tool for organising content in a course is [the module](https://www.instructure.com/en-au/resources/blog/how-use-modules-build-courses-canvas?filled). For 8 plus years it has been known that there are significant limitations with the functionality of Canvas' module (e.g. [one](https://community.canvaslms.com/t5/Canvas-Instructional-Designer/Too-many-Modules-Options-for-resorting-structuring-content/td-p/55983), [two](https://community.canvaslms.com/t5/Idea-Conversations/Modules-within-Modules/idi-p/357681/page/2), [three](https://learntech.medsci.ox.ac.uk/wordpress-blog/a-dashboard-view-of-modules-in-canvas/) etc.). Other Canvas features have similarly long-term limitations that remain unfixed.

The community of Canvas users have a [long history of producing userscripts](https://community.canvaslms.com/t5/forums/searchpage/tab/message?advanced=false&allow_punctuation=false&q=userscript) to address these limitations. Institutions appear not to be aware of these.

Begging the question

## Why are university L&T digital development processes so out-dated?

What follows is some early answers based on experience and what I'm currently reading.

### **Digital skills shortage? Don't think so.**

Australian universities are struggling with recruiting and retaining skilled IT staff. e.g. A [CAUDIT webinar](https://caudit.edu.au/events/talent-recruitment-and-retention/) on the topic. Perhaps that's the reason for interest in RPA in Oz universities? After all citizen development is supposedly a response to the skills shortage?

### **Limited digital fluency of teaching staff? Don't think so**

For numerous years the digital illiteracy of teaching staff has been identified as a significant limitation on various forms of digital transformation (e.g. [the 2014 Horizon report listed it as #1](https://djon.es/blog/2014/09/12/you-want-digitally-fluent-faculty/)). But on the other hand at least some of the people in the Canvas community developing userscripts and other workarounds [are teaching staff](https://oudigitools.blogspot.com/2020/02/lms-privacy-and-purpose-limitation.html).

[![You want digitally fluent faculty? by David T Jones, on Flickr](https://farm4.static.flickr.com/3865/15025763858_58eea9f20c.jpg "You want digitally fluent faculty? by David T Jones, on Flickr")](https://www.flickr.com/photos/david_jones/15025763858/)

### Low code (citizen development) and the Law of Requisite Variety

### __somethign about orchestrating higher level applications__

_using LTI isn't enough_

[Setting up Sway for interactive orals](https://sway.office.com/8Sm1OBn58tg4zsU1?loc=swsp)..

### **Limited organisational epistemic fluency? Maybe, but how useful?**

## References

Binzer, B., & Winkler, T. J. (2022). Democratizing Software Development: A Systematic Multivocal Literature Review and Research Agenda on Citizen Development. In N. Carroll, A. Nguyen-Duc, X. Wang, & V. Stray (Eds.), *Software Business* (pp. 244--259). Springer International Publishing. [https://doi.org/10.1007/978-3-031-20706-8\_17](https://doi.org/10.1007/978-3-031-20706-8_17)