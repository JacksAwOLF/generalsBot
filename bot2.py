import socketio
import urllib

url = 'http://botws.generals.io'
#url = urllib.parse.quote(url)

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect(url)
sio.wait()