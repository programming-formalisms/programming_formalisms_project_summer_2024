#Formal testing using unittest of the function is_prime in python.


def prime_number_checker(number):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                return False
        return True
    else:
        return False
