#!/usr/bin/python3
"""
1 - Top Ten
Prototype: def top_ten(subreddit)
"""
import requests


def top_ten(subreddit):
    if not subreddit or type(subreddit) is not str:
        print(None)
    response = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                            .format(subreddit),
                            headers={"User-Agent": "fetch-scopes by u/EddieHG"}
                            )
    posts = response.json().get('data', {}).get('children', None)

    if response.status_code == 200:
        for post in posts:
            print(post.get('data', {}).get('title', None))
    print(None)
