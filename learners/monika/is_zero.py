def is_zero(x):
    """Determines if the input is one integer that is zero"""
    if x == 0:
        return True
    return False

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)


