import json
from main.utils import load_posts

POST_PATH = 'posts.json'


def image_save(picture):
    """
    Сохраняет изображение по нужному пути
    """
    filename = picture.filename
    filetype = filename.split('.')[-1]

    try:
        if filetype not in ['jpeg', 'jpg', 'png']:
            return

        picture.save(f'./uploads/images/{filename}')
        return f'uploads/images/{filename}'

    except TypeError as e:
        print(e)

    except FileNotFoundError as e:
        print(e)


def post_save_to_json(posts):
    """
    записывает объект в файл json
    """
    with open(POST_PATH, 'w') as file:
        json.dump(posts, file)


def adding_post(post):
    """
    добавляет новый пост
    """
    posts = load_posts()
    posts.append(post)
    post_save_to_json(posts)
