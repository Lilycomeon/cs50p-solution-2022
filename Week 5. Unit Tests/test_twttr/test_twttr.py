import pytest
from twttr import shorten

def test_hello():
    assert shorten("hello") == "hll"

def test_check():
    assert shorten("check") == "chck"

def test_REALLY():
    assert shorten("REALLY, you") == "RLLY, y"

def test_number123():
    assert shorten("number123") == "nmbr123"
