---
title: Building AI applications based on learning research
---
[GRAILE Seminar](https://www.eventbrite.com/x/621321217487/?keep_tld=1&internal_ref=social) - [Global Research Alliance for AI in Learning and Education](https://graile.ai/)

[Kristen DiCerbo](https://www.kristendicerbo.com/about-me) (Khan Academy) & Hassan Khosrav


## Abstract

The rush is on to build new applications of AI in education. However, before we rush blindly into the future, looking at the legacy of research in the field will help us build applications with a better chance of improving outcomes. This webinar will look at how decades of research help inform efforts to integrate the latest large language models into Khan Academy. You will get a behind the scenes look at how AI features were built into a platform used by millions of learners a year, and hear what is being learned from the rollout of these features to a small group of schools and districts.

### Related

- [World-class AI for education](https://www.khanacademy.org/khan-labs) - Khan Academy's AI web page
- [The amazing AI super tutor for students and teachers](https://www.ted.com/talks/sal_khan_the_amazing_ai_super_tutor_for_students_and_teachers/c) - Sal Khan TED talk on this work.
- [What is Khanmigo?](https://www.techlearning.com/news/what-is-khanmigo-the-gpt-4-learning-tool-explained-by-sal-khan) - brief article summarising some of this.
- [Khanmigo is great but NOT ready to tutor student](https://www.linkedin.com/pulse/khanmigo-great-ready-tutor-student-richard-tong/) - LinkedIn post from the chair of IEEE's AI standards committee reporting on his experience using Khanmigo.

## Summary and Reflection 

For just over 5 months Khan Academy have been working with OpenAI to integrate applications of large language models (LLMs) into Khan Academy's platform. Originally prompted by a [challenge from Bill Gates](https://www.gatesnotes.com/The-Age-of-AI-Has-Begun) to Open AI for its LLMs to pass AP Biology. A challenge which led OpenAI reaching out to Khan Academy. Khan Academy have leveraged this to integrate 

For me, Khan Academy's use of OpenAI's LLMs is a good example of gathering and weaving. In particular, strong example of how LLMs allow that gathering and weaving to move up a few layers of abstraction. For example, by integrating pedagogical knowledge into prompts (e.g. good tutor practices) so the LLM does this. In ways that aren't normally accessible either because the tutor isn't available or doesn't have the knowledge.

For example, the "Tutor me" mode in Khanmigo is [reportedly](https://www.linkedin.com/pulse/khanmigo-great-ready-tutor-student-richard-tong/) "very good at guiding the tutoring process by providing tailored scaffolding support, asking probing questions, prompting critical thinking". Arguably, because the work Khan Academy does on prompt engineering. In particular, prompting the LLM to act as a tutor and draw upon published research on tutoring practices (Graesser et al, 1995). Achieved by prompting the LLM with the academic reference.

Key to the performance of the LLM is the bespoke prompt engineering that is done by Khan Academy. A [prompt template](#prompt-template) was mentioned in the talk. For me a good example of how the gathering/weaving metaphor continues in the brave new AI world. Potentially, getting much easier to do more specific pedagogical scaffolding.


### Tasks 

- ChatGPT as a source for answers to "why should I care about this?"

	One example of something to help students/teachers in a school context - mathematics.
- Khan Academy if weaving more context into the use of ChatGPT
- Lesson builder to create lesson hooks etc and with prompt engineering added in
- Read the Graesser paper the type of research is being automated/fed into LLMs


## Notes

What's talked about here has been available for about 5 weeks. Still early day explorations.

### ChatGPT features

- Appears to be taking a more interview/discussion approach. 
- Khan Academy now has a couple of hundred staff.
- OpenAI has been in contact with Khan Academy. Using their AP biology questions to train OpenAI's models.
- ChatGPT costs money to run, hence these features are available to research partners and Khan Academy donors.

Aims 

- Get this to act as a tutor for students  
- ??
- Teacher assistant

[Khanmigo](https://www.khanacademy.org/khan-labs)
- chat/buddy 
- passes knowledge of current khan academy page to the LLM for various things
	- packaged as prompts to ChatGPT
	- e.g. act like a socratic tutor
	- don't give answer
- also passes in student mastery levels and the course currently in
- ponder if/how to expand the information that is being passed in e.g. student interest

Other features are giving debates, chats etc.

Story about a student confused about why Gatsby was staring at a green light and used the chat to ask the character

![](https://djon.es/assets/memex/sense/AI/images/gatsbyInterview.png)

Who then also acts as a general chatGPT

![](https://djon.es/assets/memex/sense/AI/images/gadsbyMath.png)

Teacher functionality

- Create a lesson hook
- Lesson objectives
- Co-create a rubric

![](https://djon.es/assets/memex/sense/AI/images/rubric1.png)

![](https://djon.es/assets/memex/sense/AI/images/rubric2.png)

### How to handle hallucination 

Particularly a problem with math, the language models aren't great at mathematics.

In maths, Khan will compare student answer to their answer to check/modify their thinking.  Will then ask the student to compare.

Khanmigo - also explicitly says it gets things wrong and explains why. Rationalised/explained to help students to understand how to interact with AIs

### How to write good prompts 

They've developed a <a id="prompt-template"></a>prompt template 

- Tell it role to play: socratic tutor, etc.
- Tell it who it's talking to: e.g. student 
- What activity are you doing 
- You should always...  
  - e.g. research on what good tutors do
  - what are the good features of a rubric
- You should never
  - don't give answers
- Examples

### Tutor models 

ChatGPT knows about the Graesser work on tutor models and that can be used as part of the prompt

![](https://djon.es/assets/memex/sense/AI/images/graesser.png)

## Risks, concerns, mitigation 

Safety and academic integrity: Teacher doesn't know what the student is saying to the LLM.  They constraint the interactions and also maintain a chat history. OpenAI has a moderation API that they use - but other languages?

Data privacy: 

- all data is anonymous going to OpenAI
- Agreement with OpenAI to not use the data to train the model 
- Though Kristen feels that this is somewhat a problem because it can't be used to improve the models

Diversity and diverse cultures - moving beyond US centric

- Khan Academy given under-represented districts access to free 
- Tax free/cost issues prevent them from making it available more broadly
- Also legal issues for each country
- OpenAI can respond in different languages 

Moderation API has 7 values it checks.

## Rough data and how's it going

- 4% of people thank Khanmigo
- Tutor on exercise page most used 
- Tell me a story used to be
- Tutor / story / debate
- Early use shows examples of boundary testing in terms of how students interact with ChatGPT

## Recommendations 

Technologists

- Jump in and experiment - MVP
- Leverage the prior research

Educators 

- Khan Academy as an AI in education course - collection of articles
- Jump in




## References

Graesser, A. C., Person, N. K., & Magliano, J. P. (1995). Collaborative dialogue patterns in naturalistic one-to-one tutoring. *Applied Cognitive Psychology*, *9*(6), 495--522. <https://doi.org/10.1002/acp.2350090604>