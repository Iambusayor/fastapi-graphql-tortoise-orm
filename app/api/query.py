import strawberry
import datetime
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
    result = {key: [i[key] for i in result] for key in result[0]}
    result = AttrDict(result)
    # if not result:
    #     return f"not found!"
    print(result)
    return twitter.TwitterOverAll(
        asaID=asaID,
        tweetsTotal=len(result["tweet"]),
        likesTotal=sum(result["likes"]),
        retweetsTotal=sum(result["retweets"]),
        sentimentScoreMean=sum(result["sentiment_score"])
        / len(result["sentiment_score"]),
        tweets=result,
    )


async def get_reddit(
    asaID: str,
    startDate: str,
    endDate: str,
) -> reddit.Reddit:
    post_result = (
        await RedditPostTable.filter(asa_id=asaID)
        .filter(posted_at__range=[startDate, endDate])
        .values()
    )
    print(post_result)
    post_result = {key: [i[key] for i in post_result] for key in post_result[0]}
    post_result = AttrDict(post_result)
    # if not post_result:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail=f"{asaID} not found!"
    #     )
    post_result_id = post_result["post_id"][0]
    comment_result = await RedditCommentTable.filter(post_id=post_result_id).values()
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
    result = await Github.filter(asa_id=asaID).values()
    result = {key: [i[key] for i in result] for key in result[0]}
    result = AttrDict(result)
    # if not result:
    # raise HTTPException(
    # status_code=status.HTTP_404_NOT_FOUND, detail=f"{asaID} not found!"
    # )
    return github.GithubOverAll(
        asaID=asaID,
        language=result.language,
        forksTotal=sum(result.no_of_forks),
        starsTotal=sum(result.no_of_stars),
        watchesTotal=sum(result.no_of_watches),
        contributorsTotal=sum(result.no_of_contributors),
        commitsTotal=sum(result.no_of_commits),
        isssuesTotal=sum(result.issues),
        pullRequestTotal=sum(result.pull_requests),
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
