from random import randint

def FermasPrime(num,test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def RandomPrime(bit):
    found_prime = False
    while not found_prime:
        p = randint(2**(bit-1), 2**bit)
        if FermasPrime(p, 1000):
            return p

def calcKey(base,privatePrime,sharedPrime):
    return pow(base,privatePrime,sharedPrime)
