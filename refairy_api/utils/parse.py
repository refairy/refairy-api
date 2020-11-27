def parse_flags(flags: list) -> dict:
    """
    Returns the parsed flags.
    """
    # restore flags to full names
    flags = ['--debug' if '-d' in flags else f for f in flags]

    # parse flags
    parsed = {}
    if '--debug' in flags:
        parsed['debug'] = True
    else:
        parsed['debug'] = False

    return parsed
