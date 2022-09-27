"""This is the starting test file"""
from app.multiplication import multiplication


def test_multiplication():
    """Test multiplication"""
    assert multiplication(2, 2) == 4

