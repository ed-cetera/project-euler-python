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
    limit = 999999
    counter = 0
    for number in range(2, limit + 1):
        number_str = str(number)
        for index in range(len(number_str)):
            if not is_prime(int(number_str[index:] + number_str[:index])):
                break
        else:
            counter += 1
    print("Solution:", counter)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
