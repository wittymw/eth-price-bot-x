from datetime import datetime  
from typing import Dict  

class TweetFormatter:  
    @staticmethod  
    def format_tweet(eth_price: float, gas_data: Dict) -> str:  
        """Format the tweet with current data"""  
        current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')  

        tweet = f"""🔄 Ethereum Update ({current_time})  

💰 ETH Price: ${eth_price:,.2f}  
⛽ Gas Prices (Gwei):  
   Safe Low: {gas_data['SafeGasPrice']}  
   Standard: {gas_data['ProposeGasPrice']}  
   Fast: {gas_data['FastGasPrice']}  

#Ethereum #ETH #GasPrice"""  

        return tweet  