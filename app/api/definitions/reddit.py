from datetime import datetime
from typing import List
import strawberry

from main.models import RedditPostTable as PostModel, RedditCommentTable as CommentModel


@strawberry.type
class Comments:
    comment_id: List[str]
    body: List[str]
    score: List[int]
    time_created: List[datetime]
    sentiment_score: List[float]
    post_id: List[str]


@strawberry.type
class Reddit:
    post_id: List[str]
    title: List[str]
    text: List[str]
    score: List[int]
    num_of_comments: List[int]
    time_created: List[datetime]
    url: List[str]
    sentiment_score: List[float]
    asaID: str
    comments: Comments
