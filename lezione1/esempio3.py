from threading import Thread, Lock
import time
import logging
from random import randrange

def thread_function(name):
    logging.info("Thread %s   :  starting", name)
    time.sleep(randrange(3,10))
    logging.info("Thread %s   :  finishing", name)

if __name__ == "__main__":
    numeroThread = 10
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main       :  before creating threads")
    listaThread = []
    for nomeThread in range(numeroThread):
        listaThread.append(Thread(target=thread_function, args=(nomeThread,)))
        
    logging.info("Main       :  before running threads")
    for eThread in listaThread:
        eThread.start()
    
    logging.info("Main       :  wait for the threads to finish")
    for eThread in listaThread:
        eThread.join()

    logging.info("Main       :  all done")
