# -*- coding: UTF-8 -*-

from users_handler import UsersHandler
import pymongo
import logging
import socketio
import eventlet
from flask import Flask
import json
import bcrypt
from random import choice
from string import ascii_uppercase


def gen_token():
    return ''.join(choice(ascii_uppercase) for i in range(12))

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
sio = socketio.Server()
app = Flask(__name__)
logged_users = {}

# @app.route('/')
# def index():
#     """Serve the client-side application."""
#     return render_template('index.html')


@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)


@sio.on('message')
def message(sid, data):
    print('message ', data)
    sio.emit('news', '1.2 en distribuidos para el que lo lea', sid)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('signup')
def signup(sid, data):
    global handler
    data = json.loads(data)
    user = data['user']
    print user
    user_res = handler.create_user(user)
    res = {}
    if user_res == 'User created successfully':
        res['response'] = True
    else:
        res['response'] = False
    res['message'] = user_res
    sio.emit('signup', json.dumps(res), sid)


@sio.on('login')
def login(sid, data):
    global handler, logged_users
    data = json.loads(data)
    user = data['user']
    user_res = handler.retrieve_user(user['username'])
    if user_res:
        print user['password'], user_res['password']
        password = user['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, user_res['password'].encode('utf-8'))
        token = gen_token()
        logged_users[token] = sid
        if hashed == user_res['password']:
            res = {
                'response': True,
                'message': 'Login succesful',
                'token': token
            }
        else:
            res = {
                'response': False,
                'message': 'Incorrect password'
            }
    else:
        res = {
            'response': False,
            'message': 'User doesn\'t exists'
        }
    sio.emit('login', json.dumps(res), sid)


@sio.on('back')
def back(sid, data):
    global logged_users
    data = json.loads(data)
    logged_users[data['token']] = sid
    print 'USERS', logged_users


if __name__ == '__main__':
    try:
        client = pymongo.MongoClient(
            "mongodb://root:chat1234@ds135797.mlab.com:35797/chat"
        )
        logging.info("Connected to the data base: {}".format(client.address))
        db = client.chat
        handler = UsersHandler(db)
    except pymongo.errors.ConnectionFailure, e:
        logging.error("Could not connect to DB server: {}".format(e))

    # wrap Flask application with socketio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)


#
# # user_data = {
# #     'first_name': 'Leiver',
# #     'last_name': 'Campeon',
# #     'username': 'leiverandres',
# #     'password': '1234',
# #     'age': '21',
# #     'gender': 'male'
# # }
#
