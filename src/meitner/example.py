"""
Example Module for Meitner.

This module provides example functions to demonstrate the functionality of the Meitner package.
"""

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Sum two numbers.

    Parameters
    ----------
    a : int or float
        The first number to add.
    b : int or float
        The second number to add.

    Returns
    -------
    int or float
        The sum of `a` and `b`.

    Examples
    --------
    >>> add(1, 2)
    3
    >>> add(1.5, 2.5)
    4.0
    """
    return a + b
