import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:12345')

try:
    print('3+4 = {}'.format(proxy.somma(3,4)))
except xmlrpc.client.Fault as err:
   print('A Fault occurred')
   print('Fault code: {}'.format(err.faultCode))
   print('Fault string: {}'.format(err.faultString))
