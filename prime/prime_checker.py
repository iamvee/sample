import sys
import time
import math
import random

def printit(f):
    def inner(*args, **kwargs):
        print(f(*args, **kwargs))
    return inner


def trial_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True


@printit
def is_prime_2(n:int) -> bool:
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return "0"
    return "1"


@printit
def is_prime_3(n: int) -> str:
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return "0"

    if n == 2 or n == 3 or n == 5 or n == 7:
        return "1"
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)


    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a, d, n, s):
            return "0"

    return "1"


if __name__ == '__main__':
    file_name = sys.argv[1]
    
    with open(file_name) as f:
        numbers = [int(s) for s in f.read().strip().split('\n')]
        
    for number in numbers:
        is_prime_2(number)
            
