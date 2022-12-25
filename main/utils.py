import json
from json import JSONDecodeError
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)
logging.basicConfig(filename="error.log", level=logging.ERROR)

POST_PATH = "posts.json"


def load_posts():
    """
    загружает данные из файла json
    """
    try:
        with open(POST_PATH, 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        logging.info(f'Файл {POST_PATH} не найден')
        print('Файл не найден')

    except JSONDecodeError:
        logging.error('Файл не преобразовывается')
        print('Файл не удается преобразовать')


def search_posts(text_for_search):
    """
    ищет посты по вводу
    """
    posts = []

    for post in load_posts():
        if text_for_search.lower() in post["content"].lower():
            posts.append(post)

    return posts
