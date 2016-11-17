from models.users import User
import logging
import re

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def validate_user(user):
    first_name_ok = re.match(r'[a-zA-Z]+', user['first_name'])
    last_name_ok = re.match(r'[a-zA-Z]+', user['last_name'])
    username_ok = re.match(r'[a-zA-Z_][a-zA-Z0-9_-]*', user['username'])
    password_ok = re.match(r'[a-zA-Z0-9_-]+', user['password'])
    age_ok = re.match(r'[0-9]+', user['age'])
    gender_ok = re.match(r'[a-zA-Z]+', user['gender'])
    return (
        first_name_ok and last_name_ok and username_ok and password_ok
        and age_ok and gender_ok
    )


class UsersHandler:
    def __init__(self, DB):
        self.db = DB

    def create_user(self, user_data):
        collection = self.db.users
        user = collection.find_one({'username': user_data['username']})
        if not user and validate_user(user_data):
            new_user = User(user_data)
            collection.insert_one(new_user.__dict__)
            logging.info('User Created')
            return True
        logging.warning('User already exists or invalid')
        return False

    def retrieve_users(self):
        collection = self.db.users
        users = collection.find()
        logging.info('All users retrived successfully')
        return users

    def retrieve_user(self, username):
        collection = self.db.users
        user = collection.find_one({'username': username})
        if user:
            logging.info('Users retrived successfully')
            return user
        logging.error('User <{}> does not exists'.format(username))
        return None
