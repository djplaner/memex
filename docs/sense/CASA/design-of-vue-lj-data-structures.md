---
name: "Design of Vue Learning Journal Data Structures"
type: "note"
tags: web-development, javascript, vue, canvas, casa
---

See also: [[vue-canvas-learning-journal]]

Design and summarise current data structures.

Currently data structure management entirely in `canvasApiData.ts`


## Usage of canvasApiData

The root component (`App.vue`) does the initial `const canvasData = getCanvasData()`, which initiates the API call. All subsequent calls will be getting the singleton. They are also guaranteed to have the data available as the `App.vue` does not add any sub-components to the DOM until the data is loaded.

Some of the sub-components currently have left over crud to be removed.

Other sub-components (the group set specific stuff) will/may need to do additional queries. Alternatively could do it all initially depending on whether a group set is determined to be a learning journal.


## canvasApiData

Exports a function `getCanvasCourse` which generates a singleton object of type `courseData`. It retrieves data from the Canvas API and then transforms it into a more useful object.

| Property | Description |
| --- | --- |
| `id` | the course id |
| `name` | the course name |
| `courseCode` | Canvas API course code |
| `hostname` | the Canvas instance's hostname (url) |
| `createdAt` | the date the course was created |
| `updated` | a counter that is incremented each time the object is updated |
| `groupSets` | an array of group sets _currently undefined_ |
| `groupSetsById` | an object with group set ids as keys and group set data as values |
| `students` | an array of student data |
| `studentsById` | an object with student ids as keys and student data as values |
| `teachers` | an array of teacher data |
| `teachersById` | an object with teacher ids as keys and teacher data as values |
| `discussions` | Array of discussion data retrieved via REST API (no graphQL support) this data is then parsed into appropriate places within `groupSets` data structure |
| `courseObject` | **deprecated** object returned by the [GraphQL query](design-of-vue-lj-casa-1.md#graphql) |
| ` @TODO assignments | |

### groupSets

The `groupSets` property is an array of objects representing an individual groupset, including 

| Property | Description |
| --- | --- |
| `_id` | the group set id |
| `id` | the group set GraphQL id |
| `name` | the group set name |
| `memberLimit` | the maximum number of members allowed in a group |
| `selfSignUp` | whether students can self sign up for groups |
| `numGroups` | the number of groups in the group set - calculated by code |
| `numMembers` | Number of students who are members of groups within the group set |
| `discussionTopics` | Discussion topics (Canvas API objects) associated with this group set |
| `groupsConnection` | the original GraphQL property |
| `groups` | array of data about the groups that belong to the group set |

#### Groups

The `groups` property is an array of objects for each group belonging to the group set with the following properties

| Property | Description |
| --- | --- |
| `_id` | the group id |
| `name` | the group name |
| `updatedAt` | the date the group was last updated |
| `membersCount` | the number of members in the group |
| `canMessage` | whether members can message each other |
| `createdAt` | the date the group was created |
| `members` | array of data about the members of the group. Which is an array of objects with a `nodes` property that contains an array (only usually one for a learning journal) with basic user information (_id, name, email, avatarUrl)  |

### students and teachers

The `students` and `teachers` properties array arrays of objects representing student/teacher  info in the course with the following properties

| Property | Description |
| --- | --- |
| `_id` | the student's Canvas id |
| `name` | the student's name |
| `email` | the student's email address |
| `htmlUrl` | the student's avatar/about page for the current course |

- [Usage of canvasApiData](#usage-of-canvasapidata)
- [canvasApiData](#canvasapidata)
  - [groupSets](#groupsets)
    - [Groups](#groups)
  - [students and teachers](#students-and-teachers)
- [Matching Python data structures](#matching-python-data-structures)
- [Transformed GraphQL data](#transformed-graphql-data)
- [On the question of stores](#on-the-question-of-stores)

```json
{
    "id": 7446794,
    "name": "Collections Copy",
    "groupSets": [],
    "courseObject": {
        "_id": "7446794",
        "name": "Collections Copy",
        "courseCode": "Collections",
        "createdAt": "2023-08-05T20:53:16-06:00",
        "groupSetsConnection": {
            "nodes": [
                {
                    "id": "R3JvdXBTZXQtMjkwMjMy",
                    "_id": "290232",
                    "name": "Your reflective journal",
                    "memberLimit": null,
                    "selfSignup": "disabled",
                    "groupsConnection": {
                        "nodes": [
                            {
                                "_id": "974036",
                                "name": "PtjMUwBqFOvn-d1WEezZi1CzZPaIPP1AfWGwEhDE5jU (PtjMUwBqFOvn-d1WEezZi1CzZPaIPP1AfWGwEhDE5jU)",
                                "updatedAt": "2023-12-12T21:11:39-07:00",
                                "membersCount": 1,
                                "canMessage": true,
                                "createdAt": "2023-12-12T21:05:07-07:00",
                                "membersConnection": {
                                    "nodes": [
                                        {
                                            "_id": "3750916",
                                            "createdAt": "2023-12-12T21:05:07-07:00",
                                            "user": {
                                                "_id": "109793678",
                                                "name": "PtjMUwBqFOvn-d1WEezZi1CzZPaIPP1AfWGwEhDE5jU",
                                                "email": "d.jones6@griffith.edu.au",
                                                "avatarUrl": null
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "_id": "974035",
                                "name": "Steven Booten (s.booten@griffith.edu.au)",
                                "updatedAt": "2023-12-12T21:11:39-07:00",
                                "membersCount": 1,
                                "canMessage": true,
                                "createdAt": "2023-12-12T21:05:06-07:00",
                                "membersConnection": {
                                    "nodes": [
                                        {
                                            "_id": "3750915",
                                            "createdAt": "2023-12-12T21:05:07-07:00",
                                            "user": {
                                                "_id": "109792759",
                                                "name": "Steven Booten",
                                                "email": "s.booten@griffith.edu.au",
                                                "avatarUrl": null
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "_id": "974034",
                                "name": "wzCp2-sXN4gCyYI8fUw__N4XCm1TDI8EPLNAhayh-Ek (wzCp2-sXN4gCyYI8fUw__N4XCm1TDI8EPLNAhayh-Ek)",
                                "updatedAt": "2023-12-12T21:11:39-07:00",
                                "membersCount": 1,
                                "canMessage": true,
                                "createdAt": "2023-12-12T21:05:05-07:00",
                                "membersConnection": {
                                    "nodes": [
                                        {
                                            "_id": "3750914",
                                            "createdAt": "2023-12-12T21:05:06-07:00",
                                            "user": {
                                                "_id": "109793756",
                                                "name": "wzCp2-sXN4gCyYI8fUw__N4XCm1TDI8EPLNAhayh-Ek",
                                                "email": "h.cook@griffith.edu.au",
                                                "avatarUrl": null
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                },
                {
                    "id": "R3JvdXBTZXQtMjkwMjky",
                    "_id": "290292",
                    "name": "Weekly learning activities",
                    "memberLimit": null,
                    "selfSignup": "disabled",
                    "groupsConnection": {
                        "nodes": [
                            {
                                "_id": "974338",
                                "name": "PtjMUwBqFOvn-d1WEezZi1CzZPaIPP1AfWGwEhDE5jU (PtjMUwBqFOvn-d1WEezZi1CzZPaIPP1AfWGwEhDE5jU)",
                                "updatedAt": "2023-12-13T13:34:40-07:00",
                                "membersCount": 1,
                                "canMessage": true,
                                "createdAt": "2023-12-13T13:34:39-07:00",
                                "membersConnection": {
                                    "nodes": [
                                        {
                                            "_id": "3751770",
                                            "createdAt": "2023-12-13T13:34:40-07:00",
                                            "user": {
                                                "_id": "109793678",
                                                "name": "PtjMUwBqFOvn-d1WEezZi1CzZPaIPP1AfWGwEhDE5jU",
                                                "email": "d.jones6@griffith.edu.au",
                                                "avatarUrl": null
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "_id": "974337",
                                "name": "Steven Booten (s.booten@griffith.edu.au)",
                                "updatedAt": "2023-12-13T13:34:39-07:00",
                                "membersCount": 1,
                                "canMessage": true,
                                "createdAt": "2023-12-13T13:34:38-07:00",
                                "membersConnection": {
                                    "nodes": [
                                        {
                                            "_id": "3751769",
                                            "createdAt": "2023-12-13T13:34:39-07:00",
                                            "user": {
                                                "_id": "109792759",
                                                "name": "Steven Booten",
                                                "email": "s.booten@griffith.edu.au",
                                                "avatarUrl": null
                                            }
                                        }
                                    ]
                                }
                            },
                            {
                                "_id": "974339",
                                "name": "wzCp2-sXN4gCyYI8fUw__N4XCm1TDI8EPLNAhayh-Ek (wzCp2-sXN4gCyYI8fUw__N4XCm1TDI8EPLNAhayh-Ek)",
                                "updatedAt": "2023-12-13T13:34:40-07:00",
                                "membersCount": 1,
                                "canMessage": true,
                                "createdAt": "2023-12-13T13:34:40-07:00",
                                "membersConnection": {
                                    "nodes": [
                                        {
                                            "_id": "3751771",
                                            "createdAt": "2023-12-13T13:34:40-07:00",
                                            "user": {
                                                "_id": "109793756",
                                                "name": "wzCp2-sXN4gCyYI8fUw__N4XCm1TDI8EPLNAhayh-Ek",
                                                "email": "h.cook@griffith.edu.au",
                                                "avatarUrl": null
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                },
                {
                    "id": "R3JvdXBTZXQtMjk2NDk3",
                    "_id": "296497",
                    "name": "testing",
                    "memberLimit": null,
                    "selfSignup": "disabled",
                    "groupsConnection": {
                        "nodes": []
                    }
                }
            ]
        }
    },
    "hostName": "https://canvas.instructure.com",
    "updated": 1
}
```

## Matching Python data structures

Todo 

- Extract from each group set's groups' members all the current members of the group set -- to identify if there are any students without a group

    - Number of groups should match number of students for initial check
    - then list of students compared with all students to find out who's missing
- Get list of discussion topics for a group set, including posts/entries
- Calculate stats for a group set/learning journal

Global 

| Python | Vue | Description | Used where |
| --- | --- | --- | --- |
| teachers | course_object.teachers | All user info based on enrolment_type "teacher" |  |
| staff_list | @todo calculate if/when needed | An array of staff user ids taken from teachers |  |
| students | course_object.students |  All user info based on enrolment type 'student' | Obtained in Vue |

Group set level -- courseObject.groupSets.nodes

| Python | Vue | Description | Used where |
| --- | --- | --- | --- |
| groupMembers | | Collection of membership information | **deprecated?** not used in view in Python   |
| users | | Paginated list of user information for people in the group | **deprecated** |
| topic | | Canvas topic object - posibly not there? | **deprecated** |
| stats | @todo further analysis in vue | num_groups, num_unanswered_student_posts, num_student_entries, num_no_student_entry, num_prompts, num_no_staff_entry  |  |
| prompts | course_object.assignments gets all assignments. @todo extract out the discussion topics and perhaps get more info or explore another way of getting the info | Array of objects for the prompts for a group set | |

Prompts level

| Python | Vue | Description | Used where |
| --- | --- | --- | --- |
| prompt_stats | | Statistics about the prompt across all groups| |
| assignment | | Info about the assignment, including the parent discussion topic | |
| responses | | Array of objects for all responses to a prompt | |

Response level

| Python | Vue | Description | Used where |
| --- | --- | --- | --- |
| topic_id | | Discussion topic information (specific to the group) | |
| group_id | | | |
| prompt_topic | | The actual discussion topic object | |
| entries | | Full discussion topic | |
| entry_stats | | | |


## Transformed GraphQL data

The GraphQL data isn't directly useful for the Vue components.


## On the question of stores

Beyond the basic (singleton) approach initially used there are purpose [built stores](https://dev.to/muratcanyuksel/saving-and-using-fetched-data-with-vuex-store-2igj) for Vue. [Pinia](https://pinia.vuejs.org/introduction.html) appears to be a current good one. Recommended by the [Vue originator](https://rubenr.dev/pinia-vuex/)

But perhaps too heavy weight for usage now. This [comparison of state management in Vue](https://medium.com/@subodha.sahu91/3-state-management-in-vue-js-c4cda1ca1397) lists three options

1. global event bus 

    - Difficult to maintain as application grows. Also lead to data inconsistencies
2. simple global store 
3. Vuex library (Pinia fits here)

[//begin]: # "Autogenerated link references for markdown compatibility"
[vue-canvas-learning-journal]: vue-canvas-learning-journal "vue-canvas-learning-journal"
[//end]: # "Autogenerated link references"