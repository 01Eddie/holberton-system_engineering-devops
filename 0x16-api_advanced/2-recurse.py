#!/usr/bin/python3
"""
2 - Recurse it!
Prototype: def recurse(subreddit, hot_list=[])
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "fetch-scopes by u/EddieHG"}
    params = {
        'after': after,
        'count': count,
        'limit': 100,
        }
    if not subreddit or type(subreddit) is not str:
        return None
    response = requests.get(URL, headers=headers, params=params,
                            allow_redirects=False
                            )

    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        results = response.json().get('data')
        after = results.get('after')
        count += results.get('dist')
        for post in posts:
            hot_list.append(post.get('data').get('title'))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
