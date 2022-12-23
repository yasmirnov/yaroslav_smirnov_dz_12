from flask import Blueprint, render_template, request
from main.utils import search_posts


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    posts = search_posts(s)

    return render_template('post_list.html', posts=posts, s=s)


