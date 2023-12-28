from plates import is_valid


def test_starts_with_2char():
    assert is_valid("C1111")== False

def test_len():
    assert is_valid("CSh11155")== False

def test_middle_numbers():
    assert is_valid("CS12l4")== False

def test_start_with0():
    assert is_valid("CS012")== False

def test_punctuation():
    assert is_valid("CS,50")== False

def test_uppercase():
    assert is_valid("CSFIFT")== True

def test_lowercase():
    assert is_valid("csfift")== True




