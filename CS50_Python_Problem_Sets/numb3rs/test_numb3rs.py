from numb3rs import validate

def test_invalid_digit():
    assert validate("256.10.10.10") == False

def test_secondbyte_digit():
    assert validate("25.257.10.10") == False

def test_thirdbyte_digit():
    assert validate("25.25.258.10") == False

def test_lastbyte_digit():
    assert validate("25.25.25.256") == False

def test_single_digit():
    assert validate("127.0.0.1") == True

def test_two_digit():
    assert validate("10.25.50.19") == True

def test_broadcast_digit():
    assert validate("255.255.255.255") == True

def test_Zero_digit():
    assert validate("0.0.0.0") == True

def test_negative_digit():
    assert validate("-1.-100.-250.-0") == False



