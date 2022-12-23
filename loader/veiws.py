from flask import Blueprint, render_template, request

from loader.utils import image_save, adding_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def page_post_add():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_add():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Данные не получены'

    picture_path = image_save(picture)

    if not picture_path:
        return 'Файл не изображение'

    new_post = {
        'pic': picture_path,
        'content': content
    }
    adding_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
