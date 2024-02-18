from requests_oauthlib import OAuth1Session

def post_tweet(tweet_text):
    # Your consumer keys and access tokens
    consumer_key = 'd0k61MNQLHYHMsEpCxPLLVFnK'
    consumer_secret = 'JUzZOoNsOaq1E55lidvrGzZdbVqTWzAbSTHgRlaByBsGXbhCPq'
    access_token = '1759005396788731905-6YjvkWBUZlPmkqoK1YEuBcNnr9cOfE'
    access_token_secret = 'lbsnnthJS50pOO2bWfUIlS8OjooVIJtfzOvPSi7zFnPTt'

    # Creating an OAuth1Session object
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    # The URL for creating a Tweet
    tweet_url = 'https://api.twitter.com/2/tweets'

    # The payload of the tweet, using the parameter tweet_text
    tweet_payload = {"text": tweet_text}

    # Making the POST request to create a tweet
    response = oauth.post(tweet_url, json=tweet_payload)

    # Checking if the request was successful
    if response.status_code == 201:
        print("Tweet created successfully!")
        # Print the response from Twitter
        print(response.json())
    else:
        print(f"Failed to create tweet. Status code: {response.status_code}, Response text: {response.text}")



# Example usage:
post_tweet("hello world. This is a test message... again :)")
