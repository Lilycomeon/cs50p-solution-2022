import pytest
from seasons import check_birthday


def test_check_bday():
    assert check_birthday("2021-07-05") == ("2021", "07", "05")
    assert check_birthday("1996-06-06") == ("1996", "06", "06")
