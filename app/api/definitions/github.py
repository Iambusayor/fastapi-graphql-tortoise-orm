from datetime import datetime
from typing import List

import strawberry


@strawberry.type
class Github:
    repo_name: str
    repo_desc: str
    date_created: datetime
    last_push_date: datetime
    language: str
    no_of_forks: int
    no_of_stars: int
    no_of_watches: int
    no_of_contributors: int
    no_of_commits: int
    issues: int
    pull_requests: int


@strawberry.type
class GithubOverAll:
    asaID: str
    language: List[str]
    forksTotal: int
    starsTotal: int
    watchesTotal: int
    contributorsTotal: int
    commitsTotal: int
    isssuesTotal: int
    pullRequestTotal: int
    repos: List[Github]
