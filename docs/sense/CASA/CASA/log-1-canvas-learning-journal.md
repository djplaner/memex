---
backlinks:
- title: Canvas Learning Journal
  url: /memex/sense/CASA/CASA/canvas-learning-journal.html
title: log-1-canvas-learning-journal
---
## Designing a Learning Journal CASA for Canvas

Automate the process of setting up a learning journal that

1. Creates a group set for the journal.
2. Creates a group for each student in the Courses.

  - e.g. [done with CSV import](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-groups-in-a-group-set/ta-p/417799)
3. Set up each group's site as per learning design.

    Each Canvas group site can have announcements, pages, discussion topics (most Canvas objects) that are specific to the group. This is how to scaffold the specifics of the learning journal in Canvas. 

4. Track and manage student engagement.
5. Mark assessment related components.


## Questions

Group creation/maintenance

- [ ] How difficult is this via the CSV import? Problems with 1 person groups?

    [Process](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-groups-in-a-group-set/ta-p/417799)

    - Create the group set first, use _I'll create groups later_ switch
    - Use the import button - generates a CSV file to download

    - Edit the CSV by updating the _group_name_ column appropriately
    - Students already with groups have their group name and details populated
    - New students need names added
    - Upload

- [ ] What happens as students added to/removed from the course? 
- [ ] Can it be automated? API? How?

Group site set up

- [ ] How difficult to set up manually? Does Canvas provide a way to pre-populate groups?

    - With discussions, you set a switch _this is a group discussion_ and one is created for each group in a group set.
    - With pages, it is done via the group navigation (i.e. in the group)
- [ ] How to automate population of Canvas groups? API? other means?

    - [Groups API](https://canvas.instructure.com/doc/api/groups.html) enables uploading of a file and a lot of querying of group resources (including activity steam). But apparently a group can be used as _parent context_ for other resource types e.g. rather than `/v1/courses/{course_id}/pages` (create page for a course) use `/v1/groups/{group_id}/pages` to create a page for  group.

### API Tasks

- [ ] Group creation - create 1 student group per student
    - [ ] Handle initial creation
    - [ ] Detect students with/without groups (handle late enrolments)
- [ ] Group site set up - create all the resources on the group site
- [ ] Task management - track and help those who have/haven't engaged
- [ ] Marking - final marking

## Sample course design

Course design that includes

- weekly learning activity log

    1 post per week. Fixed format (one of two to choose from)
    Task details provided as Word documents

- portfolio 1

    - Collection of weekly tasks. Combined into a single Word document.  
    - A reflection
    - Feedback
- portfolio 2

### Possibilities

- Discussion forums
    - A single group discussion for each assessment task 

      - Canvas discussions are limited in terms of threads. Making it difficult to see who has/hasn't engaged.
      - Makes it easier to do a holistic marking of all contributions, rather than marking each separately.
    - Multiple forums - one for each individual component - support threaded discussions better - but complexity? - better support for identifying who has completed or not - and also for separate due dates - also for the first task which is not assessable

- Home page - not proper home page for group section, just on the pages for that group

    Configure the home page with information about the assessment, perhaps pointing to various details elsewhere. Perhaps sharing a page across all groups?  Can't be done apparently.

- Announcements

    Are visible on the group home page, but are somewhat visually limited. Probably no value in automating the addition of announcements in each group.  Could emulate much the same via links to assessable discussion forums in the broader course Canvas site.