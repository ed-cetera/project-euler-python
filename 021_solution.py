#!/usr/bin/env python3

import time


def sum_of_proper_divisors(number):
    sopd = 0
    for divisor in range(1, number//2 + 1):
        if number % divisor == 0:
            sopd += divisor
    return sopd


def main():
    limit = 9999
    sopd = [0] * limit
    for number in range(limit):
        sopd[number] = sum_of_proper_divisors(number + 1)
    total_sum = 0
    for number in range(limit):
        if (sopd[number] - 1 < limit
                and sopd[number] != number + 1
                and sopd[sopd[number] - 1] == number + 1):
            total_sum += number + 1
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
