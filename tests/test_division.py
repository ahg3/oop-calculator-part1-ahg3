"""This is the starting test file"""
import pytest

from app.division import division


def test_division():
    """Divide Two Numbers"""
    assert division(2,2) == 1


def test_division_div_zero():
    """Tests that division by zero exception is thrown"""
    with pytest.raises(ZeroDivisionError):
        division(4, 0)
