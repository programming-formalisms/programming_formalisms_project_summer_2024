## practise ex2 
def is_zero(x):
    """ Definition to check if int is zero """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False


assert is_zero(0)
assert not is_zero(1)
assert is_zero.__doc__
assert is_zero("awdawd")
