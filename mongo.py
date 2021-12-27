import os
from dotenv import load_dotenv
from pymongo import MongoClient, server
from pprint import pprint

class Mongo:
    def __init__(self):
        load_dotenv(override=True)
        self.user = os.environ["MONGO_USER"]
        self.user_password = os.environ["MONGO_USER_PASSWORD"]
        self.db_name = os.environ["DB_NAME"]
        self.connection_string = f"mongodb+srv://{self.user}:{self.user_password}@cluster0.wq1zp.mongodb.net/{self.db_name}?retryWrites=true&w=majority"
        self.client = MongoClient(self.connection_string)
        self.db = self.client.test

    def add_user(self, user):
        users = self.db.users
        result = users.insert_one(user)
        return result
    

