
from pymongo import MongoClient
from dotenv import dotenv_values


uri = ("mongodb+srv://dlujan226:Daniel2006_@cluster0.57atq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(uri)
db = client['db20']
collection = db["Simulation"]