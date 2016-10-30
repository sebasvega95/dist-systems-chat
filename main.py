from users_handler import UsersHandler
import pymongo
import logging
import sys

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

try:
    client = pymongo.MongoClient("mongodb://root:chat1234@ds135797.mlab.com:35797/chat")
    logging.info("Connected to the data base: {}".format(client.address))
except pymongo.errors.ConnectionFailure, e:
    logging.error("Could not connect to DB server: {}".format(e))

user_data = {
    'first_name': 'Leiver',
    'last_name': 'Campeon',
    'username' : 'leiverandres',
    'password' : '1234',
    'age' : '21',
    'gender': 'male'
}

db = client.chat
handler = UsersHandler(db)
handler.create_user(user_data)
