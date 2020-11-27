from typing import List


def filter_sentences(sentences: List[str]):
    """
    Returns the filtered sentences.
    """
    return list(
        filter(
            lambda x: len(x.split(' ')) > 1,
            sentences
        )
    )
