from refairy_api.views.index import index


def test_index():
    assert index() == "Hello, ReFairy!"
