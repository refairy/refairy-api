import sys
from .app import main
from .utils.parse import parse_flags


if __name__ == '__main__':
    flags: dict = parse_flags(sys.argv)
    debug: bool = flags['debug']

    main(debug)
