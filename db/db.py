from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Database:
    def __init__(self, uri):
        self.uri = "mongodb+srv://gdanylov:bhHrg8f5H9T1NIsM@cluster0.vn18sgp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    def connect(self):
        try:
            client = MongoClient(self.uri, server_api=ServerApi('1'))
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except Exception as e:
            print(e)
