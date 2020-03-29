import sys
import time
import math
import random


def is_prime_1(n:int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_2(n:int) -> bool:
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def is_prime_3(n: int) -> bool:
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


if __name__ == '__main__':
    with open(file_name) as f:
        numbers = [int(s) for s in f.read().split('\n') if s.strip()]
        for number in numbers:            
            check = is_prime_2(number) 
            if check:
                print(1)
            else:
                print(0)
