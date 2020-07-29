import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://PyRiskUser:123123321@cluster0-udhog.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["pyrisk_db"]
collection = db["pyrisk_resolutions"]


x = collection.find_one({"_id":0})
print(x["res"][0])
print("And then...")
print(x["res"][1])
