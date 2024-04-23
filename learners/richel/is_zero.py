
def is_zero(x):
    """Determines if the input is one integer with value zero"""
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)

has_thrown = False
try:
    is_zero("nonsense")
except TypeError:
    has_thrown = True
assert has_thrown
