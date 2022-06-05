from tortoise.models import Model
from tortoise import fields


class Twitter(Model):
    tweet_id = fields.BigIntField(pk=True)
    tweet = fields.TextField()
    posted_at = fields.DatetimeField(auto_now_add=False)
    likes = fields.IntField()
    retweets = fields.IntField()
    sentiment_score = fields.FloatField()
    asa_id = fields.TextField()

    class Meta:
        table = "twitterTable"


class RedditPostTable(Model):
    post_id = fields.CharField(pk=True, max_length=10)
    title = fields.TextField()
    text = fields.TextField()
    score = fields.IntField()
    num_of_comments = fields.IntField()
    time_created = fields.DatetimeField(auto_now_add=False)
    url = fields.TextField()
    sentiment_score = fields.FloatField()
    asa_id = fields.TextField()

    class Meta:
        table = "redditPostTable"


class RedditCommentTable(Model):
    comment_id = fields.CharField(pk=True, max_length=10)
    body = fields.TextField()
    score = fields.IntField()
    time_created = fields.DatetimeField(auto_now_add=False)
    sentiment_score = fields.FloatField()
    post_id = fields.ForeignKeyField("models.RedditPostTable", related_name="post_id")

    class Meta:
        table = "redditCommentTable"


class Github(Model):
    repo_name = fields.CharField(pk=True, max_length=255)
    repo_desc = fields.TextField()
    date_created = fields.DatetimeField(auto_now_add=False)
    last_date = fields.DatetimeField(auto_now_add=False)
    language = fields.CharField(max_length=100)
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
