#!/usr/bin/python3
"""
2-recurse
"""
import urllib.request
import json


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot articles for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (custom bot 0.1)"}
    )

    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode("utf-8"))
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after")

        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        if after is None:
            return hot_list if hot_list else None

        return recurse(subreddit, hot_list, after)

    except Exception:
        return None
