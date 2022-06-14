from . import schema


def test_twitter(client):
    async def get_tweets():

        query = """
        query MyQuery($asaID: String!, $startDate: String) {
    analytics(asaID: $asaID, startDate: $startDate) {
        twitter {
        asaID
        likesTotal
        retweetsTotal
        sentimentScoreMean
        tweetsTotal
        tweets {
            likes
            postedAt
            retweets
            sentimentScore
            tweet
            tweetId
        }
        }
        }
        }
        """

        result = await schema.execute(
            query,
            variable_values={
                "asaID": "ChoiceCoin",
                "startDate": "2021-03-01",
            },
        )

        return result

    result = client.portal.call(get_tweets)

    assert result.errors is None
    assert result.data["analytics"] == {
        "twitter": {
            "asaID": "ChoiceCoin",
            "likesTotal": 68,
            "retweetsTotal": 105,
            "sentimentScoreMean": 0.5333333333333333,
            "tweetsTotal": 6,
            "tweets": {
                "likes": [50, 3, 5, 0, 0, 10],
                "postedAt": [
                    "2021-03-01T00:00:00+00:00",
                    "2021-03-06T00:00:00+00:00",
                    "2021-03-08T00:00:00+00:00",
                    "2021-03-15T00:00:00+00:00",
                    "2021-03-21T00:00:00+00:00",
                    "2021-10-02T06:05:03+00:00",
                ],
                "retweets": [32, 12, 45, 2, 4, 10],
                "sentimentScore": [0.7, 0.4, 0.6, 0.3, 0.3, 0.9],
                "tweet": [
                    "Hey first tweet! Great!",
                    "Hey! Second tweet!",
                    "Third tweet! Just there",
                    "Bad!!",
                    "Bad, not good!",
                    "Heyyy!!First mutation of ChoiceCoin",
                ],
                "tweetId": [
                    "1213245124",
                    "1611245324",
                    "1213245107",
                    "1213245891",
                    "4321451234",
                    "7641768731718",
                ],
            },
        }
    }


def test_github(client):
    async def get_github():
        query = """query MyQuery ($asaID: String!){
                          analytics(asaID: $asaID) {
                            github {
                              asaID
                              commitsTotal
                              contributorsTotal
                              forksTotal
                              isssuesTotal
                              language
                              pullRequestTotal
                              starsTotal
                              watchesTotal
                              repos {
                                dateCreated
                                issues
                                language
                                lastPushDate
                                noOfCommits
                                noOfContributors
                                noOfForks
                                noOfStars
                                noOfWatches
                                pullRequests
                                repoDesc
                                repoName
                              }
                            }
                          }
                        }
                        """

        result = await schema.execute(
            query,
            variable_values={
                "asaID": "ChoiceCoin",
            },
        )

        return result

    result = client.portal.call(get_github)

    assert result.errors is None
    assert result.data["analytics"] == {
        "github": {
            "asaID": "ChoiceCoin",
            "commitsTotal": 54,
            "contributorsTotal": 31,
            "forksTotal": 12,
            "isssuesTotal": 21,
            "language": ["rust", "ruby", "scala"],
            "pullRequestTotal": 71,
            "starsTotal": 124,
            "watchesTotal": 52,
            "repos": {
                "dateCreated": [
                    "2021-08-05T00:00:00+00:00",
                    "2021-02-21T00:00:00+00:00",
                    "2022-04-30T00:00:00+00:00",
                ],
                "issues": [5, 11, 5],
                "language": ["rust", "ruby", "scala"],
                "lastPushDate": [
                    "2022-03-01T00:00:00+00:00",
                    "2022-04-23T00:00:00+00:00",
                    "2022-05-31T00:00:00+00:00",
                ],
                "noOfCommits": [14, 20, 20],
                "noOfContributors": [7, 4, 20],
                "noOfForks": [6, 3, 3],
                "noOfStars": [24, 50, 50],
                "noOfWatches": [22, 12, 18],
                "pullRequests": [13, 41, 17],
                "repoDesc": ["desc -01", "desc 02", "desc 03"],
                "repoName": ["repo-00", "repo-02", "repo-03"],
            },
        }
    }


def test_reddit(client):
    async def get_reddit():
        query = """query MyQuery ($asaID: String!, $startDate: String){
                          analytics(asaID: $asaID, startDate: $startDate) {
                            reddit {
                                asaID
                                numOfComments
                                postId
                                score
                                sentimentScore
                                text
                                timeCreated
                                title
                                url
                                comments {
                                  body
                                  commentId
                                  postId
                                  score
                                  sentimentScore
                                  timeCreated
                                    }
                                }
                            }
                        }
                        """

        result = await schema.execute(
            query,
            variable_values={"asaID": "YieldlyFinance", "startDate": "2021-01-01"},
        )

        return result

    result = client.portal.call(get_reddit)

    assert result.errors is None
    assert result.data["analytics"] == {
        "reddit": {
            "asaID": "YieldlyFinance",
            "numOfComments": [5, 3],
            "postId": ["auiwes4", "6325337"],
            "score": [41, 8],
            "sentimentScore": [0.8, 0.9],
            "text": [
                "Heyy! Yo! This coin is to the moon !!",
                "Service spring night live throw. Support place floor office star.\nRisk bad around want room. Line throughout cover. She form action wait hear.",
            ],
            "timeCreated": ["2021-02-28T00:00:00+00:00", "2022-02-21T18:52:28+00:00"],
            "title": ["Great Post", "Steday grinding! Steady update!!"],
            "url": ["getpost.com", "http://www.hawkins-escobar.com/main.html"],
            "comments": {
                "body": [
                    "comment 1",
                    "comment 2",
                    "comment 3",
                    "comment 4",
                    "comment 5",
                ],
                "commentId": [
                    "iegedo3e8",
                    "iegeddfde8",
                    "iegd3e4548",
                    "i334edo3e8",
                    "iejjed3e8",
                ],
                "postId": ["auiwes4", "auiwes4", "auiwes4", "auiwes4", "auiwes4"],
                "score": [50, 3, 5, 0, 0],
                "sentimentScore": [0.7, 0.4, 0.6, 0.3, 0.3],
                "timeCreated": [
                    "2021-03-01T00:00:00+00:00",
                    "2021-03-06T00:00:00+00:00",
                    "2021-03-08T00:00:00+00:00",
                    "2021-03-15T00:00:00+00:00",
                    "2021-03-21T00:00:00+00:00",
                ],
            },
        }
    }
