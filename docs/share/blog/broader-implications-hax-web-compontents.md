---
title: Broader Implications Hax Web Compontents
---
## Broader implications: the NGDLE and the VLE 

The rise of the idea of the Next Generation Digital Learning Environment (NGDLE) is a recognition that no single system can meet the requirements of learning and teaching. Instead, there needs to be an ecosystem of components available that “allow individuals and institutions the opportunity to construct learning environments tailored to their requirements and goals” (Brown et al., 2015, p. 1). This "lego approach" to constructing an ecosystem of technologies requires standards that specify how the lego pieces connect. Otherwise there will be a disconnected user experience.

For institutions the standard de jour is [Learning Tools Interoperability (LTI)](https://en.wikipedia.org/wiki/Learning_Tools_Interoperability). And it sort of works. A lot of educational technology vendors and their tools (sort of) support it. One of the problems is that the individual "blocks" in LTI lego tend to be individual applications. You use LTI to connect Blackboard with the portfolio system. 

LTI typically doesn't support and/or get used for the what was originally proposed as a model for the NGDLE, the mash-up.
> the model for the NGDLE architecture may be the mash-up. A mash-up is a web page or application that “uses content from more than one source to create a single new service displayed in a single graphical interface (Brown et al., 2015, p. 3)

Being based on standard web standards and implemented by all modern web browsers web components appear to provide the best approach to supporting the mash-up model of the NGDLE. As illustrated above (in a not very educational example) I've been able to combine content and services from various sources into a single interface. Creating web components - like those produced by the folk at Penn State University when developing HAX and the magic script - enable sharing and reuse. 

Web components provide lego blocks at a smaller scale than LTI. And perhaps enable the curation of more seamless learning environments.

### Magic script as permeable membrane

Entropy will kill a closed system. An open system is needed and web components provide such an open system. But institutions also tend not to want a system that is too open. For many reasons, some good. They'd like to be able to define a permeable membrane that enables them to specify how open the system is.

The [magic script approach](https://dev.to/btopro/uwc-part-3-the-magic-script-122a)  provides a permeamble membrane. It only recognises the web components specified in [the JSON registry file](https://cdn.webcomponents.psu.edu/cdn/wc-registry.json). Suggesting something for the institution to control. (Though it wouldn't be difficult to create my own registry and point the script there)

### Unbundling as being platform agnostic

The folk behind this are using an [unbundled approach](https://dev.to/btopro/part-1-how-penn-state-unbundles-web-components-for-cdn-deployments-20di) to web components.

HAX promises to transform "authorship so faculty can focus on instruction rather than HTML in order to accurately represent their expertise" ([Ollendyke, 2018](https://psu.app.box.com/s/gk6013odcl3115j3ibfzudj3bqar059v)). **Card and content interface** do something similar but take a different approach...

Something here about breaking out of the LMS...but what about my work with tweaks and links to the design principles of CASA and/or my ISDT