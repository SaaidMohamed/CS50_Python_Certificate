from seasons import get_minutes, convert_to_words
import pytest


def test_excpected_date():
    assert get_minutes("2023-09-25") == 1440


def test_unsupported_format1():
    with pytest.raises(SystemExit):
        get_minutes("january 4, 2023")


def test_unsupported_format2():
    with pytest.raises(SystemExit):
        get_minutes("january 4th, 2023")


def test_unsupported_format3():
    with pytest.raises(SystemExit):
        get_minutes("23-02-12")


def test_convert_to_words():
    assert convert_to_words(123) == "One hundred twenty-three minutes"
