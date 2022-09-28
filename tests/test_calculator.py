"""This is the starting test file"""
from app.calculator import Calculator


def test_calculator_operations():
    assert Calculator.addition(2, 2) == 4, "The Addition Function Passed"
    assert Calculator.divide(2, 2) == 1, "The Division Function Passed"
    assert Calculator.multiply(2, 2) == 4, "The Multiplication Function Worked"
    assert Calculator.subtract(2, 2) == 0, "The Subtraction Function Worked"

    import sys


def print_python_version():
    """Function printing python version."""
    print(sys.version)
