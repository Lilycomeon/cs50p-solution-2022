import pytest
from numb3rs import validate

def test_maximium():
    assert validate("275.3.6.28") == False

def test_minimum():
    assert validate("-2.3.6.28") == False

def test_true():
    assert validate("255.255.255.0") == True

def test_extra():
    assert validate("255.255.255.0.1") == False

def test_ip():
    assert validate("cat") == False


def test_digit():
    assert validate("1.2.3.999") == False