import socket
import logging
from sys import argv
import json
import re

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

    leave(clientSocket, currNode, oracleIP, oraclePORT)
