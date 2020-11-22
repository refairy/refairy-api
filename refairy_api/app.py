from flask import Flask
from .views.index import index as index_view
from .utils.get_env import get_env


def main():
    app = Flask(__name__)

    app.add_url_rule('/', 'index', view_func=index_view)

    port = get_env('PORT')
    app.run('0.0.0.0', port)


if __name__ == '__main__':
    main()
