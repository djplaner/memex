---
backlinks:
- title: Canvas Learning Journal - Vue implementation
  url: /sense/CASA/vue-canvas-learning-journal.html
tags: web-development, javascript, vue, canvas, casa
title: Development tasks - Canvas Learning Journal
type: note
---
List of current development tasks for the [Canvas Learning Journal](https://github.com/djplaner/canvas-learning-journal)

## Current work

- [ ] cljCreateGroups (see below)
- [ ] cljCreateLearningJournal (see below)
- [x] groupset overview loading progress doesn't get replaced if the CLJ not open
- [ ] Add a reload/refresh button that gets the Canvas API data afresh

- [ ] cljPromptParticipationDetails 

    - [x] try out Vuex data table or alternative [vue3-easy-data-table](https://hc200ok.github.io/vue3-easy-data-table-doc/features/style-customization.html)

        Problem with data table (Vuex) is the icons and Canvas' `i[class*=icon-]:before` rule which is changing the font to a Canvas font to make those icons work. Vuetify add `v-icon` and `v-icon--size-default` classes. Remove those classes and it appears to work (manually). Can it be made to work programmatically?
    - [x] fix up group cell for details and css
    - [x] test for presence of real avatar url
    - [x] fix up counting stats for student and staff
    - [x] test for the topic having an assignment 
      - [ ] And maybe if the student actually has a submission??? no student entries would suggest nothing
    - [x] link to forum
    - [ ] testing for an unanswered reply can't really rely just on last post...or needs to make it clear from the naming
    - [ ] add days since last student entry and unanswered to stats generation for topics


    - [ ] numGroups calculation in participation getting too many groups

- [ ] cljTopicEntries

    - [ ] make the threaded entries display collaps/expandable in various ways 
      - [ ] live on the actual replies itself 
      - [ ] collapse/expand all to reduce space in the table
    - [x] identify where/how to get the entries and replies
        - should be in the `promptsByGroupId[..].stats.view
           - and each one can have a 'replies' property - descending
    - [x] generate the recursive structure of replies

        - [x] entries being shown
        - [x] get user name 
        - [x] recurse to show replies 
        - [x] change the structure of the table to give more space to the threaded replies

- Defining group set status as a learning journal 

    - [x] document [status](vue-canvas-learning-journal.md#group-set-learning-journal-states)
    - [x] lmsDataApi - implement a 'learningJournalState' property
    - [x] implement the cljStatusLearningJournal component
    - [x] modify cljEveryone to show that state/status
    - [x] modify cljGroupSet to show the state/status
- refining the GraphQL query to get all the data 

    - Did some initial work but now refining as working on each component

- [x] Implement initial root components just the infrastructure
- canvasApiData 

    - [ ] Clean up [canvasApiData](#canvasapidata) to do list 
    - [X] Getting discussions data via REST API
    - [ ] Getting the contents of discussion topics for a groupset via REST API
    - [ ] check/update to get all group set information
    - [ ] identify if a group set can be a learning journal
    - [ ] get the prompt data - identify when this should 🙋 

        e.g. at load time or when/if the group set is displayed (latter seems a good choice)
    - [ ] Implement methods to be used by other components

## cljGroupSet

- [x] hide orchestrate and parts of configure when not learning journal
- [ ] Implement cljConfigure
- [ ] Implement cljOrchestrate

## cljCreatePrompt

- [ ] identify the data/API required to create a ???
- [ ] implement a lib/create???.ts file 
  - [ ] defines a type/class for the data/API 
  - [ ] Implements the async call to the API to create the learning journal
- [ ] link it to the component
    - [ ] use the type to guide creation of the form
    - [ ] identify the other data required to scaffold form completion
    - [ ] interact with the async call to create and report progress/end result

## cljCreateLearningJournal 

- [ ] identify the data/API required to create a ???
- [ ] implement a lib/create???.ts file 
  - [ ] defines a type/class for the data/API 
  - [ ] Implements the async call to the API to create the learning journal
- [ ] link it to the component
    - [ ] use the type to guide creation of the form
    - [ ] identify the other data required to scaffold form completion
    - [ ] interact with the async call to create and report progress/end result

## cljCreateGroups

Called from cljGroupSet when there are students who do not have the group 

- provide a button when pressed 
- opens a dialog that allows 
- selection of what groups to create

    - which sections of students to include  - drop down with all sections
    - Ability to select individual students to exclude - table showing all students without groups
    - [ ] add some blurb about what to do 
    - [ ] correctly label the search on name and sections
    - [ ] add a "Create groups" button

- and then creates the groups 

    - [ ] add a function/method to create the groups
        - [ ] Identify how to create groups from AEL LJ
        - [ ] update the display
        - [ ] do a synchronous call to the API to create the groups
- returning to the original state

### cljConfigure

- [x] hide cljStatusDiscussions and cljOrchestrate when not learning journal

#### cljStatusGroupSet

- [ ] whether/what to add in terms of configuration buttons/links when no groups, no prompts
- [ ] How to display the details of students who are not in a group (used in multiple places)

#### cljStatusStudentGroups

- [ ] model method to calculate statistics about entries in prompts

    - [ ] groups without student entries: 7 days and ever
    - [ ] groups without staff entries: 7 days and ever

#### cljStatusDiscussions

- [ ] show table and rows for all groups

    - [ ] basic rows with names and columns
    - [ ] add status property to each group's discussion topics objects
        - this.groupSets[0].groups[0].prompts[0].stats
    - [ ] add status property to each groupset's discussion topics objects based on the relevant group's discussion status property

Trying to figure out how to add prompt stats to discussionTopics

this.groupSets[0].discussionTopics[0].prompts = {} // a dict of points to the prompts....grouped by discussion topic, rather than group


### cljOrchestrate




## General

### Operations

- [ ] How to trap and handle errors
- [ ] code based documentation
- [ ] testing

### Visual design

- [ ] colour schemes
- [ ] look and feel

### Documentation site

- [ ] Identify list of in application document links required
- [ ] Identify components of the documentation site
- [ ] Organise into structure
- [ ] Identify look and feel
- [ ] develop content

## main.ts 

- [ ] Ensure App only added for teaching staff
- [ ] Clean up debugging

## App.vue

- [ ] Handle all possibilities retrieving Canvas data via the API

    - [ ] Waiting for data to be retrieved
        Not currently being done
    - [ ] Error retrieving data
    - [ ] Data successfully retrieved **currently working roughly**

## canvasApiData

- [x] Rename functions to be more specific to the Canvas Learning Journal (rather than course)
- [x] transform the GraphQL object into something a little more useful - see [[design-of-vue-lj-data-structures]]
- [ ] Be able to get all the learning journal data (drawn from LearningJournal class from Python version)

    - [x] discussion topics (global)
    - [ ] group set topics and messages

            Sort of working


    - Course level??

        - [x] `teachers` 
        - [ ] `staff_list`
        - [x] `students` - i.e. those in the section?? or all students???

    - Group set level

        - [ ] `members`
        - [ ] `stats`

        - `prompts` - Prompt level (part of each group set) - prompts (array of dicts)

            - [ ] `prompt_stats`
            - [ ] `assignment` info about the assignment, including discussion topic?
            - [ ] `responses` array of dicts for all responses to a prompt

                - `topic_id` - discussion topic information (specific to the group)
                - `group_id` 
                -  `prompt_topic` - the actual discussion topic object 
                - `entries` full discussion topic
                - `entry_stats`


        - `groups`  (part of each group set)

- [ ] Add in specific CLJ methods
    - `isGroupSetALearningJournal`
    - `getNumLearningJournals`
    - `getNoGroupStudents`

[//begin]: # "Autogenerated link references for markdown compatibility"
[design-of-vue-lj-data-structures]: design-of-vue-lj-data-structures "Design of Vue Learning Journal Data Structures"
[//end]: # "Autogenerated link references"