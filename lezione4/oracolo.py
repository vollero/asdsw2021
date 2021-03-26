import socket
from sys import argv
import logging
import re
import json

def decodeJoin(addr, mess):
    result = re.search('(\{[a-zA-Z0-9\"\'\:\.\, ]*\})' , mess)
    if bool(result):
        logging.debug('RE GROUP(1) {}'.format(result.group(1)))
        action = json.loads(result.group(1))
    else:
        action = {}
    
    action['command'] = 'join'

    return action

def decodeLeave(addr, mess):
    result = re.search('(\{[a-zA-Z0-9\"\'\:\.\, ]*\})' , mess)
    if bool(result):
        logging.debug('RE GROUP(1) {}'.format(result.group(1)))
        action = json.loads(result.group(1))
    else:
        action = {}
    
    action['command'] = 'leave'
    
    return action

def decodeMessage(addr, mess):
    result = re.search('^\[([A-Z]*)\]' , mess)
    if bool(result):
        command = result.group(1)
        logging.debug('COMMAND: {}'.format(command))

        try:
            action = {
                'JOIN'  : lambda param1,param2 : decodeJoin(param1, param2),
                'LEAVE' : lambda param1,param2 : decodeLeave(param1, param2)
            }[command](addr, mess)
        except:
            action = {}
            action['command'] = 'unknown'
    else:
        action = {}
        action['command'] = 'invalid'

    logging.debug('ACTION: {}'.format(action))

    return action

def updateRingJoin(action, listOfNodes):
    logging.debug('RING JOIN UPDATE')
    node = {}

    id_ = 1
    idList = [eNode['id'] for eNode in listOfNodes]
    for i in range(1, len(listOfNodes)+2):
        if i not in idList:
            id_ = i
            break

    node['id'] = id_
    node['port'] = action['port']
    node['addr'] = action['addr']

    listOfNodes.append(node)
    
    return True

def updateRingLeave(action, listOfNodes):
    logging.debug('RING LEAVE UPDATE')
    return True

def updateRing(action, listOfNodes):
    logging.info('RING UPDATE: {}'.format(action))
    try:
        result = {
            'join'  : lambda param1,param2 : updateRingJoin(param1, param2),
            'leave' : lambda param1,param2 : updateRingLeave(param1, param2)
        }[action['command']](action, listOfNodes)
    except:
        result = False

    return result

if __name__ == '__main__':

    IP     = argv[1]
    PORT   = int(argv[2])
    bufferSize  = 1024
    listOfNodes = []

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    OracleSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    OracleSocket.bind( (IP, PORT) )

    print("ORACLE UP AND RUNNING!")

    while True:
        mess, addr = OracleSocket.recvfrom(bufferSize)
        dmess = mess.decode('utf-8')

        logging.info('REQUEST FROM {}'.format(addr))
        logging.info('REQUEST: {}'.format(dmess))

        action = decodeMessage(addr, dmess)
        updateRing(action, listOfNodes)

        logging.info('UPDATED LIST OF NODES {}'.format(listOfNodes))

        OracleSocket.sendto(str.encode('[ACCEPT]'), addr)
