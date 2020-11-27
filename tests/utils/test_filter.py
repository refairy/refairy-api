from refairy_api.utils.filter import filter_sentences


def test_filter_sentences():
    sentences = [
        "Dokdo is clearly a Japanese territory",
        "Korea is China's subject state",
        "Jeju-do belongs to Korea",
        "This",
        "lol",
    ]
    filtered = filter_sentences(sentences)
    for s in filtered:
        assert len(s.split(' ')) > 1
    assert len(filtered) == 3
