from users_handler import UsersHandler
import pymongo
import logging
import socketio
import eventlet
# from flask import Flask, render_template
from flask import Flask
import json

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
sio = socketio.Server()
app = Flask(__name__)


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
    global client
    print 'Before', data
    data = json.loads(data, encoding='utf-8')
    print 'After', data
    user = data['user']
    db = client.chat
    handler = UsersHandler(db)
    if handler.create_user(user):
        res = {
            'response': 'User created successfully'
        }
    else:
        res = {
            'response': 'Didn\'t create user'
        }
    print res
    sio.emit('signup', json.dumps(res), sid)


client = None

if __name__ == '__main__':
    try:
        client = pymongo.MongoClient(
            "mongodb://root:chat1234@ds135797.mlab.com:35797/chat"
        )
        logging.info("Connected to the data base: {}".format(client.address))
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
