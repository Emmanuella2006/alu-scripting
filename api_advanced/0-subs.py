#!/usr/bin/python3
"""
0-subs
"""
import urllib.request
import json


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (custom bot 0.1)"}
    )
    
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode("utf-8"))
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
