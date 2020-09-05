import os
from dotenv import load_dotenv
from tiingo import TiingoClient

config = {}
config['session'] = True
load_dotenv()
config['api_key'] = os.getenv("API")
client = TiingoClient(config)
