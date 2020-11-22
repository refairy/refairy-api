from flask import Flask
from .views.index import index as index_view
from .views.check import check as check_view
from .utils.get_env import get_env


def main(debug: bool=False):
    app = Flask(__name__)

    app.add_url_rule('/', view_func=index_view)
    app.add_url_rule('/check', view_func=check_view, methods=['POST'])

    port = get_env('PORT')
    app.run('0.0.0.0', port, debug=debug)


if __name__ == '__main__':
    main()
