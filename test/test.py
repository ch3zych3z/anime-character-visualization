from api import get_text


def test_data_preprocessing():
    assert get_text("Big boy", "Tokyo Ghoul") == "Big boy in Tokyo Ghoul world"
