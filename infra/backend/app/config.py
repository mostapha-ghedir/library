# app/config.py
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb_service:27017")
MONGO_DB = os.getenv("MONGO_DB", "libraryDB")