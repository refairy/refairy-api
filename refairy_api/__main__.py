import os
import sys
from .app import main


if __name__ == '__main__':
    if '-d' in sys.argv or '--debug' in sys.argv:
        os.environ['FLASK_ENV'] = 'Development'
        debug = True
    else:
        os.environ['FLASK_ENV'] = 'Production'
        debug = False
    main(debug)
