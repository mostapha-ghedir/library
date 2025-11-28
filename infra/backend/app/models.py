from pymongo import MongoClient
import os

mongo_url = os.getenv("MONGO_URL", "mongodb://mongodb:27017/librarydb")
client = MongoClient(mongo_url)
db = client.get_database()

books_collection = db["books"]