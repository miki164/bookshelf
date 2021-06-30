import pymongo
import json

print("Reading secrets")
secrets = open("secret.json")
secrets = json.load(secrets)

print("Connecting with DB")
client = pymongo.MongoClient(secrets['connection-string'])
db = client.bookshelf

print("Creating collections")
db.create_collection("books")
db.create_collection("users")

print("Creating indexes")
db.books.create_index([("location", pymongo.GEOSPHERE)])

print("DB setted up")
