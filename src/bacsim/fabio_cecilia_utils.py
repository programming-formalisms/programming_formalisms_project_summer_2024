# Utils 
def is_prime_fabio_cecilia(x):
    """ This is our function"""
    is_prime_out = True
    
    if x == 1:        
        return is_prime_out
    
    
    else:
        for i in range(2, x):
            if x % i == 0:
                is_prime_out = False
                return is_prime_out
            
    return is_prime_out
