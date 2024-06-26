def is_even(x):
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    return x % 2 == 0

assert is_even.__doc__
assert is_even(2)
assert not is_even(1)

