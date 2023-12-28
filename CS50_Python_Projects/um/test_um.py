from um import count


def test_um_space():
    assert count("hello, um my name is ") == 1


def test_um_symbols():
    assert count("hello, um, my name is um... a name ") == 2


def test_um_in_words():
    assert count("hello, um, my name is umbrella ") == 1


def test_um_case_sensitive():
    assert count("hello, UM, my name is UM.. brella ") == 2
