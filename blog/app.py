# from time import time
# from flask import g, request
from flask import Flask
from blog.articles.views import article
from blog.user.views import user
from blog.report.views import report


# фабрика по созданию приложений
def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)


"""
создаем экземпляр приложения, атрибут name - зарезервированная переменная, имеет название модуля в котором работаем
app = Flask(__name__)


страница должна работать по роуту '/'
@app.route('/')
на главной странице выведется текст
def index():
   return 'HELLO'


@app.route('/', methods=['GET', 'POST'])
def index():
    return f'This is a {request.method} request!'


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

"""