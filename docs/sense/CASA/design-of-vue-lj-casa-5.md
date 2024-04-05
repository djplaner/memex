---
name: "Development tasks - Canvas Learning Journal"
type: "note"
tags: web-development, javascript, vue, canvas, casa
---

See also: [[vue-canvas-learning-journal]]

List of current development tasks for the [Canvas Learning Journal](https://github.com/djplaner/canvas-learning-journal)

## Current work

- [x] show the stats for student groups overview
- [x] Move the progress ring on config to cljConfigure not the sub components
- [x] check the values for the stats 

    - [x] group status
    - [x] discussion status
- [x] Move the root component widget to under the active tabs

    div#group_categories_tabs > div.ui-tabs-panel with aria-expanded=true

    - [x] the event handler for the groupSet component needs to move the root component between different active tabs

- [x] if on everyone page don't load the discussion topic data

- [x] rename "configure" > "Overview" and "orchestrate" > "Participation"

- [x] think about how/when to get all the discussion information for a group set

    First approach is to implement it within canvasApiData as a separate class/method/singleton, which can then be called from anywhere. Will start within the root component and evolve it from there. -- see [canvasApiData](#canvasapidata)

    - at the root component in the initial getCourseData

        - at this level it would be easier to share elsewhere in the app - future features
        - also simplifies the idea that all the data is already in place
        - but potentially is a lot of data waiting for it to return - responsiveness

    - separate it out till later

        - at the group set level 
        - or at the level of the component that actually displays the information

- [x] Fix problem with updating open cljGroupSet when changing between group sets

    Changing between group sets is done via an event handler in Canvas. This is bypassing my code

    - [X] try adding an eventHandler in cljGroupSet.vue

        That works for the cljGroupSet component, but the sub-components aren't changing based on changes in the group set.

    - [x] Is there a "vue way" to make sub-components change

        Yes, the problem is that the bottom sub-components were using groupSetId to access global state, but weren't watching for changes in that state.


- Defining group set status as a learning journal 

    - [x] document [status](vue-canvas-learning-journal.md#group-set--learning-journal-states)
    - [x] lmsDataApi - implement a 'learningJournalState' property
    - [x] implement the cljStatusLearningJournal component
    - [x] modify cljEveryone to show that state/status
    - [ ] modify cljGroupSet to show the state/status
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
[vue-canvas-learning-journal]: vue-canvas-learning-journal "vue-canvas-learning-journal"
[design-of-vue-lj-data-structures]: design-of-vue-lj-data-structures "design-of-vue-lj-data-structures"
[//end]: # "Autogenerated link references"