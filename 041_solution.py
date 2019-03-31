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


def is_pandigital(number):
    number_str = str(number)
    if len(number_str) > 9:
        return False
    digits = set([int(d) for d in number_str])
    if len(digits) != len(number_str):
        return False
    if 0 in digits:
        return False
    for digit in range(1, len(number_str) + 1):
        if digit not in digits:
            return False
    return True


def main():
    # pandigital numbers with 2, 3, 5, 6, 8, or 9 digits are divisible by 3
    for number in range(7654321, 1234567 - 1, -2):
        if is_pandigital(number) and is_prime(number):
            break
    else:
        for number in range(4321, 1234 - 1, -2):
            if is_pandigital(number) and is_prime(number):
                break
        else:
            number = None
    print("Solution:", number)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
