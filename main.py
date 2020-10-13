from flask import Flask
from flask_socketio import SocketIO, send
import eventlet
from eventlet.green import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)

#
# def geturl():
#     c = socket.socket()
#     ip = socket.gethostbyname(url)
#     c.connect((ip, 80))
#     print('%s connected' % url)
#     c.sendall('GET /\r\n\r\n')
#     return c.recv(1024)


if __name__ == '__main__':
    socketio.run(app)

#
# @socketio.on('json')
# def handle_json(json):
#     print('received json: ' + str(json))
#
#
# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))
#
#
# @socketio.on('my event')
# def handle_my_custom_event(arg1, arg2, arg3):
#     print('received args: ' + arg1 + arg2 + arg3)
#
#
# # Flask-SocketIO also supports SocketIO namespaces, which allow the client to multiplex several independent
# # connections on the same physical socket
# @socketio.on('my event', namespace='/test')
# def handle_my_custom_namespace_event(json):
#     print('received json: ' + str(json))
