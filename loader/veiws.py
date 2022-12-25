from flask import Blueprint, render_template, request
from loader.utils import image_save, adding_post
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)
logging.basicConfig(filename="error.log", level=logging.ERROR)

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def page_post_add():
    """
    страница с формой добавления поста
    """
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_add():
    """
    страница с добавленным постом
    """
    picture = request.files['picture']
    content = request.form.get('content')

    if not picture:
        logging.error('Ошибка загрузки файла')
        return 'Ошибка загрузки файла'
    elif not content:
        logging.error('Ошибка загрузки текста')
        return 'Ошибка загрузки текста'

    picture_path = image_save(picture)

    if not picture_path:
        logging.info(f'Файл {picture} - не изображение')
        return 'Загруженный файл - не изображение'

    new_post = {
        'pic': picture_path,
        'content': content
    }
    adding_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
