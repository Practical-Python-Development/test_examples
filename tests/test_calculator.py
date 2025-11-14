"""Test for calculator functions."""

import pytest
from src.calculator import add, divide


def test_add_parametrized(addition_cases):
    """Test using parameters from fixture."""
    a, b, expected = addition_cases
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [(6, 3, 2), (10, 2, 5)])
def test_divide(a, b, expected):
    """Test using parameters from decorator."""
    assert divide(a, b) == expected


def test_divide_by_zero():
    """Test if something raises an exception."""
    with pytest.raises(ValueError, match='Division by zero!'):
        divide(1, 0)
