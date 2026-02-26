#!/usr/bin/python3
"""
3-count
"""
import json
import re
import urllib.request


def count_words(subreddit, word_list, counts=None, after=None):
    """Recursively counts keyword occurrences in hot article titles"""
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

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
            title = post.get("data", {}).get("title", "").lower()
            words = re.split(r'[^a-z0-9]+', title)
            for word in counts:
                counts[word] += words.count(word)

        if after is None:
            results = [(k, v) for k, v in counts.items() if v > 0]
            results.sort(key=lambda x: (-x[1], x[0]))
            for word, count in results:
                print("{}: {}".format(word, count))
            return

        return count_words(subreddit, word_list, counts, after)

    except Exception:
        return
