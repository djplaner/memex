---
backlinks:
- title: Canvas Learning Journal - Vue implementation
  url: /memex/sense/CASA/vue-canvas-learning-journal.html
tags: web-development, javascript, vue, casa
title: Vue learning journal design
type: note
---
## Canvas learning journal - high level design

The design is based on the [single student group & graded discussions kludge](https://djplaner.github.io/memex/sense/CASA/CASA/canvas-learning-journal/#implementing-private-journals-in-canvas). i.e. each individual student's learning journal consists of

1. A Canvas group of which they are the only member.

    A group that is one of many created in a specific group set via the Canvas course's People page. 

2. One or more graded discussions topics allocated to the group set.

    In turn, each group gets a unique graded discussion topic. Students contribute to the learning journal by posting to the discussion topics. Only they and staff can see. The number of topics and if they are graded for any value depends on the learning design.

## What the CASA adds

Known issues with kludge include: 

- Ensuring all students, including those who are added late to a course, have an individual group. 

    Creating single student groups is a manual process involving CSV files. Once created, the groups are not automatically updated if students are added to the course.

- Providing an interface where teaching staff can view if and when any students have contributed to their learning journal.

    Student contributions to discussion forums are visible via the Canvas gradebook or the individual discussion topics. However, these interfaces are not well suited to the needs of teaching staff managing a large number of students with specific learning designs.

## Conceptual design

For the CASA a **learning journal activity** is an individual and assessable (in Canvas assessable tasks can contribute no marks) task. Each learning journal consists of a number of **prompts**. A prompt for one or more student **responses**. A response is some artefact the students has generated in response to the prompt. **Responses** can also be made by teaching staff. The following table maps these concepts to Canvas objects.

| Learning Journal Concept | Canvas Object |
| --- | --- |
| Learning Journal | Group set (aka group category for the Canvas API) configured with single student groups with graded discussion topics (prompts) |
| Prompt | Graded discussion topic |
| Response | Discussion post |

## User experience using the CASA

#### Creation 

To create a learning journal activity the teacher would first create a group set with the following options

| Option | Value |
| --- | --- |
| Group set name | Teacher's choice |
| Self sign-up | Nothing chosen, especially not self-sign up. Student groups will be created and allocated by the CASA |
| Group Structure | Create groups later |

#### Teacher use - configuration and management

The CASA will become active when viewing any group set that has some combination of 

- no groups allocated
- only single student groups allocated

At this stage it will add two sections somewhat mirroring the Python report design

- configuration - provides some details about the activity and its current configuration. 

    e.g. number of students/groups and any new students that haven't been allocated with the option to allocate them to groups.

- management/reporting

    A tab for each **prompt**. Each tab will show a list of students and their **responses** to the prompt.

    Teachers will be able to 

    - access the grade discussion topic for the prompt
    - see summary stats about the configuration of the graded discussion topic and student/staff entries 
    - avatar image and name/email address of the student
    - access to each student's profile page, speed grader entry for the specific discussion topic, and to the specific topic itself.
    - for each student stats including # days since last entry, # days unanswered, # staff entries, and threaded display of entries with access to the specific topics

#### Student usage

Students should be able to use the CASA to view their progress on the learning journal activity. Perhaps with some information about the activity - in the form of a Canvas page.

The CASA could provide this information when someone views the home page of the student's group.