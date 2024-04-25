def is_even(x):
	if not isinstance(x, int):
		raise TypeError("Warning! The input must be an integer")
	if(x%2 == 0):
        	return True
	return False

