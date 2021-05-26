from xmlrpc.server import SimpleXMLRPCServer

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

def factorial(n):
    if(n == 1):
        return 1
    return n * factorial(n-1)

server = SimpleXMLRPCServer(('0.0.0.0', 12345))
print('Server Calcolatrice Pronto, in ascolto sul porto 12345')

server.register_multicall_functions()

server.register_function(add, 'somma')
server.register_function(subtract, 'sottrai')
server.register_function(multiply, 'moltiplica')
server.register_function(divide, 'dividi')
server.register_function(factorial, 'fattoriale')

server.serve_forever()
