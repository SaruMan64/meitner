"""
Test Module for Example Functions.

This module tests the functions provided in the example module of the Meitner package.
"""

import pytest

from meitner.example import add


def test_add() -> None:
    """
    Test the add function from the example module.

    This function tests the add function with various inputs to ensure
    it returns the correct sum of the provided numbers.

    Test Cases
    ----------
    test_add_integers : Test the addition of two integers.
    test_add_floats : Test the addition of two floats.
    test_add_mixed : Test the addition of an integer and a float.

    Examples
    --------
    >>> test_add()
    """
    # Test addition of integers
    assert add(1, 2) == 3, "Adding 1 + 2 should be 3"

    # Test addition of floats
    assert add(1.5, 2.5) == 4.0, "Adding 1.5 + 2.5 should be 4.0"

    # Test addition of an integer and a float
    assert add(1, 2.5) == 3.5, "Adding 1 + 2.5 should be 3.5"


if __name__ == "__main__":
    pytest.main()
