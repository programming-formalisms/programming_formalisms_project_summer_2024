"""Develop is_zero."""

def is_zero(x):
  """Returns true if x is one integer that is zero.
  Raises an exception when x is not an integer.
  """
  if not isinstance(x, int):
      raise TypeError("x must be one integer")
  return x == 0

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)

has_thrown = False
try:
    is_zero("nonsense.")
except TypeError:
    has_thrown = True
assert has_thrown
