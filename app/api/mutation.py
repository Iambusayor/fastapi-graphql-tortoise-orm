import datetime
from faker import Faker
from typing import List, Optional

import strawberry
from main.models import Github, RedditPostTable, Twitter, RedditCommentTable


fake = Faker()


@strawberry.type
class TwitterValidation:
    tweet: str
    tweet_id: str
    posted_at: datetime.datetime
    likes: int
    retweets: int
    sentiment_score: float
    asa_id: str


@strawberry.type
class PostValidation:
    post_id: str
    title: str
    text: str
    score: int
    num_of_comments: int
    time_created: datetime.datetime
    url: str
    sentiment_score: float
    asa_id: str
    comments: List[str]


@strawberry.type
class GithubValidation:
    repo_name: str
    repo_desc: str
    date_created: datetime.datetime
    last_date: datetime.datetime
    language: str
    no_of_forks: int
    no_of_stars: int
    no_of_watches: int
    no_of_contributors: int
    no_of_commits: int
    issues: int
    pull_requests: int
    asa_id: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def populate_twitter(
        tweet: str,
        asaID: str,
        likes: Optional[int] = fake.random_number(),
        retweet: Optional[int] = fake.random_number(),
    ) -> TwitterValidation:
        values = {
            "tweet_id": fake.ean13(),
            "tweet": tweet,
            "posted_at": fake.date_time_this_decade(),
            "likes": likes,
            "retweets": retweet,
            "sentiment_score": fake.random_choices((0.1, 0.3, 0.5, 0.7, 0.9))[0],
            "asa_id": asaID,
        }
        print(values.values())
        await Twitter.create(**values)
        return TwitterValidation(**values)

    @strawberry.mutation
    async def populate_reddit(
        title: str,
        asaID: str,
        score: int,
        num_comments: int,
        body: Optional[str] = fake.text(),
    ) -> PostValidation:
        values = {
            "post_id": fake.iana_id(),
            "title": title,
            "text": body,
            "score": fake.random_digit_not_null(),
            "num_of_comments": num_comments,
            "time_created": fake.date_time_this_decade(),
            "url": fake.uri(),
            "sentiment_score": fake.random_choices((0.1, 0.3, 0.5, 0.7, 0.9))[0],
            "asa_id": asaID,
            "comments": [fake.sentence() for i in range(num_comments)],
        }
        print(values.values())
        await RedditPostTable.create(**values)
        for i in range(num_comments):
            RedditCommentTable.create(
                comment_id=fake.iana_id(),
                body=values["comments"][i],
                score=fake.random_digit_not_null(),
                time_created=fake.date_time_this_year(),
                sentiment_score=fake.random_choices((0.1, 0.3, 0.5, 0.7, 0.9))[0],
                post_id=values["post_id"],
            )
        return PostValidation(**values)

    @strawberry.mutation
    async def populate_githu(
        repo_name: str,
        repo_desc: str,
        language: str,
        no_of_forks: int,
        no_of_stars: int,
        no_of_watches: int,
        no_of_contributors: int,
        no_of_commits: int,
        issues: int,
        pull_requests: int,
        asa_id: str,
    ) -> GithubValidation:
        values = {
            "repo_name": repo_name,
            "repo_desc": repo_desc,
            "date_created": fake.date_time_this_decade(),
            "last_date": fake.date_time_this_year(),
            "language": language,
            "no_of_forks": no_of_forks,
            "no_of_stars": no_of_stars,
            "no_of_watches": no_of_watches,
            "no_of_contributors": no_of_contributors,
            "no_of_commits": no_of_commits,
            "issues": issues,
            "pull_requests": pull_requests,
            "asa_id": asa_id,
        }
        await Github.create(**values)
        return GithubValidation(**values)
