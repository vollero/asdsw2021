from cmd import Cmd
from threading import Thread
import time 
import os
import re

class RingPrompt(Cmd):
    prompt = ''
    intro  = 'Benvenuto nel ring. Usa ? per accedere all\'help'

    def do_exit(self, inp):
        print('Ciao, alla prossima!')
        return True

    def do_send(self, inp):
        #Prototipo messaggio: [id] <MESSAGGIO>
        result = re.search('^\[([0-9]*)\]', inp)
        if bool(result):
            id_ = result.group(1)
        result = re.search('<([a-zA-Z0-9\,\.\;\'\"\!\?<> ]*)>', inp)
        if bool(result):
            mess = result.group(1)
        print('Destinatario: {}\nMessaggio: {}'.format(id_, mess))

    def echo_message(self, inp):
        print('Messaggio Ricevuto: {}'.format(inp))

    #def do_help(self, inp):
    #    print("Help non ancora implementato")

    def do_shell(self, inp):
        print(os.popen(inp).read())

def managePrompt(prompt):
    prompt.cmdloop()

if __name__ == '__main__':
    prompt = RingPrompt()

    Thread(target=managePrompt, args=(prompt,)).start()
