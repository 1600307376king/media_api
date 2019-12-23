from flask import Flask
from view.link_images import images_index

app = Flask(__name__)
app.config.from_pyfile('config/setting.py')

app.register_blueprint(images_index, url_prefix='')


if __name__ == '__main__':
    app.run()
