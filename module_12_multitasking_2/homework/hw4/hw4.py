import logging
import os
import time
import threading
import multiprocessing
import sqlite3
import requests

from threading import Lock


LOCK = Lock()

logging.basicConfig(level=logging.INFO,filename='log.txt')
logger = logging.getLogger(__name__)


def get_image(thread:int):
    with LOCK:
        start=time.time()
        while(time.time()-start) <20:
            response = requests.get('https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp=1549892280', timeout=(5, 5))
            print(response.text)
            if response.status_code != 200:
                print('UPS')
                return
            result = response
            print(result)
            with open('log.txt','a') as f:
                f.write(str(thread)+str(result.text)+'\n')
            time.sleep(1)

        
    


def load_images_multithreading():
    start = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=get_image, args=(i,))
        thread.start()
        threads.append(thread)
        
        print(i)

    for thread in threads:
        thread.join()

    logger.info('Done in {:.4}'.format(time.time() - start))
load_images_multithreading()