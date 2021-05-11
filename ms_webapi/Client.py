import requests
import json

address = 'http://192.168.112.120:12345'

def registration():
    query = {'user': 'Luca', 'password': '1122334455'}
    response = requests.post(address + '/api/v1/messages/registration', params=query)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('-'*80)

def authentication():
    query = {'user': 'Luca', 'password': '1122334455'}
    response = requests.get(address + '/api/v1/messages/authentication', params=query)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('-'*80)

def send():
    query = {'user': 'Luca', 'token': '11223344556677889900', 'destination': 'Pippo', 'message': 'Ciao, come stai?'}
    response = requests.post(address + '/api/v1/messages/send', params=query)
    print('-'*80)
    print(json.dumps(response.json(), indent=4, sort_keys=True))

def receive():
    query = {'user': 'Luca', 'token': '11223344556677889900'}
    response = requests.get(address + '/api/v1/messages/receive', params=query)
    print('-'*80)
    print(json.dumps(response.json(), indent=4, sort_keys=True))

registration()
authentication()
send()
receive()
