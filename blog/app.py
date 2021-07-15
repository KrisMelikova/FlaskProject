from time import time

from flask import Flask, g
from flask import request

# создаем экземпляр приложения, атрибут name - зарезервированная переменная, имеет название модуля в котором работаем
app = Flask(__name__)


# страница должна работать по роуту '/'
# @app.route('/')
# на главной странице выведется текст
# def index():
#    return 'HELLO'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return f'This is a GET request!'
    if request.method == 'POST':
        return f'This is a POST request!'


@app.before_request
def process_before_request():
    g.start_time = time()


@app.after_request
def process_after_request(response):
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time
    return response


@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error)
    return '404'
