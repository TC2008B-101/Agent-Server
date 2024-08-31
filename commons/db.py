
from pymongo import MongoClient
from dotenv import dotenv_values
import certifi

uri = ("mongodb+srv://Cluster71888:Shepard691.@cluster71888.kt6vp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster71888")
client = MongoClient(uri, tlsCAFile=certifi.where())
db = client['db20']
collection = db["Simulation"]