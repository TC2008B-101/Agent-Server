from pymongo import MongoClient
client = MongoClient('mongodb+srv://dlujan226:Daniel2006_@cluster0.57atq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['db1']
collection = db['youtube']

document = {"name":"daniel", "city":"hermosillo"}
insert_doc = collection.insert_one(document)

print(f"inserted Document ID : {insert_doc.inserted_id}")   
client.close()

