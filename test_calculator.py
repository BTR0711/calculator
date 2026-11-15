import pytest
from calculator import *


def test_add_int():
    assert add(2, 3) == 5


def test_add_float():
    assert add(2.1, 3.1) == pytest.approx(5.2)


def test_div():
    assert div(10, 5) == 2.0


def test_div_by_zero():
    with pytest.raises(ValueError):
        div(5, 0)
