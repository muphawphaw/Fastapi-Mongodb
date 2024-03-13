from pymongo import MongoClient
db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection.person
collection = db["users"]