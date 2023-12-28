from twttr import shorten


def test_onelower_word():
    assert shorten("hello") == "hll"


def test_oneupper_word():
    assert shorten("NAME") == "NM"


def test_lowerupper_word():
    assert shorten("hello 1 NAME") == "hll 1 NM"


def test_mixed_sentence():
    assert shorten("hello1 NAME_left then name_Right") == "hll1 NM_lft thn nm_Rght"

def test_punctuation_sentence():
    assert shorten("name, Right") == "nm, Rght"


