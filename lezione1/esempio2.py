from threading import Thread, Lock
import time
import logging
from random import randrange

def thread_function(name):
    logging.info("Thread %s   :  starting", name)
    time.sleep(randrange(5))
    logging.info("Thread %s   :  finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main       :  before creating threads")
    x = Thread(target=thread_function, args=(1,))
    y = Thread(target=thread_function, args=(2,))
    logging.info("Main       :  before running threads")
    x.start()
    y.start()
    logging.info("Main       :  wait for the threads to finish")
    x.join()
    y.join()
    logging.info("Main       :  all done")
