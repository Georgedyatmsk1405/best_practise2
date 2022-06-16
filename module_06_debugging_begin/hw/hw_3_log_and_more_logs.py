"""
Логов бывает очень много. А иногда - ооооооооочень много.
Из-за этого люди часто пишут логи не в человекочитаемом,
    а в машиночитаемом формате, чтобы машиной их было обрабатывать быстрее.

Напишите функцию

def log(level: str, message: str) -> None:
    pass


которая будет писать лог  в файл skillbox_json_messages.log в следующем формате:
{"time": "<время>", "level": "<level>", "message": "<message>"}

сообщения должны быть отделены друг от друга символами переноса строки.
Обратите внимание: наше залогированное сообщение должно быть валидной json строкой.

Как это сделать? Возможно метод json.dumps поможет вам?
"""
import logging
import sys
import datetime
import json

logger=logging.getLogger('level')
def log(level: str, message: str) -> None:

    time=str(datetime.datetime.now())
    to_json ={'time': time, 'level': level,'message':message}


    with open('skillbox_json_messages.log', 'a') as f:
        f.write(json.dumps(to_json,indent=4))


log('sssssas','sssada')
log('sssssaszz','sssadaazzza')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
