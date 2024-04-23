def is_zero(val):

    if not isinstance(val,int):
        raise TypeError(f"{val} is not a integer")
    if val == 0:
        return True
        
assert is_zero(0)
has_thrown = False
try:
    is_zero("Stuff")
except TypeError:
    has_thrown = True

assert has_thrown

assert is_zero(1)