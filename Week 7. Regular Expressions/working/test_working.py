import pytest
from working import convert

def test_value_error01():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_value_error02():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_convert01():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert02():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"