from uu import encode
import pymongo
import os
from dotenv import load_dotenv
import hashlib
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


myclient = pymongo.MongoClient(DATABASE_URL)
mydb = myclient["companyname"]
mycol = mydb["users"]


def add_user(name, username, password, email):

    mydoc = mycol.find_one({"username": username})

    if mydoc:
        return 'user exist'

    else:

        salt = "5gz"
        dataBase_password = password+salt
        hashed = hashlib.md5(dataBase_password.encode())

        mycol.insert_one({"name": name, "username": username,
                         "password": hashed.hexdigest(), "email": email})
        return 'user created!'


def login_user(username, password):
    salt = "5gz"
    dataBase_password = password+salt
    hashed = hashlib.md5(dataBase_password.encode())
    mydoc = mycol.find_one(
        {"username": username, "password": hashed.hexdigest()})
    if mydoc:
        return mydoc
    else:
        return 'user not found!'

