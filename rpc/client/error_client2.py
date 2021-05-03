import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://www.google.com')

try:
    print('3+4 = {}'.format(proxy.somma(3,4)))
except xmlrpc.client.ProtocolError as err:
   print('A Protocol Error occurred')
   print('URL: {}'.format(err.url))
   print('HTTP/HTTPS headers: {}'.format(err.headers))
   print('Error code: {}'.format(err.errcode))
   print('Error message: {}'.format(err.errmsg))
