from flask import Blueprint, render_template
from werkzeug.utils import redirect
from blog.user.views import USERS

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1:
        {
            'id': 1,
            'title': 'Top 100 in Earth Science',
            'text': 'some text',
            'author': {
                'name': USERS[1],
                'id': 1,
            }
        },
    2:
        {
            'id': 2,
            'title': 'Hubble Gazes at a Cluster Full of Cosmic Clues',
            'text': 'some text',
            'author': {
                'name': USERS[2],
                'id': 2,
            }
        },
    3:
        {
            'id': 3,
            'title': 'NASA’s Ingenuity Mars Helicopter Completes First One-Way Trip',
            'text': 'some text',
            'author': {
                'name': USERS[3],
                'id': 3,
            }
        }
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]['title']
        article_text = ARTICLES[pk]['text']
        article_author = ARTICLES[pk]['author']
    except KeyError:
        return redirect('/articles')
    return render_template(
        'articles/details.html',
        article_name=article_name,
        article_text=article_text,
        article_author=article_author
    )
