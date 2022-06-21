from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Twitter(Model):
    """
    Twitter model
    """

    tweet_id = fields.BigIntField(pk=True)
    tweet = fields.TextField()
    posted_at = fields.DatetimeField(auto_now_add=False)
    day_of_week = fields.IntField()
    day = fields.IntField()
    month = fields.IntField()
    year = fields.IntField()
    hr = fields.IntField()
    mins = fields.IntField()
    likes = fields.IntField()
    retweets = fields.IntField()
    sentiment_score = fields.FloatField()
    asa_id = fields.TextField()

    class Meta:
        table = "twitterTable"

    class PydanticMeta:
        exclude = ["asa_id"]


Twitter_Pydantic = pydantic_model_creator(
    Twitter,
    name="twitterPydantic",
)


class RedditPostTable(Model):
    post_id = fields.CharField(pk=True, max_length=255)
    title = fields.TextField()
    text = fields.TextField()
    score = fields.IntField()
    num_of_comments = fields.IntField()
    time_created = fields.DatetimeField(auto_now_add=False)
    day_of_week = fields.IntField()
    day = fields.IntField()
    month = fields.IntField()
    year = fields.IntField()
    hr = fields.IntField()
    url = fields.TextField()
    sentiment_score = fields.FloatField()
    asa_id = fields.TextField()

    class Meta:
        table = "redditPostTable"

    class PydanticMeta:
        exclude = ["asa_id"]


Post_Pydantic = pydantic_model_creator(
    RedditPostTable,
    name="postsPydantic",
)


class RedditCommentTable(Model):
    comment_id = fields.CharField(pk=True, max_length=255)
    body = fields.TextField()
    score = fields.IntField()
    time_created = fields.DatetimeField(auto_now_add=False)
    day_of_week = fields.IntField()
    day = fields.IntField()
    month = fields.IntField()
    year = fields.IntField()
    hr = fields.IntField()
    sentiment_score = fields.FloatField()
    post = fields.ForeignKeyField("models.RedditPostTable", related_name="parent_id")

    class Meta:
        table = "redditCommentTable"


Comment_Pydantic = pydantic_model_creator(
    RedditCommentTable,
    name="commentsPydantic",
)


class Github(Model):
    repo_name = fields.CharField(pk=True, max_length=255)
    repo_desc = fields.TextField()
    date_created = fields.DatetimeField(auto_now_add=False)
    dc_day_of_week = fields.IntField()
    dc_day = fields.IntField()
    dc_month = fields.IntField()
    dc_year = fields.IntField()
    dc_hr = fields.IntField()
    last_push_date = fields.DatetimeField(auto_now_add=False)
    lp_day_of_week = fields.CharField(max_length=255)
    lp_day = fields.IntField()
    lp_month = fields.IntField()
    lp_year = fields.IntField()
    lp_hr = fields.IntField()
    lp_language = fields.CharField(max_length=100)
    no_of_forks = fields.IntField()
    no_of_stars = fields.IntField()
    no_of_watches = fields.IntField()
    no_of_contributors = fields.IntField()
    no_of_commits = fields.IntField()
    issues = fields.IntField()
    pull_requests = fields.IntField()
    asa_id = fields.TextField()

    class Meta:
        table = "githubTable"

    class PydanticMeta:
        exclude = ["asa_id"]


Github_Pydantic = pydantic_model_creator(
    Github,
    name="githubPydantic",
)
