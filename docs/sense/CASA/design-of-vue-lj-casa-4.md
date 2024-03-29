---
name: "Design of root components - (Canvas Learning Journal CASA 4)"
type: "note"
tags: web-development, javascript, vue, canvas, casa
---

See also: [[vue-canvas-learning-journal]]

Outline the design of the root components and overall high level application design for _Canvas Learning Journal_.

## main.ts

Ensures that the Vue app is only loaded onto the "people" and groupset pages of a Canvas course when used by teaching staff.

If on the groupset page, pass the group set id to the App.

Also starts the retrieval of course information from the Canvas API using `getCanvasCourse` from [canvasApiData](#canvasapidata).

## App

Decide which component to display based on the group set id prop

1. If no groupset, display the [cljEveryone component](#cljEveryone).
2. if there is a group set, display the [cljGroupSet component](#cljGroupSet).

## cljEveryone

Shown on the user's (people) page of a Canvas course to raise awareness that CLJ is available and to provide a link to the documentation.  Also via expansion provide a holder component that relies on sub-components to do the work

- [cljGroupSets](#cljGroupSets)

    Overview of all the groupsets currently in the course.

- [cljCreateLearningJournal](#cljCreateLearningJournal)

    Form to create a learning journal group set

### cljGroupSets

Display a table for each available learning journal.

Table will display

- Name of the group set
- Group set type (learning journal status)

    - no group allocation
        - groups don't have any members
    - not learning journal 
        - Groups have more than one person AND/OR self-sign up is possible
        - no discussion forums
    - learning journal
        - groups have more than one person AND/OR self-sign up is possible 
        - graded discussion forums
    - private learning journal
        - groups have only one person AND self-sign up is not possible

- missing from groups

    - display # of students without allocated groups in each group set

        The group set display will provide details on who they are and how to allocate them to a group. Which would depend on the status.

### cljCreateLearningJournal

Form to create a learning journal group set

- would require simply the name of the group set 
- submission would create the group set and automatically allocate one group per student
- needs to ensure that the name entered does not match any existing group set
- display information about the next steps for creation


## cljGroupSet

Shown on the group set page of a Canvas course. Provides all functionality required to configure (through [cljConfigure](#cljconfigure)) and orchestrate (through [cljOrchestrate](#cljorchestrate)) the use of a learning journal for that specific group set.

### cljConfigure

Display the current status of configuration as a learning journal for the current groupset and provide the functionality necessary to complete the configuration.

Configuration stages include the following

- Configure the group set - `cljStatusGroupSet`

    As `cljConfigure` is displayed on the group set page, it won't actually provide any configuration functionality. It will provide a summary of whether or not the group set can be used as a learning journal. Including display of the current configuration of the group set.
- Create groups in the group set for all students - `cljStatusStudentGroups`

    Each student should have their own group. Provide information summarising number of groups, and details of students without groups. Provide option to create groups for those students.

    **Note:** Removing students from a section.
- Create the graded discussion forums for the learning journal prompts - `cljStatusDiscussions`


The model here is that there is a component responsible for displaying current status as part of `cljConfigure`, including some visual update at the highest level. These will be combined perhaps using a shoelace `details` widget.

If there is any configuration left to be done, that component provides a button/interface that launches the matching `cljConfigure<Stage>` component. That will probably be some pop-up.

#### cljStatusGroupSet

Possible data for group sets from [Canvas API](https://canvas.instructure.com/doc/api/group_categories.html)

- id 
- name 
- role communities, student_organised, imported
- self_signup: random, first, null
- auto_leader: random, first, null
- context_type: Course, Account (possibly ignore this one?)
- group_limit: used if self-signup is enabled, null places no limit, otherwise number

#### cljStatusStudentGroups

#### cljStatusDiscussion

### cljOrchestrate

Provide a report of the current status of all learning journals and ways for the teacher to orchestrate student engagement.

If there's no learning journal possible for the current group set, this is all greyed out.

Two components

- `cljStatusLearningJournal`

    Summary of # of prompts and students and then the high level table.

- `cljStatusPrompts`

    Each prompt has a tab with a report of student engagement with those prompts.

#### cljStatusLearningJournal

Based on top part of existing report - to be refined

#### cljStatusPrompts

Based on bottom part of existing report - to be refined

## Support libraries and components

### canvasApiData

The data model for the components.

Perform a big GraphQL query of Canvas API data that is provided to the rest of the components. Act as a central, reactive store for that information. 

Provide CLJ specific methods used by the other components.

[//begin]: # "Autogenerated link references for markdown compatibility"
[vue-canvas-learning-journal]: vue-canvas-learning-journal "vue-canvas-learning-journal"
[//end]: # "Autogenerated link references"