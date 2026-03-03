#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting"}

    response = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")

    for post in data.get("children"):
        print(post.get("data").get("title"))
