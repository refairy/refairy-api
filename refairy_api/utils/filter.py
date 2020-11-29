from typing import List
from numba import jit


@jit(forceobj=True)
def _filter(sentences: List[str]):
    """
    Default function for filtering. JIT compiled.
    """
    sentences = filter_sentences(sentences)
    sentences = filter_duplicates(sentences)
    sentences = filter_javascript(sentences)
    return sentences


def filter_sentences(sentences: List[str]):
    """
    Returns the filtered sentences(recognize sentences).
    띄어쓰기가 너무 적은 것들은 거른다.
    """
    return list(
        filter(
            lambda x: len(x.split(' ')) > 2,
            sentences
        )
    )


def filter_duplicates(sentences: List[str]):
    """
    Returns the filtered sentences(remove duplicates).
    중복을 제거하고 반환한다. (단, 순서는 유지)
    """
    filtered = []
    for s in sentences:
        if s not in filtered:
            filtered.append(s)
    
    return filtered


def filter_javascript(sentences: List[str]):
    """
    JavaScript code is filtered.
    """
    keywords = [
        "function(", "$(", "({", "})", "getElement", "createElement", "src=", ")=>"
    ]
    filtered = []
    for sentence in sentences:
        if not sum([kw in sentence.replace(' ', '') for kw in keywords]):
            filtered.append(sentence)

    return filtered
