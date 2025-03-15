"""
FILE: main.py
PURPOSE: Define macros using mkdocs-macros-plugin
"""

import datetime
from git import Repo

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