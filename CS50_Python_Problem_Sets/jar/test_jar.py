from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(5)
    assert str(jar) == ""
    jar.deposit(10)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_negativeV_err_raised():
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(6)


def test_capacity_err_raised():
    with pytest.raises(ValueError):
        jar = Jar(4)
        jar.deposit(5)
