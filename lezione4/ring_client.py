import socket
import logging
from sys import argv
import json
import re

def join(clientSocket, currNode, nextNode, oracleIP, oraclePORT):
    message = '[JOIN] {}'.format(json.dumps(currNode))
    logging.debug('JOIN MESSAGE: {}'.format(message))
    clientSocket.sendto(message.encode(), (oracleIP, oraclePORT))
    message, addr = clientSocket.recvfrom(1024)
    message = message.decode('utf-8')
    logging.debug('RESPONSE: {}'.format(message))
    # update currNode, nextNode 

def leave(clientSocket, currNode, nextNode, oracleIP, oraclePort):
    pass

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
    clientSocket.bind((clientIP, clientPORT))

    logging.info('CLIENT UP AND RUNNING')

    currNode = {}
    nextNode = {}

    currNode['addr'] = clientIP
    currNode['port'] = str(clientPORT)

    join(clientSocket, currNode, nextNode, oracleIP, oraclePORT)
