import os
from dotenv import load_dotenv
from pymongo import MongoClient

class Mongo:
    def __init__(self):
        load_dotenv()
        self.user = os.environ["MONGO_USER"]
        self.user_password = os.environ["MONGO_USER_PASSWORD"]
        self.db_name = os.environ["DB_NAME"] or "test"
        self.connection_string = f"mongodb://{self.user}:{self.user_password}@cluster0.wq1zp.mongodb.net/{self.db_name}?retryWrites=true&w=majority"
    
    def connect(self):
        self.client = MongoClient(self.connection_string)
        print(">>> Mongo is connected")
