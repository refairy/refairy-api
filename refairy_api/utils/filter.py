from typing import List


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
