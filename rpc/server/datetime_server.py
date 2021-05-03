import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

# Funzione da esportare
def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

# Definizione Server RPC
server = SimpleXMLRPCServer(('0.0.0.0', 12345))

print('Server UP and Running, listening on port 12345 ...')

# Registrazione funzione da esportare
server.register_function(today, 'today')

# Avvio server
server.serve_forever()
