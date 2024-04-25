def is_even(x):
    """this is a function of is even"""
    if not isinstance(x,int):
        raise TypeError("not a integer")
    return x%2 == 0
    

assert is_even(0)
assert not is_even(1)
assert is_even.__doc__

assert is_even(2.4) 