import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:12345')

multicall = xmlrpc.client.MultiCall(proxy)

multicall.somma(3,4)
multicall.sottrai(5,3)
multicall.moltiplica(2,3)
multicall.dividi(7,2)
multicall.fattoriale(3)

result = tuple(multicall())

print(result)

print('3+4 = {}, 5-3={}, 2*3={}, floor(7/2)={}, fattoriale(3)={}'.format(*result))
