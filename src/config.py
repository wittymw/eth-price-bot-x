import os  
from dotenv import load_dotenv  

load_dotenv()  

# Twitter API credentials  
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')  
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')  
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')  
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')  

# Etherscan API  
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')  

# Update interval (15 minutes)  
UPDATE_INTERVAL = 900  # seconds  
RETRY_INTERVAL = 300  # 5 minutes in case of error  