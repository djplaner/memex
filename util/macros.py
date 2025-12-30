"""
FILE: main.py
PURPOSE: Define macros using mkdocs-macros-plugin
"""

import datetime
from git import Repo

import pygal
from pygal.style import DarkStyle

from pprint import pprint
import sys

sys.path.append("/Users/davidjones/memex/util")

from corpus import corpus
bubbles = corpus()

def filterWorkHistory(region=""):
    """
    Retrieve the work history for a given region and convert the list of bubbles into a dict of dicts ordered on month and day.
    """
    #-- get a list of work-history bubbles
    regionWorkHistory = bubbles.get_bubble_by_type("work-history")
    #-- filter by region, if region "" don't filter
    if region:
        workHistory = []
        for bubble in regionWorkHistory:
            yaml = bubble.get('yaml', {})
            if not yaml:
                continue
            bubbleRegion = yaml.get('region', "unknown")
            #-- check if region is a list
            if isinstance(bubbleRegion, list):
                if region in bubbleRegion:
                    workHistory.append(bubble)
            elif region == "wood-duck-meadows" or bubbleRegion == region:
                workHistory.append(bubble)

    #-- convert the list of bubbles into a dict of dicts ordered on month and day.
    history = {}
    for bubble in workHistory:
        yaml = bubble.get('yaml', "")
        if not yaml:
            continue
        dateStr = yaml.get('date', "")
        if not dateStr:
            continue
        region = yaml.get('region', "unknown")
        #-- convert dateStr to a datetime object
        date = datetime.datetime.strptime(dateStr, "%d-%m-%Y")
#        date = date.strftime("%Y-%m-%d")
        if date.year not in history:
            history[date.year] = {}
        if date.month not in history[date.year]:
            history[date.year][date.month] = {}
        if date.day not in history[date.year][date.month]:
            history[date.year][date.month][date.day] = {}
        history[date.year][date.month][date.day] = bubble

    return history

def getWorkHistory(region=""):
    """
    Generate a string showing the work history for a region. The default region "" is for all regions

    For a single region show work history in reverse chronological order, structured as a collection of headings for year, month, and day

    ### Year

    #### Month

    ##### Day

    [Region] <if multiple regions>

    """

    #-- Extract the work history bubbles for the given region
    history = filterWorkHistory(region)

    content = ""

    for year in sorted(history.keys(), reverse=True):
        content += f"### {year}\n\n"

        for month in sorted(history[year].keys(), reverse=True):
            #-- convert numeric month into month name
            month_name = datetime.date(year, month, 1).strftime("%B")
            content += f"#### {month_name}\n"

            for day in sorted(history[year][month].keys(), reverse=True):
                bubble = history[year][month][day]
                yaml = bubble.get('yaml', {})
                title = ""
                dateStr = ""
                if yaml:
                    title = yaml.get('title', "")
                    dateStr = yaml.get('date', "")
                    if dateStr:
                        date = datetime.datetime.strptime(dateStr, "%d-%m-%Y")
                        ## dateStr == "<date> <Month> <Year>"
                        dateStr = f"**{date.strftime("%d %B %Y")}** - "

                content += f"{dateStr}{title}\n\n"
                ## - show content
                content += f"{bubble['content']}\n\n"

    if content == "":
        print(f"--------No work history available. -- region '{region}' --------")
        print(sorted(history.keys(), reverse=True))
        print("------------")
        content = "No work history available."

    return content

def calculateCommitsByYear( commits ):
    """
    Generate a dict of dicts showing the commits by year and month.
    
    {
        2025: {
            'January': [ <array of commits> ],
            'February': [ <array of commits> ],
            ...
        },
        2024: {
            'December': [ <array of images commits> ],
            ...
        }
    }
    """

    commitsByYear = {}

    for commit in commits:
        datetime_object = datetime.datetime.strptime(str(commit.committed_datetime), '%Y-%m-%d %H:%M:%S%z')
        year = datetime_object.year
        month = datetime_object.strftime('%B')

        if year not in commitsByYear:
            commitsByYear[year] = {}

        if month not in commitsByYear[year]:
            commitsByYear[year][month] = []

        commitsByYear[year][month].append(commit)


    return commitsByYear

def generateMonthByYearStats( year, commitsByYear, numCommits, numChanges ):
    """
    return a string with stats for commits by month for the given year.

    params:
        year: int - the year to generate stats for
        commitsByYear: dict - the dict of commits by year and month
        numCommits: int - the number of commits in the year
    """

    #-- if number of months with commits <= 1 return ""
    if len(commitsByYear[year]) <= 1: 
        return ""

    stats = f"""
??? info "Monthly change stats for {year}"

"""

    stats += f"""  
    ![](/memex/colophon/commitsByMonth_chart_{year}_{numChanges}.svg)

"""

    bar_chart = pygal.HorizontalBar(human_readable=True, style=DarkStyle, print_values=True)
    bar_chart.title = f"# of commits by month for {year}"

    for month in [ 'December', 'November', 'October', 'September', 'August', 'July', 'June', 'May', 'April', 'March', 'February', 'January' ]:
        numCommits = len(commitsByYear[year][month]) if month in commitsByYear[year] else 0
        bar_chart.add(month, numCommits)

    bar_chart.render_to_file(f'docs/colophon/commitsByMonth_chart_{year}_{numChanges}.svg')    


    return stats

def generateByYearStats( commitsByYear, numChanges ):
    """
    Generate a string with stats for commits by year.

    params:
        commitsByYear: dict - the dict of commits by year and month
    """

    stats = """??? info "Yearly change stats"

"""

    #-- if number of years == 1 show nothing
    if len(commitsByYear) == 1:
        return ""

    stats += f"""
    ![](/memex/colophon/commitsByYear_chart_{numChanges}.svg)

"""

#    for year in sorted(commitsByYear.keys(), reverse=True):
#        numCommits = sum(len(month) for month in commitsByYear[year].values())
#
#        stats += f"     | {year} | {numCommits} |\n"

#    stats += "\n\n"

    bar_chart = pygal.HorizontalBar( human_readable=True, style=DarkStyle, print_values=True )
    bar_chart.title = "# of commits by year"
    for year in sorted(commitsByYear.keys(), reverse=True):
        numCommits = sum(len(month) for month in commitsByYear[year].values())
        bar_chart.add(str(year), numCommits)

    bar_chart.render_to_file(f'docs/colophon/commitsByYear_chart_{numChanges}.svg')    

    return stats

def getRecentChangesTimeline( numChanges : int = -1) :
    """
    Get the last X changes to the current git repo, convert them into a timeline and return.
    If numChanges is -1, return all changes.

    Timeline is implemented via Markdown headings

    ## 2025 - (<x> changes)

    ### June, 2025 (<y> changes)

    :calendar: <commit datetime>
    <commit message>

    :calendar: <commit datetime>
    <commit message>
    """

    REPO_DIR = "/Users/davidjones/memex"
    repo = Repo(REPO_DIR)

    if numChanges == -1:
        prev_commits = list(repo.iter_commits('master'))
    else:
        prev_commits = list(repo.iter_commits('master', max_count=numChanges))

    commitsByYear = calculateCommitsByYear( prev_commits )

    changes = generateByYearStats( commitsByYear, numChanges )

    for year in sorted(commitsByYear.keys(), reverse=True):
        numCommits = sum(len(month) for month in commitsByYear[year].values())
        changes += f"### {year} - ({numCommits} changes)\n\n"
        changes += generateMonthByYearStats(year, commitsByYear, numCommits, numChanges)

        for month in [ 'December', 'November', 'October', 'September', 'August', 'July', 'June', 'May', 'April', 'March', 'February', 'January' ]:
            if month in commitsByYear[year]:
                numCommits = len(commitsByYear[year][month])
                changes += f"#### {month}, {year} - ({numCommits} changes)\n\n"

                changes += "<div class=\"grid cards\" markdown>\n\n"

                for commit in commitsByYear[year][month]:
                    datetime_object = datetime.datetime.strptime(str(commit.committed_datetime), '%Y-%m-%d %H:%M:%S%z')
                    dateStr = datetime_object.strftime('%a %-d %b, %Y %-I:%M%p')

                    #-- replace all \n in commit.message with <br>
                    commit.message = commit.message.replace("\n", "<br>" )

                    changes += f"""
-   📅 {dateStr}

    ---

    {commit.message}

"""

                changes += "</div>\n\n"
                    
    return changes

def getRecentChanges( numChanges : int ):
    """
    Get the last X changes to the current git repo, convert them into formatted markdown and return.
    """

    REPO_DIR = "/Users/davidjones/memex"
    MARKDOWN_TEMPLATE = "| {DATE} | {MESSAGE} |\n"

    repo = Repo(REPO_DIR)

    prev_commits = list(repo.iter_commits('master', max_count=numChanges))

    changes = """| When | Change |
| --- | --- |
"""

    for commit in prev_commits:
        datetime_object = datetime.datetime.strptime(str(commit.committed_datetime), '%Y-%m-%d %H:%M:%S%z')
        dateStr = datetime_object.strftime('%a %-d %b, %Y %-I:%M%p')

        #-- replace all \n in commit.message with <br>
        commit.message = commit.message.replace("\n", "<br>" )

        changes += MARKDOWN_TEMPLATE.format(MESSAGE=commit.message, DATE=dateStr, AUTHOR=commit.author)

    return changes

def getBubbleTypes():
    """
    Return a markdown table showing all bubble types in the corpus with counts ordered by descending order on count.
    """
    
    bubbleTypes = bubbles.get_bubble_type_count()

    #-- generate a list of tuples (bubbleType, count)
    bubbleTypeCounts = []
    for btype in bubbleTypes:
        bubbleTypeCounts.append( (btype, len(bubbleTypes[btype])) )

    #-- sort the list by count in descending order
    bubbleTypeCounts.sort( key=lambda x: x[1], reverse=True )

    content = """| Bubble Type | Count |
| --- | --- |
"""

    for btype, count in bubbleTypeCounts:
        content += f"| {btype} | {count} |\n"

    return content

def define_env(env):
    """
    Define the macros for use in markdown files
    """

    @env.macro
    def workHistory( region: str = "" ):
        """
        Get the work history for a specific region.
        """
        return getWorkHistory( region )

    @env.macro
    def recentChanges( numChanges : int = 5 ):
        """
        Get the last X changes to the current git repo, convert them into formatted markdown and return.
        """
        return getRecentChanges( numChanges )

    @env.macro
    def recentChangesTimeline( numChanges : int = -1 ):
        """
        Generate a timeline of the last numChanges changes to the current git repo.
        By default, will show all changes.
        """
        return getRecentChangesTimeline( numChanges )

    @env.macro
    def formatStringDate( strDate : str ):
        """
        Given a string date in the format YYYY-MM-DD HH:MM:SS, convert it to a datetime object
        and return it in the format 'dd MMM YYYY'
        """
        datetime_object = datetime.datetime.strptime(strDate, '%Y-%m-%d %H:%M:%S')
        return datetime_object.strftime('%d %b %Y')

    @env.macro
    def blogStats():
        """
        Placeholder function for use in draft blog posts. Actual blog stats is implemented on the blog site.
        """

        return "{{ blogStats()}}"

    @env.macro
    def showBubbleTypes():
        """
        Show all bubble types in the corpus with counts.
        """

        return getBubbleTypes()