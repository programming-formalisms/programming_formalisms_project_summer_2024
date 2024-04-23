def is_zero(val):
    """This function checks whether an integer is zero or not"""
    if not isinstance(val,int):
        raise TypeError(f"{val} is not a integer")
    return val == 0

assert is_zero(0)
has_thrown = False
try:
    is_zero("Stuff")
except TypeError:
    has_thrown = True

assert has_thrown
assert not is_zero(1)
assert is_zero.__doc__
