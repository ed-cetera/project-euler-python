#!/usr/bin/env python3

import math
import time


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def main():
    upper_limit_b = 1000
    noninclusive_absolute_limit_a = 1000
    b_primes = [2]
    counter = 1
    while counter < upper_limit_b:
        counter += 2
        for prime in b_primes[1:]:
            if counter % prime == 0:
                break
        else:
            b_primes.append(counter)
    longest_prime_series = 0
    for b in b_primes:
        for a in range(-1 * noninclusive_absolute_limit_a + 1,
                       noninclusive_absolute_limit_a):
            n = 0
            while is_prime(n**2 + a * n + b):
                n += 1
            if n > longest_prime_series:
                longest_prime_series = n
                coefficient_product = a * b
    print("Solution:", coefficient_product)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
