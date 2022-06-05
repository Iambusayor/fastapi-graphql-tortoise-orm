from typing import List
import strawberry
from datetime import datetime


@strawberry.type
class Twitter:
    tweet_id: List[str]
    tweet: List[str]
    posted_at: List[datetime]
    likes: List[int]
    retweets: List[int]
    sentiment_score: List[float]

    # @classmethod
    # def from_instance(cls, instance: dict):
    #     return cls(
    #         tweet_id=instance["tweet_id"],
    #         tweet=instance["tweet"],
    #         postedAt=instance["postedAt"],
    #         likes=instance["likes"],
    #         retweets=instance["retweets"],
    #         sentimentScore=instance["sentimentScore"],
    #     )


@strawberry.type
class TwitterOverAll:
    asaID: str
    tweetsTotal: int
    likesTotal: int
    retweetsTotal: int
    sentimentScoreMean: float
    tweets: Twitter

    # @strawberry.field
    # def tweets(self) -> Twitter:
    # return Twitter.from_instance(self.instance.tweets)
