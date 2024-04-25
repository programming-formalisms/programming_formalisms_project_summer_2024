# Utils 
def is_prime_fabio_cecilia(x):
    """ This is our function"""
    is_prime_out = False
    for i in range(2, x):
        if x % i == 0:
            continue
        if i == x:
            is_prime_out = True 
    return is_prime_out
