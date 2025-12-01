"""
Simple pytest tests for calc_lib.py
These tests cover basic functionality of the calculator library

© 2025 Pau Erola, University of Bristol
"""

import pytest
from calc_lib import add, subtract, multiply, divide


# Tests for add function
def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(10, 15) == 25


def test_add_negative_numbers():
    assert add(-5, -3) == -8
    assert add(-10, 5) == -5


def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5


# Tests for subtract function
def test_subtract_positive_numbers():
    assert subtract(10, 3) == 7
    assert subtract(20, 15) == 5


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2
    assert subtract(5, -3) == 8


def test_subtract_to_zero():
    assert subtract(5, 5) == 0


# Tests for multiply function
def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12
    assert multiply(7, 8) == 56


def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 10) == 0


def test_multiply_negative_numbers():
    assert multiply(-3, 4) == -12
    assert multiply(-5, -2) == 10


# Tests for divide function
def test_divide_positive_numbers():
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5


def test_divide_with_decimals():
    assert divide(7, 2) == 3.5
    assert divide(9, 4) == 2.25


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_negative_numbers():
    assert divide(-10, 2) == -5
    assert divide(10, -2) == -5
    assert divide(-10, -2) == 5
