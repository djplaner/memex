---
title: MAT081C Planning for unit 1 - statistical investigation
type: "note"
tags: statistics, teaching-mathematics
---

See also: [[mat081c-2024]], [[statistics]]

Where I'll start my more detailed planning for my version of the unit.

## Lessons

- [[MAT081C-2024-U1L1|Lesson 1 - You, Mathematics and this class]]

### Content and pedagogy resources

- [TIMES - Data investigation and interpretation - year 8](http://amsi.org.au/teacher_modules/Data_Investigation_and_interpretation8.html)
- [M1Maths statistics](https://m1maths.com/im-statistics.html)
- [MathisFun data](https://mathsisfun.com/data/index.html)
- [Mathematics hub - Year 8 statistics](https://www.mathematicshub.edu.au/planning-tool/8/statistics/)
- ?? advice/resources on conducting investigation
- [NZ UoW statistical investigation](https://nzmaths.co.nz/statistical-investigations-units-work)
- [Vocabulary of statistics](https://open.ocolearnok.org/psycstats/chapter/chapter-2-vocabulary-of-statistics/)
- [Simple random sampling](https://www.investopedia.com/terms/s/simple-random-sample.asp)

Images 

- [xkcd selection bias](https://www.explainxkcd.com/wiki/index.php/2618:_Selection_Bias)

Misconceptions

- [Samples and sampling (top drawer)](https://topdrawer.aamt.edu.au/Statistics/Misunderstandings/Misunderstanding-samples-and-sampling)

#### Quotes

Aaron Levenstein:
>    “Statistics are like a bikini. What they reveal is suggestive, but what they conceal is vital”.

#### Specific resources

Steam and leaf plots

- [interactive stem and leaf plot generator](https://jeroenjanssens.com/stem/) - simple textarea, put in data and generates a basic stem and leaf plot - [gist](https://gist.github.com/jeroenjanssens/6395842) has the code
- [Khan academy](https://www.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/a/stem-and-leaf-plots-review) review page has some detail and offers a collection of questions testing ability to read a stem and leaf plot


## Driving question

Possibilities

- **How do we know if someone is lying with data?** 
- How can we make better data-informed decisions?  
- How do we use data to make better decisions?  
- What decisions are important to me?

Search for examples

- Which toothpaste should I buy?
- illustrate types of decisions that might need making

## Terminology

[Art of smart - list of cogntive verbs](https://artofsmart.com.au/study/qcaa-cognitive-verbs-list)

| Term | Definition |
| --- | --- |
| Plan  |  knowledge utilisation |
| Conduct | To organise and carry out action |
| Investigate | Carry out research or a formal inquiry to uncover facts and draw new conclusions about data and information |
| Analyse | Examine/consider something for the purpose of finding meaning or identifying similiarties or differences |
| Report | |
| Compare | Recognise similarities and differences & identify their significance |
| Recognise | Identify features of information from knowledge of appearance or character |
| Solve | To work out the answer or solution to a problem |
| Use | To apply knowledge or rules to put theory into effect |

## Planning

- Driving question - Can I use this data to make a meaningful comment on a more general situation?
- _Question_ [ ] Can the student survey from the first lesson be used as an exemplar?

    - What type of data source is it?
    - What types of variables are there?
    - Draw on Likert styles from other similar surveys and use them to explore bias?

- _task_ [ ] Explore use of Australian Census data in the region as practical example/data source

    - [Census site](https://www.abs.gov.au/census)
    - Next census in [2026](https://www.abs.gov.au/census/2026-census-topic-review), last in 2021 on [this topic list](https://www.abs.gov.au/census/find-census-data/census-data-topic)
    - [2021 students data](https://www.abs.gov.au/articles/education-australia-abc-bs-and-cs) - some nice graphs
    - [PISA Oz students not trying](https://www.theguardian.com/australia-news/2024/jan/12/nearly-80-australian-students-say-they-didnt-fully-try-in-latest-pisa-tests)
    - [JJJ hottest 100 kaggle dataset](https://www.kaggle.com/datasets/mijames/jjj-hottest-100) (tsv file)
    - [Better intersections dataset](https://betterintersections.jakecoppinger.com/about) - includes articles researching the problems arising from lengthy waits at intersections

        - [Guardian article](https://www.theguardian.com/australia-news/2018/sep/09/placebo-buttons-australian-pedestrians-press-for-no-reason-at-traffic-lights) includes nice visualisation
    - Car colour - various online stories

    - Use of PISA data - including recent information about students not trying

- _idea_ [ ] Ask each student in the class to generate a sample to collate results and use to compare variation across samples

    - important for illustrating variability 
    - different samples could be designed to explore different types of variability

- _point_ [ ] Surveys encouraging people to register an opinion are considered very unreliable - use popular online/phone surveys
- _task_ [ ] In general identify contemporary examples of bad sampling for nefarious means

    - [Misuse of statistics - datapine](https://www.datapine.com/blog/misleading-statistics-and-data/) - interesting story about Colgate, and various others - but largely a US focus
    - [Statistics flawed in media](https://news.mit.edu/1994/statistics-1019) - 1994 article that describes some good examples

- _task_ [ ] What visualisation methods for reveal/web can I use for dotplots and steam-and-leaf plot

    - including ways to visualise variation and range

## Lessons

13 lessons

- ~7 teaching
- ~6 investigation

### Lesson 2 - Samples & Populations

Learning outcomes

- Understand the difference between a sample & a population
- Understand the various methods of collecting data (survey, census, questionnaire)

    **Question** The relationship between "collecting data" and "collecting primary" data seems arbitrary

- Select an appropriate sample and know if it is biased or not
- Explain where you've seen data used in life - food, sports, online


| Terms | Definitions | Examples and activities |
| ----- | ----------- | ----------------------- |
| Population | The group of things to make conclusions about | Give concrete examples (PISA, hottest January - 2024 versus 1964, and Oz census ) to illustrate the size of populations, which are then illustrated below |
| Census | Collection of information bout the whole of a population | - hottest temperature<br>- australian census data |
| Survey | ?? Process of gathering information from a sample |  | 
| Sample | A subset of a population | |
| Random Sample | A subset of the population chosen such that every element of the population has an equal chance of being selected. | |
| Representative sample | Includes only members of the population being studied | |
| Data | A set of observations and measurements collected during any type of systematic investigation | |
| Questionnaire | | |
| Observation | | |
| Measurement | | |
| Bias | | |
| Primary data | Data you collected | |
| Secondary data | Data collected by someone else. | |

#### Lesson activities

Starter

- perhaps a [[notice-and-wonder]] activity with data/conclusions from a couple of the chosen "statistical investigations" or perhaps just data

    Perhaps a bit too group for a starter, but perhaps a leader into one of these might be useful. Could be just a TPS type activity.  Aim here being perhaps to get them asking questions about bias, sample size, how do people know?

ToC

- Introduce the driving question - including the Goompi version
- use some of the sample SIs to draw out more discussions link to the Goompi model
- touch on what we'll do in this lesson and the rest of the unit

Tour of statistical investigation samples

- Delve more deeply into the different samples to introduce and illustrate the different terminology
- Can we get them recording/discussing/filling out some sort of worksheet with details on whether or not the different types of terminology helps/hinders drawing conclusions etc. -- better, structure it with questions that they can use for their own statistical investigation
- For example - question about if these questions should focus on the statistical investigation or the reporting of it - highlight the PISA.

    - What's the population?
    - What's the sample?
    - What methods were used to gather the data?
    - What's the variation?
    - What's the range?

Quality of decision making/reporting - build on the previous step but focus more on the reporting that has arisen around it (including mine re: temperature)

    **Important** This distinction between the reporting and the details could be very useful to make. Linked to the Goompi model

    - What did they say?
    - Can they say it?
    - Sources of bias and reliability? This might need to be exploratory and have some explicit teaching
    - **Need** identify how to visualise/demonstrate using randomly generated numbers to demonstrate random sampling


### Lesson 3 - Primary & Secondary data

Learning outcomes

- Understand the difference between primary and secondary data
- Understand various methods of collecting primary data (observation, measurement & surveys)
- Understand the source and reliability of secondary data

    - _me_ Evaluate the quality of data
- _me_ Considering the constraints on them gathering data (small to medium)
- _me_ Have students start sharing the questions/topics they're interested in exploring

#### Lesson Activities

Starter

- Some connection with prior lesson and segue into this week
- [[notice-and-wonder]] with using some secondary data - though all off the data I'm using is secondary

    - perhaps showing some of the conditions for the gathering of the data I used
    - the Colgate example would be useful
    - Something health related (e.g. [this video](https://ed.ted.com/lessons/can-you-spot-the-problem-with-these-headlines-level-1-jeff-leek-and-lucy-mcgowan)) could be useful, esp. if recent and real
    - Aim being to get students to start identifying the components and start thinking about the source and reliability
    - The PISA example is particularly good



ToC (unordered)

- Methods of collecting data
- Sources of data (combine the two?)

    - [newspaper story](https://www.theguardian.com/news/datablog/2013/may/31/times-tables-hardest-easiest-children) about a school answering the question "which times tables do students get wrong the most?" (or some such) - data generated by an app - and there's [a spreadsheet with the data](https://docs.google.com/spreadsheets/d/18QfP_gCptfo6Gf1Y5HAaiNBwrDMhGutyNk2qYl8zYmo/edit#gid=0)
- Reliability of secondary data

    - purpose of the original gathering
    - available details on the data they gathered and analysed (types of questions they need to ask for their investigation)

### Lesson 4 & 5 - Organising & displaying data

- [Guardian article on road deaths](https://www.theguardian.com/australia-news/2023/may/21/australias-rising-road-toll-how-the-pandemic-and-a-love-of-big-cars-are-putting-lives-at-risk) includes a graph that might be useful as a starter - getting students to tell the story - but then showing [wikipedia page](https://en.wikipedia.org/wiki/List_of_motor_vehicle_deaths_in_Australia_by_year) on motor vehicle deaths in Australia by year

    Graphs on wikipedia are currently down. Maybe get students to generate their own graphs from the data

    [Australian Automobile Association](https://www.aaa.asn.au/newsroom/road-deaths-continue-to-rise/) has a press release linking failure in government policy to reduce road deaths. A way to evaluate reality

### Lesson 6 - Measures of centre & spread

### Lesson 7-8 Assignment lessons


- Hand out
- Decide their topic
- Design survey Q
- Collect data
- Organise data into frequency table

Questions

- What scaffolds/activities/starters do we need for this

### Lesson 9 - Measures of centre & spread

### Lesson 10-11 Assignment lessons

- Collect data from other class
- Construct graph from frequency table

### Lesson 12 - Analysing data

Sources


### Lesson 13-14 Assignment lessons

- Analyse data
- Write report



[//begin]: # "Autogenerated link references for markdown compatibility"
[mat081c-2024]: mat081c-2024 "MAT081C-2024"
[statistics]: ../../../Mathematics/statistics "Statistics - mathematical content"
[MAT081C-2024-U1L1|Lesson 1 - You, Mathematics and this class]: mat081c-2024-u1l1 "mat081c-2024-u1l1"
[notice-and-wonder]: ../../../Mathematics/notice-and-wonder "Notice and wonder"
[//end]: # "Autogenerated link references"