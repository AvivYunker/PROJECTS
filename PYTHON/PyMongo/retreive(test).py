import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://pyrisk_user:6310297799@cluster0-udhog.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test1"]


x = collection.find_one({"_id":15})
y = collection.find_one({"_id":16})
z = collection.find_one({"_id":17})
print(x["_id"])
print(y["_id"])
print(z["_id"])

