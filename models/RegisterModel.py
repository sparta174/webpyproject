import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.CodeWizard
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

        id = self.Users.insert({
            "username": data.username, "name": data.name,
            "password": hashed, "email": data.email
                                })
        print("uid is", id)
        myuser = self.Users.find_one({"username": data.username})
        # print(myuser)

        if bcrypt.checkpw("avocado1".encode(), myuser["password"]):
            print("this matches")
