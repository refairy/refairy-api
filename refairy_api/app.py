from typing import Optional
from sanic import Sanic

from .views.check import CheckView, CheckIDView, init_text_comparison
from .utils.get_env import get_env


def main(debug: Optional[bool]=False):
    """
    Runs the api server.
    """
    app = Sanic(__name__)

    # add routes
    app.add_route(CheckView.as_view(), CheckView.base_path)  # /check
    app.add_route(CheckIDView.as_view(), CheckIDView.base_path)  # /check/<id>

    # call init function
    init_text_comparison()

    # run server
    port = get_env('PORT')
    app.run('0.0.0.0', port=port, debug=debug)


if __name__ == "__main__":
    main()
