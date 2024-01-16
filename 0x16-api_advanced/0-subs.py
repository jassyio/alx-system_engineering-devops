#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers. """

    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        subscribers = data.get('subscribers', 0)
        return subscribers
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to query.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"The subreddit '{subreddit}' has {subscribers} subscribers.")
