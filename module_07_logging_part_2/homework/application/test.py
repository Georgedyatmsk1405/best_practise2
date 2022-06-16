import sys

from utils import string_to_operator
from logging_tree import printout                      #6 задание протестировал
import logging
import logging.config
from declr import dict_config
root_logger = logging.getLogger()
logging.config.dictConfig(dict_config)


# 7 задание фильтер
class NoParsingFilter(logging.Filter):
    def filter(self, record):
        print(record.getMessage().isascii())
        if record.getMessage().isascii()==True:
            return record.getMessage()
        else:
            return None


module_logger = logging.getLogger('module_logger')
module_logger.addFilter(NoParsingFilter())

module_logger.info("b")
module_logger.info("casesØ")
a=3
module_logger.warning("a")


b=3
module_logger.debug("b")

printout()