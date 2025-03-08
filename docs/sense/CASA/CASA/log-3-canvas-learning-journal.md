# Log 3 - Canvas learning journal

Implementation of a [[canvas-learning-journal]] [[casa]].

In particular, the aim here is to develop a web-based report on activity/contributions to an individual group graded discussion.


- [X] [Search for example graded discussion forum reports](#search-for-example-graded-discussion-forum-reports) - nothing apparent for the current purpose
- [X] [What APIs required - REST/GraphQL](#what-apis-required-restgraphql) - using CanvasAPI in Python
- [X] Implement in Python - commenced `lj-report.py` in AEL-LT
- [X] [Design the visuals for such a report](#design-the-visuals)
- [X] [Reconceptualise the learning journal - generalise](#reconceptualise-the-design)


## Search for example graded discussion forum reports


- [Workshop presentation](https://www.uv.uio.no/om/organisasjon/idea/aktivitetstilbud/idea-arrangerer/uv-labene/engagelab-using-canvas-discussion-analytics-for-teaching-and-online-discussion) from Norway on PhD student developing a Canvas discussions dashboard - not a great amount of detail

### Canvas LMS discussions to Google analytics

[post](https://hawksey.info/blog/2016/04/pushing-canvas-lms-discussion-data-to-google-analytics-tips-on-google-analytics-api-integration-batch-collection-and-queue-time/) from Martin Hawksey. And [related earlier post](https://hawksey.info/blog/2013/02/lak13-recipes-in-capturing-and-analyzing-data-using-sna-on-canvas-discussions-with-nodexl-for-when-its-not-a-snapp/) useing NodeJS

Interesting application, slightly different purpose

### [Discussion Analytics](http://learningapps.northwestern.edu/#/app/c92eafed-61bd-4261-8ce0-470910a34e69)

PHP App from Northwestern University - applies NLP to content from discussion forums. [Code is available](https://bitbucket.org/northwesternitartsdg/discussion-analytics-release/src/master/)

Different purpose

## What APIS required - REST/GraphQL

### [Discussion Topics API](https://canvas.instructure.com/doc/api/discussion_topics.html)

Can be given group id


Likely process

- Configuration information required
  - name of graded discussion topic?

- Get the discussion topic

    - List the [discusion topics](https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics.index)

        `/api/v1/courses/<courseId>/discussion_topics?order_by=title`, JSON returned includes

          - `group_category_id` - group set??
          - `topic_children` - might be the individual group discussions??? 
          - `group_topic_children` - list of dicts with topic id (41331) and group id (16567)
          - `assignment` - dict with details of assignment
    - if the right one 
      - [Get the full topic](https://canvas.instructure.com/doc/api/discussion_topics.html#method.discussion_topics_api.view)

        `/api/v1/groups/<group-id>/discussion_topics/<topic-id>/view`, returns dict with

        - `unread_entries` - list of entry ids not read
        - `participants` - list of dicts with details of users, including `avatar_image_url`, `id`, `display_name`, `html_url` 
        - `view` a threaded view of all entries 

            List of dicts, each containing

            - `id`, `user_id`
            - `created_at`, `updated_at`
            - `message`
            - `replies` - a list of dicts of the same structure

## Design the visuals

Requirements

- overview of graded discussion (per graded discussion)

  - # of groups (students)
  - # of groups with student entries after staff reply
  - # of student entries in journals, average, min, max
  - # of staff entries per group: average, min, max

- summary of each group topic (student)

  - Name and link to the group topic
  - # of posts by student, staff
  - when the last post was for student's staff
  - student photo and their profile

### first design - cards - test case

```html
<sl-card class="">
  <img slot="image"
     src="" alt=""
  />

  <strong><a href="">(forum/student name)</a></strong><br />  
  <p># posts student: (num) staff: (num)</p>  
  <p>Last post: student (date) staff <span class="late">(date)</p>
</sl-card>
```

### second design - move to tables

Using at the Carbon Design System's [data table](https://web-components.carbondesignsystem.com/?path=%2Fdocs%2Fcomponents-datatable-filtering--default) for implementation

Original design was using two tables - expandable and sortable. Have since moved to using a single table and merging content.

- [X] Improve design of tables: rows, spacing, width, font etc
- [X] Remove form name from journal - just the student
- [X] Change the formatting of the tab to make the current selected on more obvious
- [X] Add column for student update
- [X] add tooltip help - **won't do**
- [X] Fix the _enrolled_ field - not working
- [X] add course name and link to title
- [X] If/how to add a relevant link to the quick grader

  - speed grader URL BASE_URL/courses/<courseId>/gradebook/speed_grader?assignment_id=<assignId>45047&student_id=<studentId>59817

    - topic.assignment_id will have that

## Reconceptualise the design

Design above only handles the case of a single graded discussion. Need to generalise to handle multiple graded discussions. Also moving to an OO MVC structure

- A _learning journal_ is essentially a _group set_ that includes at least one _graded discussion_.
- There may not always be a single student - but we can assume that.

Given a _courseId_ and a _groupSetId_ generate a learning journal report for all associated graded discussions


  Replacing the idea of providing the list of teaching staff members

- [X] Fix num_groups
- [X] Highlight the first response tab
- [X] Implement DATA-GROUPS
- [X] add in date of last post (from students)
   Started work in the view -- need to align the code for unanswered and date last post

  - [X] displayPromptPanel

Intro

- [X] Add in details about the group set in the title

    - [X] Include time the report was generated
- [X] Revisit the top level stats

  - [X] Add # of groups

- [X] Add a short description

Style

- [X] fix table cell alignment - make consistent

Testing

- [X] Test with multiple graded discussions

  - https://canvas.instructure.com courseId 7446794 group set 286165
  - working, but not sure if model/view is excluding groups that don't belong to it.
    - From the view it appears it is getting prompt_topics that don't belong to the response
    - View is 
      - for prompt in self.learningJournal.prompts
        - for response in prompt['response'] 
    - Model::getResponse is looping though groupTopics, perhaps not only including those relevant to the current group
      - does prompt_topic contain the prompt.assignment.discussion_topic.id 19950852

Finishing

- [X] fix base URL
- [X] Update and improve the help
- [X] Write some final documentation

[//begin]: # "Autogenerated link references for markdown compatibility"
[canvas-learning-journal]: canvas-learning-journal "Canvas Learning Journal"
[casa]: ../casa "Contextually Appropriate Scaffolding Assemblages (CASA)"
[//end]: # "Autogenerated link references"