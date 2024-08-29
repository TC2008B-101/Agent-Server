
from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")
uri = config.get("MONGO_URI")
client = MongoClient(uri)
db = client['simulation_database']
collection = db['simulations']