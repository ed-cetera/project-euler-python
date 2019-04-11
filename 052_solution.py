#!/usr/bin/env python3

import time


def are_permutations(number1, number2):
    if (sorted([int(digit) for digit in str(number1)])
            == sorted([int(digit) for digit in str(number2)])):
        return True
    return False


def main():
    number = 0
    while True:
        number += 1
        if (are_permutations(number, 2*number)
                and are_permutations(number, 3*number)
                and are_permutations(number, 4*number)
                and are_permutations(number, 5*number)
                and are_permutations(number, 6*number)):
            break
    print("Solution:", number)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
