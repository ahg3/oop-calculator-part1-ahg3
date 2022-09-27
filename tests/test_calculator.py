"""This is the starting test file"""
from app.calculator import Calculator


def test_calculator_operations():
    assert Calculator.addition(2, 2) == 4
    assert Calculator.divide(2, 2) == 1
    assert Calculator.multiply(2, 2) == 4
    assert Calculator.subtract(2, 2) == 0

