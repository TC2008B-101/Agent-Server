
from pymongo import MongoClient
from dotenv import dotenv_values
import certifi


uri = (MONGO_URI)
client = MongoClient(uri, tlsCAFile=certifi.where())
db = client['db20']
collection = db["Simulation"]