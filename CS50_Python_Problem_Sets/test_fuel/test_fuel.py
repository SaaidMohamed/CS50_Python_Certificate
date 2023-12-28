submit50 cs50/problems/2023/sql/donutsfrom fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50

def test_guage1():
    assert gauge(50) == "50%"

def test_guage3():
    assert gauge(99) == "F"

def test_guage4():
    assert gauge(1) == "E"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("l/2")

def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
