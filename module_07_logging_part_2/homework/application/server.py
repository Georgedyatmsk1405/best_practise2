from flask import Flask, render_template, request, url_for,abort, session, redirect, Response
import logging
logging.basicConfig()
module_logger = logging.getLogger('module_logger')
module_logger.setLevel(logging.DEBUG)
module_logger.propagate = False
custom_handler = logging.StreamHandler()
module_logger.addHandler(custom_handler)
import sys


"""curl -X POST -F name=3 http://127.0.0.1:5000/main"""
application= Flask(__name__)


@application.route('/main',methods=['POST','GET'])
def main():


    resultt=request.form['name']
    resultt=2+int(resultt)
    module_logger.debug(str(resultt))
    result={'result':resultt}


    return result


if __name__ == '__main__':
    application.run(debug=True)