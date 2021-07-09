from notepad.models import Note, get_random_string


def test_string_length_equal_eight():
    text = get_random_string()
    assert len(text) == 8


def test_two_strings_are_different():
    assert get_random_string() != get_random_string()
