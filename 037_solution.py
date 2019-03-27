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
    limit = 11
    number = 10
    found = 0
    total_sum = 0
    while found < limit:
        number_str = str(number)
        for offset in range(len(number_str)):
            if not (is_prime(int(number_str[offset:]))
                    and is_prime(int(number_str[:offset + 1]))):
                break
        else:
            found += 1
            total_sum += number
        number += 1
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
