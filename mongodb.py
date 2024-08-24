from pymongo import MongoClient

uri = "API-KEY"
client = MongoClient(uri, server_api=pymongo.server_api.ServerA)
db = client['db1']
collection = db['youtube']

document = {"name":"daniel", "city":"hermosillo"}
insert_doc = collection.insert_one(document)

print(f"inserted Document ID : {insert_doc.inserted_id}")   
client.close()