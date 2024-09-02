
from pymongo import MongoClient
from dotenv import dotenv_values
import certifi

uri = ("mongodb+srv://dlujan226:Daniel2006_@cluster0.57atq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(uri, tlsCAFile=certifi.where())
db = client['db20']
collection = db["simulations"]