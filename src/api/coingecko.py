import requests  
from typing import Dict  

class CoinGeckoAPI:  
    BASE_URL = "https://api.coingecko.com/api/v3"  

    @staticmethod  
    def get_eth_price() -> float:  
        """Fetch current ETH price from CoinGecko API"""  
        try:  
            url = f"{CoinGeckoAPI.BASE_URL}/simple/price?ids=ethereum&vs_currencies=usd"  
            response = requests.get(url)  
            response.raise_for_status()  
            data = response.json()  
            return data['ethereum']['usd']  
        except Exception as e:  
            raise Exception(f"Error fetching ETH price: {str(e)}")  