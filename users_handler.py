from models.users import User
import logging

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

class UsersHandler:
    def __init__(self, DB):
        self.db = DB

    def create_user(self, user_data):
        collection = self.db.users
        user = collection.find_one({"username": user_data["username"]})
        if not user:
            new_user = User(user_data)
            collection.insert_one(new_user.__dict__)
            logging.info("User Created")
            return True
        logging.warning("User already exists")
        return False

    def retrieve_users(self):
        collection= self.db.users
        users = collection.find()
        logging.info("All users retrived successfully")
        return users

    def retrieve_user(self, username):
        collection = self.db.users
        user = collection.find_one({'username': username})
        if user:
            logging.info("Users retrived successfully")
            return user
        logging.error("User <{}> does not exists".format(username))
        return None
