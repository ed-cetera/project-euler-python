#!/usr/bin/env python3

import time


def is_pandigital(number):
    number_str = str(number)
    if len(number_str) != 9:
        return False
    digits = set([int(d) for d in number_str])
    for digit in range(1, 10):
        if digit not in digits:
            return False
    return True


def num_set_concat(number, n):
    result = ""
    for multiplier in range(1, n + 1):
        result += str(multiplier * number)
    return int(result)


def main():
    largest_concatenated_pandigital = 0
    for multiplicant in range(1, 9877):  # 9876 + 1
        for n in range(2, 10):  # n > 1, 9 + 1, max. 9 concatenations
            concatenation = num_set_concat(multiplicant, n)
            if is_pandigital(concatenation):
                if concatenation > largest_concatenated_pandigital:
                    largest_concatenated_pandigital = concatenation
    print("Solution:", largest_concatenated_pandigital)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
