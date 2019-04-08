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


def are_permutations(number1, number2):
    if (sorted([int(digit) for digit in str(number1)])
            == sorted([int(digit) for digit in str(number2)])):
        return True
    return False


def main():
    solved = False
    for first in range(1000, 10**4 - 2):
        if is_prime(first):
            for steps in range(1, (10**4 - 1 - first)//2 + 1):
                if first == 1487 and steps == 3330:
                    continue
                if is_prime(first + steps) and is_prime(first + 2*steps):
                    if (are_permutations(first, first + steps)
                            and are_permutations(first, first + 2*steps)):
                        solved = True
                        break
        if solved:
            break
    print("Solution:", str(first) + str(first + steps) + str(first + 2*steps))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
