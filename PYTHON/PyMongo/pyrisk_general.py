import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://pyrisk_user:6310297799@cluster0-udhog.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_general"]

x = collection.find_one({"_id":0})
print(x["name"])