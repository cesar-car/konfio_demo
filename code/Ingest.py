import requests

class CoinGeckoClient:
    def __init__(self, api_key, version="demo"):
        self.api_key = api_key
        if version not in ["demo", "pro"]:
            raise ValueError("version must be 'pro' or 'demo'")
        if version == "demo":
            self.main_url = "https://api.coingecko.com/api/v3/" 
            self.header = "x-cg-api-key"
        else:
            self.main_url = "https://pro-api.coingecko.com/api/v3/" 
            self.header = "x-cg-pro-api-key"
    
    def query_endpoint(self, endpoint, path_params=None, query_params=None):
        if path_params:
            endpoint = endpoint.format(**path_params)
        url = self.main_url + endpoint
        headers = {self.header: self.api_key}
        try:
            response = requests.get(url, headers=headers, params=query_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        
        



    

