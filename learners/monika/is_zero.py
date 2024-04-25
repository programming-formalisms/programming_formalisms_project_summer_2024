"""A function to check if a number is 0."""
def is_zero(x):
    """Determine if the input is one integer that is zero."""
    if not isinstance(x, int):
        message = "The input must be an integer."
        raise TypeError(message)
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


