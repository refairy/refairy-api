from typing import List


def filter_sentences(sentences: List[str]):
    """
    Returns the filtered sentences(recognize sentences).
    """
    return list(
        filter(
            lambda x: len(x.split(' ')) > 1,
            sentences
        )
    )


def filter_duplicates(sentences: List[str]):
    """
    Returns the filtered sentences(remove duplicates).
    """
    filtered = []
    for s in sentences:
        if s not in filtered:
            filtered.append(s)
    
    return filtered
