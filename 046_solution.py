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
    list_of_odd_primes = [3, 4, 7]
    number = 7
    while True:
        number += 2
        if is_prime(number):
            list_of_odd_primes.append(number)
            continue
        for prime in list_of_odd_primes:
            base = 1
            while prime + 2 * base**2 < number:
                base += 1
            if prime + 2 * base**2 == number:
                break
        else:
            break
    print("Solution:", number)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
