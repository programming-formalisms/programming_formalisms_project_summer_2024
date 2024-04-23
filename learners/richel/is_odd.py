
def is_even(x):
    """Determine if the input is one integer that is even"""
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    return x % 2 == 0

assert is_even.__doc__
assert is_even(2)
assert not is_even(1)

# 'is_even("nonsense")' throws a TypeError 
# because of the modulo operator

has_thrown = False
try:
    is_even(0.0)
except TypeError:
    has_thrown = True
assert has_thrown

def is_odd(x):
    """Determine if the input is one integer that is odd"""
    return not is_even(x)

assert is_odd.__doc__
assert is_odd(1)

# Already passes, consider not putting it in
# assert not is_odd(2)

# Already passes, consider not putting it in
# has_thrown = False
# try:
#     is_odd(0.0)
# except TypeError:
#     has_thrown = True
# assert has_thrown
