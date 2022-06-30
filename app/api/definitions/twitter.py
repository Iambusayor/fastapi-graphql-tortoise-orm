from typing import List
import strawberry
from datetime import datetime


@strawberry.type
class Twitter:
    tweet: str
    posted_at: datetime
    likes: int
    retweets: int
    sentiment_score: float


@strawberry.type
class TwitterOverAll:
    asaID: str
    tweetsTotal: int
    likesTotal: int
    retweetsTotal: int
    sentimentScoreMean: float
    tweets: List[Twitter]
