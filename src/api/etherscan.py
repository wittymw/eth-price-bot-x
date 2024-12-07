import requests  
from typing import Dict  
from src.config import ETHERSCAN_API_KEY  

class EtherscanAPI:  
    BASE_URL = "https://api.etherscan.io/api"  

    @staticmethod  
    def get_gas_prices() -> Dict:  
        """Fetch current gas prices from Etherscan API"""  
        try:  
            url = f"{EtherscanAPI.BASE_URL}?module=gastracker&action=gasoracle&apikey={ETHERSCAN_API_KEY}"  
            response = requests.get(url)  
            response.raise_for_status()  
            data = response.json()  
            return data['result']  
        except Exception as e:  
            raise Exception(f"Error fetching gas prices: {str(e)}")  