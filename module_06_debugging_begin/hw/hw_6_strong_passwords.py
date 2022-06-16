"""
Давайте ещё раз вернёмся к нашему приложению, проверяющему пароли.
К нам пришли сотрудники отдела безопасности и сказали,
    что согласно новым стандартам безопасности хорошим паролем
    считается такой пароль, который не содержит в себе слов английского алфавита.

Давайте допишем эту проверку в функцию:

    def check_weak_passwords(password_string: str) -> bool:
        pass


Список слов английского алфавита вы можете найти в файле /usr/share/dict/words
(берите только слова больше 4 символов).
"""

import getpass
import hashlib
import logging

logger = logging.getLogger("password_checker")


def check_if_password_is_weak(password_string: str) -> bool:
    result=True
    spisok_slov=[]
    f=open('/usr/share/dict/words.txt') # файла я такого не нашел, но допустим он есть и разделен запятыми
    for i in f:
        slovo=i.split(',')
        spisok_slov.append(slovo)
    for j in spisok_slov:
        if j in password_string.split('_'):    # наш пароль видим разделен пробелами если там есть солва, либо _ , как определять наличие слов, которые
                                            # сливаются друг с другом, это наверное сложный алгоритм.
            result=True                 # возвращаем true, значит пароль слабый, насколько я понял далее по коду
        else:
            result=False

    return result



def input_and_check_password():
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    elif check_if_password_is_weak(password):
        logger.warning("Вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)
