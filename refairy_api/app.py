from sanic import Sanic

from .routes.index import index as index_route
from .routes.check import check as check_route
from .utils.get_env import get_env


def main(debug: bool=False):
    app = Sanic(__name__)

    app.add_route(index_route, '/')
    app.add_route(check_route, '/check/', methods=['POST'])

    port = get_env('PORT')
    app.run('0.0.0.0', port=port, debug=debug)


if __name__ == "__main__":
    main()
