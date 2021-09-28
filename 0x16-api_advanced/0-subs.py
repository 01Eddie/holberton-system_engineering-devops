#!/usr/bin/python3
"""
1-how many subs?
prototype: number_of_subscribers(subreddit)
"""
import requests


def number_of_subscribers(subreddit):
    response = requests.get('https://www.reddit.com/r/{}/about.json'
                            .format(subreddit),
                            headers={"User-Agent": "fetch-scopes by u/EddieHG"}
                            ).json()
    if not subreddit and type(subreddit) is not str:
        return 0
    subscribers = response.get('data', {}).get('subscribers', 0)
    return subscribers
