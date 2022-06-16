import sys

from utils import string_to_operator
import logging
#Здесь функция 1-3 задание
root_logger = logging.getLogger()
logging.basicConfig()

class CustomFileHandler(logging.Handler):

    def __init__(self,  mode='a'):
        super().__init__()

        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        level=str(record).split(',')[1]
        print(level)
        if "10" in level:
            with open("debug.log", mode=self.mode) as f:
                f.write(message + '\n')
        elif "20" in level:
            with open("info.log", mode=self.mode) as f:
                f.write(message + '\n')
        elif "30" in level:
            with open("warning.log", mode=self.mode) as f:
                f.write(message + '\n')
        elif "40" in level:
            with open("erroe.log", mode=self.mode) as f:
                f.write(message + '\n')
        elif "50" in level:
            with open("critical.log", mode=self.mode) as f:
                f.write(message + '\n')

progress = CustomFileHandler()
module_logger = logging.getLogger('module_logger')
module_logger.setLevel(logging.DEBUG)
module_logger.propagate = False
custom_handler = logging.StreamHandler()
module_logger.addHandler(custom_handler)
module_logger.addHandler(progress)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")
custom_handler.setFormatter(formatter)


def calc(args):
    module_logger.debug("Arguments: ", args)

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        module_logger.error("Error while converting number 1")
        module_logger.error(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        module_logger.error("Error while converting number 1")
        module_logger.error(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    module_logger.info("Result: ", result)
    module_logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    calc(sys.argv[1:])

