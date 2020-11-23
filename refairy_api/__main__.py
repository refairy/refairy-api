import sys
from .app import main


if __name__ == '__main__':
    if '-d' or '--debug' in sys.argv:
        debug = True
    else:
        debug = False

    main(debug)
