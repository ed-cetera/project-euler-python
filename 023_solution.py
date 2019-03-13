#!/usr/bin/env python3

import time


def sum_of_proper_divisors(number):
    sopd = 0
    for divisor in range(1, number//2 + 1):
        if number % divisor == 0:
            sopd += divisor
    return sopd


def main():
    limit = 28123
    abundant_number = [False] * (limit + 1)
    for number in range(1, limit + 1):
        if sum_of_proper_divisors(number) > number:
            abundant_number[number] = True
    total_sum = 0
    for number in range(1, limit + 1):
        total_sum += number
        for summand in range(1, number//2 + 1):
            if abundant_number[summand] and abundant_number[number - summand]:
                total_sum -= number
                break
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
