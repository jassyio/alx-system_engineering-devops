#!/usr/bin/python3
"""
Function that query the Reddit API and prints
top ten hot posts of a subreddit
"""
from requests import get

def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    response = get(url, headers=user_agent, params=params)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json()
        my_data = results['data']['children']

        for post in my_data:
            print(post['data']['title'])

    except Exception as e:
        print(f"Error: {e}")
        print("None")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
