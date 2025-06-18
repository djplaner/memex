"""
FILE: main.py
PURPOSE: Define macros using mkdocs-macros-plugin
"""

import datetime
from git import Repo

import pygal
from pygal.style import DarkStyle

from pprint import pprint

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

    bar_chart = pygal.HorizontalBar(human_readable=True, style=DarkStyle)
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

    bar_chart = pygal.HorizontalBar( human_readable=True, style=DarkStyle)
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


def define_env(env):
    """
    Define the macros for use in markdown files
    """

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