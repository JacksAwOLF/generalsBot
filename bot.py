from websocket import create_connection
import urllib
import json

url = 'ws://botws.generals.io/socket.io/?EIO=3&transport=websocket'
ws = create_connection(url)


data = '42["set_username", "rkzKelCed", "Ayame\'s Dad"]'


print('recieve1', ws.recv())


print('recieve2', ws.recv())

ws.send('2')
print('sending data 2')

print('recieve3', ws.recv())

ws.send(data)
print('sending data 3')

print('recieve4', ws.recv())	

print(ws.recv())

ws.close()

