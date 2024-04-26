"""Richel's utility functions."""

def is_zero(x):
    """Determine if `x` is zero.

    If `x` is not a number, a `TypeError` is raised.

    Returns `True` if `x` is zero
    """
    if not isinstance(x, (int, float)):
        msg = "'number' must be a number. "
        raise TypeError(
            msg,
            "Actual type of 'number': ", type(x),
        )
    return x == 0
