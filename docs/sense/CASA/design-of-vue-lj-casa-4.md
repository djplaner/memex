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

Canvas API REST method to [create a group set (aka category)](https://canvas.instructure.com/doc/api/group_categories.html#method.group_categories.create), request parameters:

  - name: string
  - self_signup: string [ enabled, restricted ]
  - auto_leader: string [ first, random ]
  - group_limit: integer 
  - sis_group_category_id: string (not sure)
  - create_group_count: integer - number of groups to created
  - split_group_count: string - deprecated

Returns a [GroupCategory](https://canvas.instructure.com/doc/api/group_categories.html#GroupCategory) object.

Form should just take the name of the group set.


 

## cljGroupSet

Base component shown on the group set page of a Canvas course. 

For valid Learning journals will provides all functionality required to configure through sub-components under tags 

- Configure - [cljConfigure](#cljconfigure)) and 
- orchestrate - ([cljOrchestrate](#cljorchestrate)) 

Only show these if there are prompts for the group set.

BUt only show 

### cljConfigure

Display the current status of configuration as a learning journal for the current groupset and provide the functionality necessary to complete the configuration.

Probably/Perhaps provide functionality to add prompts and create single-person groups - turn off self-signup etc.

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

Show high level stats about the current group set (aka [group category](https://canvas.instructure.com/doc/api/group_categories.html)) showing

- general group category/set information, and

    - name 
    - self_signup and group_limit
    - auto_leader

- any additional learning journal analysis

    - num members / num course students
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

Design ideas 

- 2 column div (flex/grid): Learning Journal, Group Set
- Learning Journal 

    Provides any info about the group sets ability/status as a group set

    - status along progression to be a learning journal
    - info about any unallocated students

- Group set 

    Copy of data from [cljGroupSets](#cljgroupsets) specific to this group set



#### cljStatusStudentGroups

Show a summary of information about each of the student groups in the current group set.

- num groups without student entries
- num groups without recent student entries
- num groups without staff entries
- num groups without recent staff entries

Each of these being a table that includes 

- a count for each category and 
- (maybe) a details tab to reveal the details of those

    Functionally, this could be done within the prompts?  but that would only be for a specific prompt.
    This level would need to include the group and maybe the prompt


#### cljStatusDiscussion

Give an overview of the status of each discussion topic for the group set. Show a table/list of all the discussion topics and variuos stats, possibilities include

- num groups without student entries - 7 days and ever
- num groups without staff entries  - 7 days and ever


### cljOrchestrate

Provide a report of the current status of all learning journals and ways for the teacher to orchestrate student engagement.

If there's no learning journal possible for the current group set, this is all greyed out.

Two components

- `cljOverviewParticipation`

    Summary of # of prompts and students and then the high level table.

- `cljPromptsParticipation`

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