import os
import flask
import flask_socketio
from os.path import join, dirname
from dotenv import load_dotenv
import flask_sqlalchemy
import models
import requests
import botMessage as bot
import botbuild as botcommand
import urlparse
from flask import request

#newpsuh

MESSAGE_RECEIVED_CHANNEL = 'message received'
USER_UPDATE_CHANNEL='user updated'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'project2.env')
load_dotenv(dotenv_path)

database_uri = os.environ['DATABASE_URL']


app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.create_all()
db.session.commit()

userCount=0
users=[]

def emit_all_messages(channel):
    all_messages = [ \
        db_message.message for db_message \
        in db.session.query(models.Chat).all()]
    all_names =[\
        db_name.name for db_name in db.session.query(models.Chat).all() ] 
    
    arrayList=[]
    for x in range(len(all_messages)):
        messageOp=all_names[x]
        messageOp+= ": "
        messageOp+=all_messages[x]
        arrayList.append(messageOp)
    socketio.emit(channel, {
        'allMessages': arrayList
    })
    

def emit_num_users(channel):
    userCount=len(users)
    socketio.emit(channel, {
        'number': userCount
    })
    

@socketio.on('connect')
def on_connect():
    socketio.emit('connected', {
        'test': 'Connected'
    })
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    emit_num_users(USER_UPDATE_CHANNEL)
    
@socketio.on('disconnect')
def on_disconnect():
    global users
    users = list(filter(lambda i: i['userid'] != request.sid, users)) 
    emit_num_users(USER_UPDATE_CHANNEL)

@socketio.on('new message')
def on_new_number(data):
    print("Got an event for new number with data:", data)
    roomid=request.sid
    new_message = data['message']['message']
    if not any(d['userid']==request.sid for d in users):
            errorz="There was an error please make sure you are logged in."
            print('inside senderror')
            socketio.emit('messageError', { 
            'errormessage': errorz
            },room=roomid)
    else:
        urlCheck=urlparse.urlParse(new_message)
        new_message=urlCheck.checkURL()
        res = next((sub for sub in users if sub['userid'] == request.sid), None)
        db.session.add(models.Chat(res.get("name"),new_message));
        db.session.commit();
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    #code to see if the message was a bot, if was figure out response and send it back
    botMessage=bot.validMessage(new_message)
    if(botMessage["KEY_IS_BOT"]):
        db.session.add(models.Chat('bot',botcommand.botCommandParse(botMessage["KEY_BOT_COMMAND"],botMessage["KEY_MESSAGE"])));
        db.session.commit();
        emit_all_messages(MESSAGE_RECEIVED_CHANNEL)    

@socketio.on('new google user')
def on_new_google_user(data):
    print("Got an event for new google user input with data:", data)
    users.append({'userid': request.sid, 'name':data['name']})
    emit_num_users(USER_UPDATE_CHANNEL)
    socketio.emit('profilePic',{
        'profPicture': data['profilepic']
    },room=request.sid)
    socketio.emit('messageError', { 
        'errormessage': ''
            },room=request.sid)
    socketio.emit('UserLogedIn', { 
        'loggedinbro': 'logedin'
            },room=request.sid)

@app.route('/')
def index():
    emit_all_messages(MESSAGE_RECEIVED_CHANNEL)
    
    return flask.render_template('index.html')


if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
