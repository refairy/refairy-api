from typing import List
from refairy_api.utils.parse import parse_flags


def test_parse_flags():
    # test debug
    debug_flags = [
        ['python', '-m', 'refairy_api', '-d'],
        ['python', '-m', 'refairy_api', '--debug'],
    ]
    debug_parsed: List[dict] = list(
        map(
            parse_flags,
            debug_flags
        )
    )
    for f in debug_parsed:
        assert f['debug'] == True

    # test none-debug
    none_debug_flags = [
        ['python', '-m', 'refairy_api'],
        ['python', '-m', 'refairy_api', '-f'],
    ]
    none_debug_parsed: List[dict] = list(
        map(
            parse_flags,
            none_debug_flags
        )
    )
    for f in none_debug_parsed:
        assert f['debug'] == False
