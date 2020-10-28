'''this is the main driver file'''
import os
import flask
import flask_socketio
from os.path import join, dirname
from dotenv import load_dotenv
import flask_sqlalchemy

import bot_message as bot
import bot_build as botcommand
import urlparse as url_parse
import urlparse
from flask import request
import connected_users

LIST_OF_CONNECTED_USERS = connected_users.Connected()
MESSAGE_RECEIVED_CHANNEL = 'message received'
USER_UPDATE_CHANNEL = 'user updated'

APP = flask.Flask(__name__)

SOCKETIO = flask_socketio.SocketIO(APP)
SOCKETIO.init_app(APP, cors_allowed_origins="*")

DOTENV_PATH = join(dirname(__file__), 'project2.env')
load_dotenv(DOTENV_PATH)

DATABASE_URI = os.environ['DATABASE_URL']

APP.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

DB = flask_sqlalchemy.SQLAlchemy()
def init_DB(APP):
    DB.init_app(APP)
    DB.app = APP
    DB.create_all()
    DB.session.commit()

import models

def get_all_messages_from_db():
    return [db_message.message for db_message in DB.session.query(models.Chat).all()]
def get_all_names_from_db():
    return [db_name.name for db_name in DB.session.query(models.Chat).all()]
def add_to_db(user_name, message):
    DB.session.add(models.Chat(user_name, message))
    DB.session.commit()

def emit_all_messages(channel):
    '''Send all of the messages out.'''
    db_all_messages = get_all_messages_from_db()
    db_all_names = get_all_names_from_db()
    list_of_messages = botcommand.concat_messages(db_all_messages, db_all_names)
    SOCKETIO.emit(channel, {
        'allMessages': list_of_messages
    })
def emit_num_users(channel):
    '''Send the number of users out.'''
    user_count = LIST_OF_CONNECTED_USERS.number_of_users()
    SOCKETIO.emit(channel, {
        'number': user_count
    })
@SOCKETIO.on('connect')
def on_connect():
    '''When a user connects.'''
    SOCKETIO.emit('connected', {
        'test': 'Connected'
    })
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    emit_num_users(USER_UPDATE_CHANNEL)
@SOCKETIO.on('disconnect')
def on_disconnect():
    '''When a user disconects.'''
    LIST_OF_CONNECTED_USERS.delete_user(request.sid)
    emit_num_users(USER_UPDATE_CHANNEL)
@SOCKETIO.on('new message')
def on_new_message(data):
    ''' Get new message from person parse it for url,
     make sure the person is online, and make sure its
     a bot message or not.'''
    room_id = request.sid
    new_message = data['message']['message']
    user_name = LIST_OF_CONNECTED_USERS.check_for_user(room_id)
    if user_name == "":
        error_message = "There was an error please make sure you are logged in."
        SOCKETIO.emit('messageError', {'errormessage': error_message}, room=room_id)
    else:
        new_message_two = url_parse.url_parse(new_message)
        add_to_db(user_name,new_message_two)
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    #code to see if the message was a bot, if was figure out response and send it back
    bot_message = bot.valid_message(new_message)
    if bot_message["is_bot"]==True:
        add_to_db('bot',botcommand.bot_command_parse(bot_message["bot_command"], bot_message["message"]))
        emit_all_messages(MESSAGE_RECEIVED_CHANNEL)

@SOCKETIO.on('new google user')
def on_new_google_user(data):
    '''When a new user connects through google.'''
    LIST_OF_CONNECTED_USERS.add_user(request.sid, data['name'])
    emit_num_users(USER_UPDATE_CHANNEL)
    SOCKETIO.emit('profilePic', {'profPicture': data['profilepic']}, room=request.sid)
    SOCKETIO.emit('messageError', {'errormessage': ''}, room=request.sid)
    SOCKETIO.emit('UserLogedIn', {'loggedinbro': 'logedin'}, room=request.sid)

@APP.route('/')
def index():
    '''Flask to run the program and load the html'''
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    return flask.render_template('index.html')


if __name__ == '__main__':
    init_DB(APP)
    SOCKETIO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
