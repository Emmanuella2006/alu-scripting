#!/usr/bin/python3
"""
1-top_ten
"""
import json
import urllib.request


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (custom bot 0.1)"}
    )

    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode("utf-8"))
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
