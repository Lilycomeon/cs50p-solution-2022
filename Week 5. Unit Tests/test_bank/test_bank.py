import pytest
from bank import value

def test_hello():
    assert value("Hello") == 0

def test_hi():
    assert value("hi") == 20

def test_goodday():
    assert value("goodday") == 100