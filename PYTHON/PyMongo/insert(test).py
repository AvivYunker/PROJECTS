import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://pyrisk_user:6310297799@cluster0-udhog.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test1"]

mydict1 = {"_id":15, "first":"Aviv1", "last":"Yunker1", "age":24}
mydict2 = {"_id":16, "first":"Aviv2", "last":"Yunker2", "age":25}
mydict3 = {"_id":17, "first":"Aviv3", "last":"Yunker3", "age":26}



collection.insert_one(mydict1)
collection.insert_one(mydict2)
collection.insert_one(mydict3)