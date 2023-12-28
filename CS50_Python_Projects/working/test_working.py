from working import convert
import pytest


def test_h_off():
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"


def test_err_raised():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


def test_m_off():
    with pytest.raises(ValueError):
        convert("09:65 AM to 05:64 PM")


def test_to_off():
    with pytest.raises(ValueError):
        convert("09:65 AM05:64 PM")
