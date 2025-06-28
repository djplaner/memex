---
backlinks:
- title: Implementing number scrabble
  url: /memex/sense/Representations/implementing-number-scrabble.html
- title: Prompt engineering
  url: /memex/sense/AI/prompt-engineering.html
- title: AI
  url: /memex/sense/AI/AI.html
- title: First experiments with LLM APIs
  url: /memex/sense/AI/explorations/first-llm-api-experiments.html
title: prompt-engineering-for-educators
---
## Designing effective AI Prompts (for Primary and High School Teachers)

From Annesha Bakharia 

- [Slides](https://docs.google.com/presentation/d/1bv2oxc4aqMNpVGixzvJgv0xULlZW7rVD/edit#slide=id.p1)
- [Video](https://www.youtube.com/watch?v=5WbZqVtmDYs&t=1s) 
- [Github repo](https://github.com/aneesha/prompt_engineering)

![](https://djon.es/assets/memex/sense/AI/images/sampleTeacherPrompts.png)

### Resources

- [Should I use generative AI? What to keep in mind and on-going considerations](https://marekkowal.substack.com/p/chatgptchecks)
- [ChatGPT education mega prompts](https://drphilippahardman.substack.com/p/introducing-chatgpt-edu-mega-prompts
)

### Highlights 

- [ChatGPT to generate a mindmap on a teaching area using mermaid.js output](https://raw.githubusercontent.com/aneesha/prompt_engineering/main/mindmap.md)

![](https://djon.es/assets/memex/sense/AI/images/generateMindMap.png)

- [Example prompt to create a grammar tutor using ChatGPT](https://raw.githubusercontent.com/aneesha/prompt_engineering/main/equation_tutor.md)
- Pointer to [AutoGPT](https://autogpt.thesamur.ai/agi) tool to have multiple versions of ChatGPT write prompts to meet a goal
- [NoleJ.io - an AI course generation tool](https://nolej.io/)

## Prompt types 

- Chain-of-thought 
- Let's think step by step

## Prompt components 

- Persona 
- Task 
  - specific task information
- Audience 
- Format


## Prompt engineering for educators – making generative AI work for you

From Danny Liu

#### [educational-innovation.sydney.edu.au](https://educational-innovation.sydney.edu.au/teaching@sydney/prompt-engineering-for-educators-making-generative-ai-work-for-you/) ▪ Thursday, April 27, 2023, 12:00 AM

ChatGPT has received a lot of attention across numerous industries. Bill Gates, drawing on the recent advances in AI which include ChatGPT, proclaimed in late March 2023 that [the age of AI has begun](https://www.gatesnotes.com/The-Age-of-AI-Has-Begun), comparing it to the advent of the internet and mobile phones in terms of potential impact on society. The impacts of AI on education, he says, will be revolutionary. However, those of us ‘on the ground’ in higher education may have only come across AI in relation to how students could use it to write essays for them, or perhaps how AI might help to generate multiple choice questions.

In this extended post, I’d like to share practical examples of how generative AI like ChatGPT has the potential to be so much more, and show you how you can try these examples out for yourself. Many of these have been inspired by educators and others from around the world who have been experimenting with AI over the last few months, as well as evidence-based approaches in the learning sciences.

_Check out our other resources, such as the companion piece on [Prompt Engineering for Students](https://educational-innovation.sydney.edu.au/teaching@sydney/prompt-engineering-for-students-making-generative-ai-work-for-you/), and other [practical AI in education resources](https://educational-innovation.sydney.edu.au/teaching@sydney/ai-and-education/)._

Chatting is the new programming
-------------------------------

[![Flowchart showing the prompt leading to a model, leading to a completion](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-24-232217-300x105.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-24-232217.jpg)

Prompts, models, and completions in ChatGPT

But first, a few fundamentals. When you use tools like ChatGPT, you provide it a ‘**_prompt_**‘, which the software sends to a ‘**_model_**‘ (the actual AI), and the model then produces a ‘**_completion_**‘ which is shown to you through the tool. There are many models available, but the most powerful to date are called GPT-3.5 and [GPT4](https://educational-innovation.sydney.edu.au/teaching@sydney/gpt-4-is-here-what-is-it-and-what-does-this-mean-for-higher-education/), made by OpenAI.

The tool is chat-based, which means after the first completion, you can provide another prompt, receive another completion, and so on. The power of this prompt-completion-prompt-completion-… cycle is that you can **interact with the AI to improve upon its responses**. In each chat session, the prompt-completion-prompt-completion-… provides a ‘**_context_**‘ for the AI to work, so that it can draw from recent turns in your conversation.

Chatting with the AI is how you get it to produce responses for you. In essence, your chat prompt(s) are how you program the AI to do things for you. Instead of needing to write computer code, your written language is how you control the AI.

Prompting basics
----------------

Keeping this in mind, it follows that how you write prompts has an important influence on what kinds of responses you might get from the AI.

**There is no real magic to writing prompts**, but there are some general guidelines for ‘_prompting_‘ that seem to help the AI return more useful completions to you. OpenAI’s own [internal prompts](https://twitter.com/rez0__/status/1645861607010979878?t=yA_J4_LQZOsOc-UUFSP2Hw) seem to follow a similar structure recommended by [others](https://www.linkedin.com/posts/dr-philippa-hardman-057851120_chatgpt-for-educators-part-2-activity-7034429494937440257-WoLy/). One such structure is:

*   Role (act as…)
*   Task (summary of what the AI needs to do)
*   Requirements (what the completion needs to include, contain, be, etc)
*   Instructions (what the AI should do to act on the prompt)

We’ll see in the examples below how this **‘RTRI’ structure** plays out. This is by no means the only (or possibly even best) way to prompt, but it does seem to produce some meaningful completions. The most [important thing to remember about prompting](https://www.oneusefulthing.org/p/a-guide-to-prompting-ai-for-what) is to keep trying, and leverage the chat functionality to iteratively work with the AI to improve its completions.

ChatGPT? GPT-4? What do I use?
------------------------------

The examples below can be run through:

*   [ChatGPT](https://chat.openai.com/) (the free version, which runs the GPT-3.5 model),
*   [ChatGPT Plus](https://openai.com/blog/chatgpt-plus) (the paid version, which runs [GPT-4](https://educational-innovation.sydney.edu.au/teaching@sydney/gpt-4-is-here-what-is-it-and-what-does-this-mean-for-higher-education/), a much more capable model), or
*   [Bing Chat](https://www.bing.com/chat) in creative mode (which uses GPT-4 under the hood).

**Most of the examples below will run more effectively through GPT-4 instead of GPT-3.5.** You can use Bing Chat in creative mode to access GPT-4 for free.

How can generative AI improve learning and teaching?
----------------------------------------------------

### Supporting retrieval practice

One of the **most effective ways to learn something is to try and bring it out from your memory**. [Retrieval practice](https://www.learningscientists.org/retrieval-practice), as this process is called, helps learning by strengthening connections in memory. One of my favourite ways to study molecular biology as a student was to write biochemical pathways on a whiteboard, rub out parts of it, go for a walk, and come back and try to fill these in. Little did I know, I found this effective because of retrieval practice.

A standard approach to giving students activities for retrieval practice is the humble quiz. Generative AI can help you [generate draft questions quickly](https://www.linkedin.com/pulse/yes-chatgpt-can-answer-exam-questions-write-them-too-justin-shaffer/). It can even suggest feedback to provide to students. The prompt below asks AI to generate some of these for you. The prompt is colour-coded to demonstrate how role (blue), task (orange), requirements (green), and instructions (purple) come together. (You’ll also see that RTRI doesn’t have to be a strict pattern).

You are an expert business information systems instructor. Make 3 multiple choice questions that test second-year university students' understanding of the following topics: - Customer Relationship Management Systems - Information Security and Privacy - Business Process Management For each question, provide the correct answer. Then write feedback to students about the correct and incorrect options. Link the topics together in your feedback to help students connect ideas together. In your feedback, provide questions that encourage students to explore these ideas more themselves, instead of giving them the answer directly. 

[![Screenshot of prompt and completion from ChatGPT](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-26-234952-259x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-26-234952.jpg)

ChatGPT generating MCQs with feedback

The screenshot to the right shows the prompt and part of the completion with ChatGPT, using the GPT-4 model. You can see how it takes the prompt and provides questions with feedback, and the feedback encourages students to draw links between the different topics. This example also draws on another process called **[elaboration](https://www.learningscientists.org/elaboration), which involves making connections between different concepts to aid learning**.

If you already have questions written but need to generate feedback for students, try this simple prompt. Try spice up the prompt by asking ChatGPT to write the feedback in different ways.

Identify the correct option to the MCQ below. Write feedback for each of the options.

<Question stem>
<Options>

Often a criticism of MCQs is that they focus on recall, or lower level skills. **One approach to power-up your MCQs is to get AI to consider [Bloom’s taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)**. In a new chat session, first prime the AI with what Bloom’s taxonomy is:

What is Bloom's taxonomy?

Now that an explanation of Bloom’s taxonomy is in the chat context as part of the AI’s first completion, you can ask the second prompt a bit differently.

...
Make 3 multiple choice questions to Bloom's level 'evaluating' that test second-year university students' understanding of the following topics:
...

### Learning through analogies and concrete examples

**[Elaboration](https://www.learningscientists.org/elaboration) is an approach that promotes learning through making connections**, expanding on ideas, and applying concepts to students’ own experiences. The biochemistry teachers I learnt the most from came up with amazing analogies that helped to turn abstract concepts into tangible realities. With the help of AI, you can effortlessly **generate analogies to kick-start student thinking**.

[![Screenshot of ChatGPT prompt and completion about generating analogies.](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-001613-276x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-001613.jpg)

ChatGPT generating analogies.

Try the following prompt:

You are an expert tutor in university-level exercise physiology.

Come up with 3 creative analogies to explain the interplay between energy systems and cardiovascular responses to exercise, using analogies drawn from contemporary popular culture.

If you know your students have particular interests, you can modify this prompt accordingly. Perhaps you’d like the AI to generate analogies related to Tiktok videos, or car parking on campus, or the Super Mario movie. The analogies won’t be perfect – but that’s the beauty of analogies. **Ask student groups to critique the analogies and identify strengths and weaknesses**, and suggest additional analogies or extensions to the existing ones.

Another effective learning approach is to cover **[concrete examples](https://www.learningscientists.org/concrete-examples). This helps students to apply abstract concepts to reality**, increases motivation, and encourages them to draw links between different ideas.

[![Screenshot of ChatGPT prompt and completion to generate scenarios for discussion.](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-110643-300x288.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-110643.jpg)

ChatGPT generating scenarios.

Try the following prompt (and notice how the elements of RTRI are present, but interspersed):

Act as an expert in social psychology. I am teaching a class about cognitive biases that affect decision making. Give me 5 examples of real life scenarios where particular cognitive biases might be at play - include examples where 2 cognitive biases are present. Make the scenarios quite diverse. Write the scenarios as short stories involving businesses and their clients. Tell me which cognitive bias(es) are active and explain why.

You could easily turn some of these examples into fuller case studies by chatting with the AI. For example, you could provide a second prompt in the chat context:

Can you expand the first scenario into a few paragraphs, including dialogue between the people involved, and structure it like a case study?

### Seeing from different perspectives

Because the training data for these AI is extremely broad, they can often help to provide generated human-sounding opinions from a variety of perspectives. **These can then be used in class to kickstart conversation and critique**. For example, what assumptions and biases are present in these AI-generated perspectives? Where are the accuracies and inaccuracies? How do these compare to students’ own experiences considering their rich and diverse backgrounds?

For example:

Give 5 different perspectives on the Great Resignation from senior managers who are working in different countries with different work cultures. These perspectives need to demonstrate their insights into why their employees are quitting. Write these in the form of short interview quotes from the perspective of these managers. The quotes must subtly demonstrate how their own societal culture impacts on their decision making.

[![Screenshot of Bing Chat in creative mode with prompt and completion about different perspectives on the great resignation](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-115504-300x211.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-115504.jpg)

Bing Chat generating quotes from different perspectives

In the screenshot here, you’ll see that I’ve used **Bing Chat in ‘creative mode’**. The benefits of using Bing Chat are that it runs GPT-4 under the hood, is free and, importantly, is connected to the internet. The screenshot shows how Bing Chat searches for the great resignation and then produces its response.

After giving this prompt, you could ask the AI to analyse its own writing and elaborate with explanations. For example, you may want to follow up the completion to the above prompt with another prompt:

Explain why these perspectives stem from their cultural backgrounds.

### AI as a universal simulator

The inimitable [Ethan Mollick](https://www.oneusefulthing.org/) from the Wharton School in the US is a thoughtful and prolific proponent of the use of AI in education and across society. In a [recent post](https://www.linkedin.com/posts/emollick_ai-is-so-close-to-creating-a-universal-educational-activity-7047622757668253696-kAoQ), **he has suggested that generative AI could be a ‘universal simulator’**.

[![Screenshot of Bing Chat in creative mode with prompts and completions around a medical scenario](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-113407-300x184.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-113407.jpg)

Bing Chat creative mode running through a simulated scenario

Consider (or modify the green portions and try!) the following prompt:

I want to do deliberate practice about how to conduct bedside consultations in a large hospital. You will be my teacher. You will simulate a detailed scenario in which I have to engage in a patient consultation. You will fill the role of the patient or their family, I will fill the role of the doctor. You will ask for my response to in each step of the scenario and wait until you receive it. After getting my response, you will give me details of what the other party does and says. You will grade my response and give me detailed feedback about what to do better using medical consultation models. You will give me a harder scenario if I do well, and an easier one if I fail.

This brings together a few of the ideas we’ve discussed so far, giving students a safe and guided environment to practice applying their knowledge. From the screenshot, the AI takes your input and provides feedback and suggestions. Students may want to use this themselves, or you could run this as a class or group activity where students need to collectively determine a response that you then feed back to the AI and use to spark discussion.

### Planning for lessons

We’ve all been there – you’ve been given a new class to teach on an unfamiliar topic and don’t quite know where to start. AI can give you some ideas that you can then adapt; don’t just do exactly what it says, but **adapt this based on your own experience and knowledge as an educator**.

In order to prime the AI to think about things that will help students learn, try this starting prompt:

Explain why retrieval practice, elaboration, analogies, and active learning are useful for learning.

The AI will tell you about these approaches. This means that the explanation of these ideas and why they are useful for learning will now be in the context for this chat conversation. Next, you might want to provide it with a prompt like:

Act as an expert veterinary sciences educator. Design a 50 minute tutorial for university students who are learning about animal behaviour management in a clinical context. Design activities that leverage retrieval practice, analogies, elaboration, and active learning.

It will give you some ideas about learning and teaching activities you could run within this class, and will likely give you a schedule for these too. Again, don’t just do what it says – **use your expert human judgement to modify or ignore its suggestions**. If you’d like to get specific, you can also modify your prompt, or use follow-up prompts, to ask it focus on particular topics, for example.

### Suggesting topics for discussion

I struggle with creativity. If you’re in a similar boat and would like some ideas about how you can get students talking about a particular topic in class, you could ask AI to generate some discussion prompts.

The following prompt combines topics that your class needs to discuss, and **asks the AI to draw links between these and common student interests**. Of course, [derive these interests from what you know about your students](https://educational-innovation.sydney.edu.au/teaching@sydney/welcoming-students-with-sres/), so that the discussion starters can be tailored to their interests and experiences.

Come up with 5 examples of discussion prompts to get university students thinking about the key microeconomic concepts of supply and demand, elasticity, and utility. Base these prompts on the following topics which they are interested in:
- Social media influencers
- Climate change
- Casual work
- Parking on campus

Similar to the analogy example earlier, these examples can be a good starting point for exploration and critique in smaller discussion groups.

### Interleaving assistant

Here’s another [great idea from Ethan and Lilach Mollick](https://hbsp.harvard.edu/webinars/unlocking-the-power-of-ai). [Interleaving](https://www.learningscientists.org/interleaving) is the practice of interspersing different topics or concepts and drawing links between them in order to promote deeper learning. If you’re switching between topics, interleaving can help your students connect the previous topic to the current one.

[![](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-05-04-102928-261x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-05-04-102928.jpg)

Screenshot of ChatGPT prompt and completion to connect different biology topics

AI can help give some ideas about this. The prompt below first establishes a role for the AI and then asks it to suggest these connections:

You are an experienced biology instructor who understands key pedagogical approaches like interleaved practice. I am an instructor. Provide suggestions on how I can connect the previous topic of cell biology with the current topic of evolution. Provide activities that I could use in class. Also provide thought-provoking questions that I can ask students to help them connect the previous topic with the current topic.

One of the emergent properties of generative AI is its ability to be (or appear to be) creative. It can draw quite neat connections between even disparate topics.

How can generative AI improve assessment?
-----------------------------------------

Assessments are one of the key activities in higher education that will be most impacted by generative AI. We are all worried that students may use generative AI inappropriately to complete assessments (interestingly, [students also feel the same, and have some great ideas for us](https://educational-innovation.sydney.edu.au/teaching@sydney/students-answer-your-questions-about-generative-ai-part-1-assessments-and-their-future/)). But what if we, as teachers, could use generative AI to enhance assessments so that they are more realistic, authentic, cognitively challenging, and supported through improved feedback? A [recent viral Reddit thread](https://www.reddit.com/r/ChatGPT/comments/12o4qaw/i_delivered_a_presentation_completely_generated/) discussed how students used GPT-4 to generate a master’s level presentation and achieved full marks. Notably, the students (and the ensuing discourse this thread received) highlighted that the key issue being that the presentation was “about a topic quite frankly we couldn’t care less about”. So, instead of trying to ‘AI-proof’ assessments, **can AI help us to uplift our approach to designing and delivering assessments and feedback that students care about**?

### Suggesting creative assessment ideas

Students are more likely to be motivated by, and less likely to cheat on, assessments that they find relevant. Academic integrity also improves when students feel a stronger connection to their teachers and to the assessment. AI might be able to help here.

[![Screenshot of ChatGPT prompt and completion about a media and communications assignment](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-140118-254x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-140118.jpg)

ChatGPT generating creative ideas for assessments

The prompt below asks AI to generate assessment ideas for a set of learning outcomes. The prompt also asks for the assessments to encourage gradual work; in the era of generative AI, many people have been promoting the idea of ‘assessing the process not the product’.

Suggest 5 creative assessment ideas that can assess the following learning outcomes in a university-level media and communications course. Make the assessment meaningful for students, encourage gradual work towards the final product, and use non-essay formats.

LO1. demonstrate a broad yet nuanced understanding of introductory theories in media studies
LO2. demonstrate how to apply these theories to ‘reading’ media texts
LO3. critically evaluate the usefulness of theories in addressing questions about media production and reception
LO4. demonstrate skills in academic writing and research
LO5. demonstrate personal and intellectual autonomy through assessment and class work.

[![Screenshot of ChatGPT follow-up prompt and completion to expand on an assessment design to suggest scaffolding techniques](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-142832-253x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-142832.jpg)

ChatGPT following up on an assessment design it suggested, explaining how students might learn from the process

Once the ideas are generated, leverage the chat to follow up. For example, ask it to expand upon particular assessments and explain **how students might most effectively learn from the process of completing the assessment**:

Assessment 2 sounds good. How can this assessment be staged so that students can most effectively learn in the process of completing the assessment?

The AI will generate some ideas that help you scaffold the assessment. Its ideas will by no means be perfect; you should always consider these with your human expertise and adapt as appropriate.

### Generating exemplars to demonstrate quality standards

As part of helping your students understand the quality of work you expect, it’s important to provide examples. These ‘[exemplars](https://doi.org/10.1080/02602938.2021.2011134)‘ are critical in the context of standards-based assessment, as they help to demonstrate quality at different levels (e.g. HD, vs CR) of achievement. Importantly, **exemplars also help students develop their internal ability to judge quality**, and help them to monitor their own progress towards well-demonstrated standards.

Try a prompt like the one below. Make sure you insert your assessment description and the performance criteria you want (i.e. use a separate prompt for HD, another for CR, etc).

Write a 300 word reflection based on the following \*\*assignment parameters\*\*. Ensure your reflection addresses achievement at the level described in the \*\*performance criteria\*\*.

## Assignment parameters

<paste in your assignment parameters>

## Performance criteria

<paste in performance criteria, such as from a rubric, for a particular achievement level>

After the AI generates the exemplars, make sure you go through and edit what it creates to match what you expect from your students at different levels of achievement. Consider using these exemplars in class as well, where you could hold discussions where students use a rubric to grade an exemplar and gain a better understanding of the expected standards.

### Drafting rubrics

Don’t have a rubric? AI could help here too. Rubrics are grids that help to explain what different levels of achievement look like against the marking criteria. They are usually presented in table format, with rows for criteria (e.g. analysis of sources, use of literature, critique of argument, etc) and columns for standards (e.g. HD, DI, CR, PS, FA).

[![Screenshot of ChatGPT prompts and completions, where ChatGPT asks the user more information](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-161206-254x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-161206.jpg)

ChatGPT prompting the teacher to assist in generating a rubric

Try the following prompt, adapting it as needed to suit your topic(s):

Act as an expert higher education academic and writer of assessment rubrics.

I need to write a marking rubric for a second-year university-level assessment where students (pre-service teachers) need to critique the use of technology in high schools. You need to help me generate the rubric rows (which are the criteria), and the columns are the various standards (from high distinction, to distinction, to credit, to pass, to fail).

Ask me questions to help me write a strong rubric. Ask one question at a time, wait for my response, and ask me the next question. After I have answered your questions, produce a draft rubric for me.

[![Screenshot of a rubric table generated by ChatGPT](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-161326-292x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-161326.jpg)

The rubric generated by ChatGPT

This prompt will have the AI ask you a few questions to find out more about what you need, before generating a draft rubric for you. **This is an interesting example of a prompt because it asks the AI to ask _you_ follow-up questions**. The rubric that it generates is by no means something I would immediately use for students, but it gives me things I can think about and improve upon.

With anything generated by AI, you’ll need to use your human expertise to amend the content that it generates, but it will be a good starting point – better than a blank page!

### Improving feedback for students

A key part of assessment is the learning that happens through feedback. Feedback needs to be understandable by students and help them know how and where they can improve. Personally, I struggle with a bit of feedback anxiety and can find it tricky to phrase feedback in the right way that is most supportive for student learning.

[![Screenshot of ChatGPT prompts and completions to improve feedback](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-163710-254x300.jpg)](https://educational-innovation.sydney.edu.au/teaching@sydney/wp-content/uploads/2023/04/Screenshot-2023-04-27-163710.jpg)

ChatGPT helping to suggest rephrasing for feedback

The prompt below has AI act as a feedback writing assistant:

Act as an expert educator in higher education.

I will give you a summary of notes for feedback to students about an assignment. I want you to expand these into a paragraph or two of feedback to students. The feedback needs to be encouraging and help students understand how they can move forward.

Base your feedback on the \*\*assignment brief\*\* as well as the \*\*marking rubric\*\*.

Acknowledge that you understand this and have received the assignment brief and rubric. Wait for me to provide the summary of notes. When I provide the summary, you should reply with the expanded feedback. Keep your feedback a maximum of 2 paragraphs.

## Assignment brief:

<paste the assignment instructions here>

## Marking rubric:

<paste the marking rubric here, i.e. what the descriptor is for each criterion and standard>

The screenshot shows the AI’s first completion in response to the above prompt, and then my summary of notes as the second prompt, and then its completion which contains the re-phrased feedback. The AI is able to take words from the assignment brief and marking rubric, and combine it with my own words. I would then take this rephrased feedback and rework it before providing it to students.

Other tips
----------

Some other final tips that might help you to modulate the output from ChatGPT and similar AIs.

*   Use [style and tone modifiers](https://twitter.com/realchasecurtis/status/1642516833382068227?t=NwFK1fNlush4LxT-dfI9_A). For example, after it has given you a completion, prompt: “Rewrite the above in a <style> style with a <tone> tone.” Some styles you might want to try might include: Descriptive, Persuasive, Narrative, Technical, Academic, Creative, Informal, Formal, Dramatic. Some tones you might want to try include: Serious, Confident, Doubtful, Sympathetic, Optimistic, Pessimistic, Aggressive, Playful, Sincere.
*   [Encourage its creativity](https://www.linkedin.com/feed/update/urn:li:activity:7048841876979781632/). Add words like ‘uncommon’, ‘novel’, ‘unconventional’ to your prompt, such as, “What are 5 unconventional things that a first year undergraduate would say after their first week at uni?”
*   If you encounter a prompt that the AI refuses to return a completion for, try asking it to ‘imagine’ that it is in a particular role. You can also explain the educational reasons why you need the prompt answered. This often helps to get past its initial refusal.

Tell me more!
-------------

---

Clipped on Saturday, May 6, 2023, 2:05 PM