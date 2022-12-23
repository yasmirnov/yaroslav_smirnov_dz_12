from flask import Flask, send_from_directory
from main.veiws import main_blueprint
from loader.veiws import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


app.register_blueprint(main_blueprint)


app.register_blueprint(loader_blueprint)


# @app.route('/')
# def index():
#     pass
#
#
# @app.route("/list")
# def page_tag():
#     pass
#
#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass
#
#
# @app.route("/post", methods=["POST"])
# def page_post_upload():
#     pass
#
#
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
