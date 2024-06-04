#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, header=header, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
