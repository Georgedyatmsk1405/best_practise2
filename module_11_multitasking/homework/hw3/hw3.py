import logging
import os
import time
import threading
import multiprocessing
import sqlite3
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.executescript(
            """CREATE TABLE TABLE_HERO(Id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, age VARCHAR, gender CHAR);""")
except(sqlite3.OperationalError):
    print('already')


def get_image(url: str):
    response = requests.get(url, timeout=(5, 5))
    if response.status_code != 200:
        print('UPS')
        return
    result = response.json()
    name = result['name']
    age = result['birth_year']
    gender = result['gender']
    print(f'name{name}, age{age}, gender{gender}')
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.executescript(
            """INSERT INTO TABLE_HERO ('name','age','gender') VALUES('{name}','{age}','{gender}')""".format(name=name,
                                                                                                            age=age,
                                                                                                            gender=gender))


def load_images_multithreading():
    start = time.time()
    threads = []
    for i in range(20):
        thread = threading.Thread(target=get_image, args=(f'https://swapi.dev/api/people/{i}/',))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    logger.info('Done in {:.4}'.format(time.time() - start))


if __name__ == '__main__':
    load_images_multithreading()
