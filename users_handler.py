from models.users import User

class UsersHandler:
    def __init__(self, DB):
        self.db = DB

    def create_user(self, user_data):
        collection = self.db.users
        new_user = User(user_data)
        collection.insert_one(new_user.__dict__)
