#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    # Define the User-Agent to avoid 'Too Many Requests' errors
    headers = {'User-Agent': 'my_reddit_app/0.1'}
    
    # Build the URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Return the number of subscribers
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If status code is not 200, the subreddit may be invalid
            return 0
            
    except requests.RequestException:
        # Handle any request-related exceptions
        return 0

# Example usage
subreddit_name = 'python'
print(f"Number of subscribers in r/{subreddit_name}: {number_of_subscribers(subreddit_name)}")

