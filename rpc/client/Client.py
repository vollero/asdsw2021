import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://127.0.0.1:12345')

print(s.pow(2,3))
print(s.somma(8,9))
print(s.multiply(3,5))

print(s.system.listMethods())
