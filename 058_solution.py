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
    limit = 0.1
    number = 9
    side_length = 3
    number_of_primes = 3
    while number_of_primes/(2*side_length - 1) >= limit:
        for i in range(4):
            number += side_length + 1
            if is_prime(number):
                number_of_primes += 1
        side_length += 2
    print("Solution:", side_length)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
