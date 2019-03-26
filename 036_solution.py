#!/usr/bin/env python3

import time


def is_palindromic(string):
    digits = list(string)
    for position in range(len(digits)//2 + 1):
        if digits[position] != digits[len(digits) - position - 1]:
            return False
    return True


def main():
    limit = 999999
    total_sum = 0
    for number in range(limit + 1):
        if (is_palindromic(str(number))
                and is_palindromic("{0:b}".format(number))):
            total_sum += number
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
