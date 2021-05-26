from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def img():
    with open('logo.png', 'rb') as handle:
        return xmlrpc.client.Binary(handle.read())

server = SimpleXMLRPCServer(('0.0.0.0', 12345))
print('IMG Transfer Server UP and Running, listening on port 12345 ...')

server.register_function(img, 'img')

server.serve_forever()
