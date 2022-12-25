from flask import Blueprint, render_template, request
from main.utils import search_posts
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def index():
    """
    главная страница
    """
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    """
    страница с результатом поиска постов
    """
    s = request.args.get('s')
    logging.info(f'Страница поиска по запросу {s} запрошена')
    posts = search_posts(s)

    return render_template('post_list.html', posts=posts, s=s)
