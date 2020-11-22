import sys
from .app import main


if __name__ == '__main__':
    if sys.argv[1] in ['-d', '--debug']:
        debug = True
    else:
        debug = False
    main(debug)
