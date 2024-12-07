import tweepy  
from src.config import (  
    TWITTER_API_KEY,  
    TWITTER_API_SECRET,  
    TWITTER_ACCESS_TOKEN,  
    TWITTER_ACCESS_TOKEN_SECRET  
)  

class TwitterAPI:  
    def __init__(self):  
        self.auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)  
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)  
        self.api = tweepy.API(self.auth)  

    def post_tweet(self, tweet_text: str) -> None:  
        """Post tweet using Twitter API"""  
        try:  
            self.api.update_status(tweet_text)  
        except Exception as e:  
            raise Exception(f"Error posting tweet: {str(e)}")  