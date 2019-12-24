
# Adding a new user in DB as we don't have a user creation module

from pymongo import MongoClient, CursorType, ASCENDING, DESCENDING
from bson import json_util, ObjectId
from bson.int64 import Int64

# DB links for user collection
client = MongoClient("mongodb://localhost:27017")
database = client["local"]
collection = database["pokedexDB"]

u = {
    "user1": {
        "new": {
            "category1": [],
            "category2": []
        },
        "old": {
            "category1": [],
            "category2": []
        }
    }
}


collection.insert_one(u)
