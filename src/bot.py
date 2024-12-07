import time  
import logging  
from datetime import datetime  
from src.api.coingecko import CoinGeckoAPI  
from src.api.etherscan import EtherscanAPI  
from src.api.twitter import TwitterAPI  
from src.utils.formatter import TweetFormatter  
from src.config import UPDATE_INTERVAL, RETRY_INTERVAL  

# Configure logging  
logging.basicConfig(  
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    handlers=[  
        logging.FileHandler('eth_bot.log'),  
        logging.StreamHandler()  
    ]  
)  

class EthereumBot:  
    def __init__(self):  
        self.twitter = TwitterAPI()  
        self.logger = logging.getLogger(__name__)  

    def run(self):  
        """Main bot loop"""  
        self.logger.info("Starting Ethereum Price & Gas Bot")  

        while True:  
            try:  
                # Fetch data  
                eth_price = CoinGeckoAPI.get_eth_price()  
                gas_data = EtherscanAPI.get_gas_prices()  

                # Format tweet  
                tweet_text = TweetFormatter.format_tweet(eth_price, gas_data)  

                # Post tweet  
                self.twitter.post_tweet(tweet_text)  

                self.logger.info(f"Tweet posted successfully at {datetime.now()}")  

                # Wait for next update  
                time.sleep(UPDATE_INTERVAL)  

            except Exception as e:  
                self.logger.error(f"Error occurred: {str(e)}")  
                self.logger.info(f"Retrying in {RETRY_INTERVAL} seconds...")  
                time.sleep(RETRY_INTERVAL)  

def main():  
    bot = EthereumBot()  
    bot.run()  

if __name__ == "__main__":  
    main()  