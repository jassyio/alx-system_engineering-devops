#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except Exception as e:
        return 0

if __name__ == "__main__":
    pass  # This file is intended to be used as a module, not executed directly
