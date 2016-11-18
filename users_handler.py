# -*- coding: UTF-8 -*-

from models.users import User
import logging
import re

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def validate_user(user):
    pat_name = re.compile(r'^[a-zA-Záéíóúñ]+$', re.UNICODE)
    first_name_ok = pat_name.match(user['first_name'].encode('utf-8'))
    last_name_ok = pat_name.match(user['last_name'].encode('utf-8'))

    pat_username = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_-]*$', re.UNICODE)
    username_ok = pat_username.match(user['username'].encode('utf-8'))

    pat_password = re.compile(r'^[a-zA-Z0-9_-]+$', re.UNICODE)
    password_ok = pat_password.match(user['password'].encode('utf-8'))

    pat_age = re.compile(r'^[0-9]+$', re.UNICODE)
    age_ok = pat_age.match(user['age'].encode('utf-8'))

    gender_ok = user['gender'] == 'M' or user['gender'] == 'F'

    print 'fn', first_name_ok
    print 'ln', last_name_ok
    print 'un', username_ok
    print 'p', password_ok
    print 'a', age_ok
    print 'g', gender_ok
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
        if user:
            logging.warning('User already exists')
            return 'User already exists'
        elif not validate_user(user_data):
            logging.warning('User data invalid')
            return 'User data invalid'
        new_user = User(user_data)
        collection.insert_one(new_user.__dict__)
        logging.info('User created')
        return 'User created successfully'

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
