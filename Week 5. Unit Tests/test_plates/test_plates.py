import pytest
from plates import is_valid

def test_length():
    assert is_valid("a") == False

def test_character():
    assert is_valid("12abc") == False

def test_letters():
    assert is_valid("a1234") == False

def test_number0():
    assert is_valid("ac022") == False

def test_numberplace():
    assert is_valid("ac123d") == False

def test_weirdcharacter():
    assert is_valid("acd12#") == False