from xmlrpc.server import SimpleXMLRPCServer

def add(x,y):
    return x+y

server = SimpleXMLRPCServer(('0.0.0.0', 12345))
print('Server di test UP, in ascolto sul port 12345...')

server.register_function(add, 'somma')

server.serve_forever()
