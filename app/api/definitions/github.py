from datetime import datetime
from typing import List

import strawberry


@strawberry.type
class Github:
    repo_name: List[str]
    repo_desc: List[str]
    date_created: List[datetime]
    last_push_date: List[datetime]
    language: List[str]
    no_of_forks: List[int]
    no_of_stars: List[int]
    no_of_watches: List[int]
    no_of_contributors: List[int]
    no_of_commits: List[int]
    issues: List[int]
    pull_requests: List[int]


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
    repos: Github
