from pymongo import MongoClient

class AgesMongo(object):
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client.flask
        self.ages = self.db.ages

    def insert_age(self, username, age):
        insertion_dict = {"username":username, "age":age}
        self.ages.insert_many([insertion_dict])

    def get_age(self, username):
        try:
            find_dict = {"username":username}
            return self.ages.find_one(find_dict)["age"]
        except TypeError:
            return -1