import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:12345')

with open('logo2.png', 'wb') as handle:
    handle.write(proxy.img().data)
