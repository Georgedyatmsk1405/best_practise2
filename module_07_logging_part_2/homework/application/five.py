import logging
#здесь 5 задание
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
        if "20" in level or "30" in level or "40" in level or "50" in level:
            with open("five.log", mode=self.mode) as f:
                f.write(message + '\n')



dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "handlers": {
        "custom_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "CustomFileHandler": {
            "()": CustomFileHandler,
            "level": "DEBUG",
            "formatter": "base",

        }
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["custom_handler", "CustomFileHandler"],
            # "propagate": False,
        }
    },

    # "filters": {},
    # "root": {} # == "": {}
}
