import strawberry
import datetime
from dacite import from_dict
from typing import Optional
from .definitions import twitter, reddit, github
from main.models import (
    Twitter,
    RedditCommentTable,
    RedditPostTable,
    Github,
)


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


@strawberry.type
class All:
    twitter: twitter.TwitterOverAll
    reddit: reddit.Reddit
    github: github.GithubOverAll


async def get_tweets(
    asaID: str,
    startDate: str,
    endDate: str,
) -> twitter.TwitterOverAll:
    result = (
        await Twitter.filter(asa_id=asaID)
        .filter(posted_at__range=[startDate, endDate])
        .values(
            "tweet_id", "tweet", "posted_at", "likes", "retweets", "sentiment_score"
        )
    )
    if not result:
        raise Exception(
            f"No data available for this ASA: '{asaID}'.Check ASA-ID and dates are valid!"
        )
    result_ = {key: [i[key] for i in result] for key in result[0]}
    result = [from_dict(data_class=twitter.Twitter, data=x) for x in result]
    print(result)
    return twitter.TwitterOverAll(
        asaID=asaID,
        tweetsTotal=len(result_["tweet"]),
        likesTotal=sum(result_["likes"]),
        retweetsTotal=sum(result_["retweets"]),
        sentimentScoreMean=sum(result_["sentiment_score"])
        / len(result_["sentiment_score"]),
        tweets=result,
    )


async def get_reddit(
    asaID: str,
    startDate: str,
    endDate: str,
) -> reddit.Reddit:
    post_result = (
        await RedditPostTable.filter(asa_id=asaID)
        .filter(time_created__range=[startDate, endDate])
        .values(
            "post_id",
            "title",
            "text",
            "score",
            "num_of_comments",
            "time_created",
            "url",
            "sentiment_score",
        )
    )
    if not post_result:
        raise Exception(
            f"No data available for this ASA: '{asaID}'. Check ASA-ID and dates are valid!"
        )
    post_result = {key: [i[key] for i in post_result] for key in post_result[0]}
    post_result = AttrDict(post_result)
    post_result_id = post_result["post_id"][0]
    comment_result = await RedditCommentTable.filter(post_id=post_result_id).values(
        "comment_id",
        "body",
        "score",
        "time_created",
        "sentiment_score",
        "post_id",
    )
    print(comment_result)
    comment_result = {
        key: [i[key] for i in comment_result] for key in comment_result[0]
    }

    comment_result = AttrDict(comment_result)
    # if not comment_result:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail=f"Error retrieving comments!"
    #     )
    return reddit.Reddit(
        post_id=post_result.post_id,
        title=post_result.title,
        text=post_result.text,
        score=post_result.score,
        num_of_comments=post_result.num_of_comments,
        time_created=post_result.time_created,
        url=post_result.url,
        sentiment_score=post_result.sentiment_score,
        asaID=asaID,
        comments=comment_result,
    )


async def get_github(asaID: str) -> github.GithubOverAll:
    result = await Github.filter(asa_id=asaID).values(
        "repo_name",
        "repo_desc",
        "date_created",
        "last_push_date",
        "language",
        "no_of_forks",
        "no_of_stars",
        "no_of_watches",
        "no_of_contributors",
        "no_of_commits",
        "issues",
        "pull_requests",
    )
    if not result:
        raise Exception(
            f"No data available for this ASA: '{asaID}'.Check ASA-ID and dates are valid!"
        )
    result_ = {key: [i[key] for i in result] for key in result[0]}
    result = [from_dict(data_class=github.Github, data=x) for x in result]
    return github.GithubOverAll(
        asaID=asaID,
        language=result_["language"],
        forksTotal=sum(result_["no_of_forks"]),
        starsTotal=sum(result_["no_of_stars"]),
        watchesTotal=sum(result_["no_of_watches"]),
        contributorsTotal=sum(result_["no_of_contributors"]),
        commitsTotal=sum(result_["no_of_commits"]),
        isssuesTotal=sum(result_["issues"]),
        pullRequestTotal=sum(result_["pull_requests"]),
        repos=result,
    )


@strawberry.type
class Query:
    @strawberry.field
    def analytics(
        self,
        asaID: str,
        startDate: Optional[str] = datetime.date.today() - datetime.timedelta(days=30),
        endDate: Optional[str] = datetime.date.today(),
    ) -> All:
        return All(
            twitter=get_tweets(asaID=asaID, startDate=startDate, endDate=endDate),
            reddit=get_reddit(asaID=asaID, startDate=startDate, endDate=endDate),
            github=get_github(asaID=asaID),
        )
