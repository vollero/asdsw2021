from cmd import Cmd
from threading import Thread
from sys import argv
import time 
import os
import re
import socket
import logging
import json

def sendDataToRing(socket, nextNode, idSorgente, idDestinazione, mess):
    # PROTOTIPO MESSAGGIO: [DATA] JSON MESSAGGIO
    messaggio = {}
    messaggio['idSorgente'] = idSorgente
    messaggio['idDestinazione'] = idDestinazione
    messaggio['payload'] = mess

    stringaMessaggio = '[DATA] {}'.format(json.dumps(messaggio))
    logging.debug('Invio Messaggio: {}'.format(stringaMessaggio))

    # INVIO MESSAGGIO

class RingPrompt(Cmd):
    prompt = ''
    intro  = 'Benvenuto nel ring. Usa ? per accedere all\'help'

    def conf(self, socket, nextNode, idSorgente):
        self.socket = socket
        self.nextNode = nextNode
        self.idSorgente = idSorgente

        self.prompt = '[{}]>'.format(idSorgente)

    def do_exit(self, inp):
        print('Ciao, alla prossima!')
        return True

    def do_send(self, inp):
        #Prototipo messaggio: [id] <MESSAGGIO>
        result = re.search('^\[([0-9]*)\]', inp)
        if bool(result):
            idDestinazione = result.group(1)
        result = re.search('<([a-zA-Z0-9\,\.\;\'\"\!\?<> ]*)>', inp)
        if bool(result):
            mess = result.group(1)
        logging.debug('INVIO MESSAGGIO:\nDestinatario: {}\nMessaggio: {}'.format(idDestinazione, mess))
        
        sendDataToRing(self.socket, self.nextNode, self.idSorgente, idDestinazione, mess)

    def echo_message(self, inp):
        print('Messaggio Ricevuto: {}'.format(inp))

    #def do_help(self, inp):
    #    print("Help non ancora implementato")

    def do_shell(self, inp):
        print(os.popen(inp).read())

def managePrompt(prompt):
    prompt.cmdloop()

def join(clientSocket, currNode, nextNode, oracleIP, oraclePORT):
    mess = '[JOIN] {}'.format(json.dumps(currNode))
    logging.debug('JOIN MESSAGE: {}'.format(mess))
    clientSocket.sendto(mess.encode(), (oracleIP, oraclePORT))
    mess, addr = clientSocket.recvfrom(1024)
    mess = mess.decode('utf-8')
    logging.debug('RESPONSE: {}'.format(mess))
	
    result = re.search('(\{[a-zA-Z0-9\"\'\:\.\,\{\} ]*\})', mess)
    if bool(result):
        logging.debug('RE GROUP(1) {}'.format(result.group(1)))	
        action = json.loads(result.group(1))
        currNode['id'] = action['id']
        nextNode = action['nextNode']
        logging.debug('NEW CONF: \n\t currNode: {} \n\t nextNode: {}'.format(currNode, nextNode))
    else:
        action = {}

def leave(clientSocket, currNode, oracleIP, oraclePort):
    mess = '[LEAVE] {}'.format(json.dumps(currNode))
    logging.debug('LEAVE MESSAGE: {}'.format(mess))
    clientSocket.sendto(mess.encode(), (oracleIP, oraclePORT))

def sendMessage(clientSocket, nextNode, message):
    pass

def receiveMessage(clientSocket):
    pass

if __name__ == '__main__':

    oracleIP     = argv[1]
    oraclePORT   = int(argv[2])
    clientIP     = argv[3]
    clientPORT   = int(argv[4])

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    clientSocket.bind( (clientIP, clientPORT) )

    logging.info('CLIENT UP AND RUNNING')

    currNode = {}
    nextNode = {}

    currNode['addr'] = clientIP
    currNode['port'] = str(clientPORT)

    join(clientSocket, currNode, nextNode, oracleIP, oraclePORT)

    prompt = RingPrompt()
    prompt.conf(clientSocket, nextNode, currNode['id'])

    Thread(target=managePrompt, args=(prompt,)).start()

    # Gestione comunicazione Ring
