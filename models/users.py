import logging
import bcrypt

class User:
    def __init__(self, user):
        self.first_name = user['first_name']
        self.last_name = user['last_name']
        self.username = user['username']
        self.password = self.__get_pass(user['password'])
        self.age = user['age']
        self.gender = user['gender']

    def __get_pass(self, password):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(password, salt)
        return hashed_pass
