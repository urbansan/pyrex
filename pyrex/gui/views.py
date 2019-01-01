import bottle
from bottle import template, Bottle
import os

web_frontend = Bottle()

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
bottle.TEMPLATE_PATH.append(TEMPLATE_DIR)


@web_frontend.route('/')
def index():
    return template('index', content='test content')


@web_frontend.route('/contracts')
def contract_list():
    return template('contract_list')


@web_frontend.route('/contract/<nb>')
def single(nb):
    return template('single_contract', nb=nb)


if __name__ == '__main__':

    # print(app.)
    web_frontend.run(host='localhost', port=8080)
