import json
from json import JSONDecodeError

POST_PATH = "posts.json"


def load_posts():
    try:
        with open(POST_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Файл формата .json отсутствует')
    except JSONDecodeError:
        print('Файл формата .json не удается преобразовать')


def search_posts(text_for_search):
    posts = []

    for post in load_posts():
        if text_for_search.lower() in post["content"].lower():
            posts.append(post)

    return posts
