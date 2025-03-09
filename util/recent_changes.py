"""
FILE: recent_changes.py
DESCRIPTION: Experiment to list recent changes to a git repo
"""

from git import Repo

REPO_PATH="../"

repo = Repo(REPO_PATH)
assert not repo.bare