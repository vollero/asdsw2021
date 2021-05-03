from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('0.0.0.0', 12345), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_function(pow)
    
    @server.register_function(name='somma')
    def adder_function(x,y):
        return x + y

    @server.register_function
    def multiply(x, y):
        return x*y

    print('Server UP, in ascolto sul porto 12345 ...')
    server.serve_forever()
