import random

def RandomPrime():
    while True:
        n = random.randint(10,1000)

        if n % 2 == 0:
            continue

        prime = True

        for x in range(3, int(n**0.5 + 1), 2):
            if n % x == 0:
                prime = False

                break

        if prime: 
            return n

def calcKey(base,privatePrime,sharedPrime):
    return (base ** privatePrime) % sharedPrime