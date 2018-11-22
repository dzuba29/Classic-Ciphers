from random import randint
from fractions import gcd

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

def RandomSmallNumber(a,b):
    return randint(a,b)
  
def RandomK(p):
  k=randint(2,p-2)
  if existS(k,p)==True:
    return k
  else: return RandomK(p)

def existS(k,p):
    if gcd(k,p-1)==1: 
        return True

def calcS(m,x,r,k,p):
  g=m-x*r
  k=modualInverse(k,p-1)
  return g*k


def extendedGcd(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedGcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modualInverse(b,n):
    g, x, y = extendedGcd(b, n)
    if g == 1:
        return x % n

def calcSign(y,r,s,g,m,p):
    left_part =pow( (pow(y,r,p) * pow(r,s,p)),1,p )
    # print(left_part)
    right_part = calcKey(g,m,p)
    # print(right_part)
    if left_part == right_part:
        return "Yes,signs match!"
    else:
        return "No, signs doesnt match!"

def calcKey(base,privatePrime,sharedPrime):
    return pow(base,privatePrime,sharedPrime)
