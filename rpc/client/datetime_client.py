import xmlrpc.client
import datetime

proxy = xmlrpc.client.ServerProxy('http://192.168.76.205:12345')

today = proxy.today()

converted = datetime.datetime.strptime(today.value, '%Y%m%dT%H:%M:%S')
print('Today: {}'.format(converted.strftime('%d/%m/%Y, %H:%M')))
