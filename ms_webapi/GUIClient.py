import requests
import json
import tkinter as tk

window = tk.Tk()

address = 'http://127.0.0.1:12345'

outputMessage = tk.Text()

def open_registration_form():
    newWindow = tk.Toplevel()
    newWindow.wm_title('Registration Form')
    label1 = tk.Label(newWindow, text='username:')
    entry1 = tk.Entry(newWindow, name='entry1')
    label2 = tk.Label(newWindow, text='password:')
    entry2 = tk.Entry(newWindow, name='entry2')
    button = tk.Button(newWindow, text='send', command=lambda:send_registration_params(newWindow))
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    button.pack()

def send_registration_params(window):
    query = {'user': window.nametowidget('entry1').get(), 'password': window.nametowidget('entry2').get()}
    response = requests.post(address + '/api/v1/messages/registration', params=query)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('-'*80)
    outputMessage.delete("1.0", tk.END)
    outputMessage.insert(tk.END,json.dumps(response.json(), indent=4, sort_keys=True))

def registration():
    open_registration_form()

def authentication():
    query = {'user': 'Luca', 'password': '1122334455'}
    response = requests.get(address + '/api/v1/messages/authentication', params=query)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('-'*80)
    outputMessage.delete("1.0", tk.END)
    outputMessage.insert(tk.END,json.dumps(response.json(), indent=4, sort_keys=True))

def send():
    query = {'user': 'Luca', 'token': '11223344556677889900', 'destination': 'Pippo', 'message': 'Ciao, come stai?'}
    response = requests.post(address + '/api/v1/messages/send', params=query)
    print('-'*80)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    outputMessage.delete("1.0", tk.END)
    outputMessage.insert(tk.END,json.dumps(response.json(), indent=4, sort_keys=True))

def receive():
    query = {'user': 'Luca', 'token': '11223344556677889900'}
    response = requests.get(address + '/api/v1/messages/receive', params=query)
    print('-'*80)
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    outputMessage.delete("1.0", tk.END)
    outputMessage.insert(tk.END,json.dumps(response.json(), indent=4, sort_keys=True))


button1 = tk.Button(text = 'Registration', width=20, height=2, command=registration)
button2 = tk.Button(text = 'Authentication', width=20, height=2, command=authentication)
button3 = tk.Button(text = 'Send Message', width=20, height=2, command=send)
button4 = tk.Button(text = 'Receive Messages', width=20, height=2, command=receive)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

outputMessage.pack()

window.mainloop()

registration()
authentication()
send()
receive()
