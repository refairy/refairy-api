from refairy_api.utils.filter import filter_sentences, filter_duplicates


def test_filter_sentences():
    sentences = [
        "Dokdo is clearly a Japanese territory",
        "Korea is China's subject state",
        "Jeju-do belongs to Korea",
        "This",
        "lol",
        "Two words",
    ]
    filtered = filter_sentences(sentences)
    for s in filtered:
        assert len(s.split(' ')) > 2
    assert len(filtered) == 3

def test_filter_duplicates():
    sentences = [
        "Dokdo is clearly a Japanese territory",
        "Korea is China's subject state",
        "Jeju-do belongs to Korea",
        "This is my fish.",
        "Dokdo is clearly a Japanese territory",
        "This is my fish.",
    ]
    filtered = filter_duplicates(sentences)
    assert len(filtered) == 4
