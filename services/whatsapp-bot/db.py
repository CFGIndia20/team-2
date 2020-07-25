from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.vz4wz.mongodb.net/cfg?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('cfg')
user_collection = pymongo.collection.Collection(db, 'users')