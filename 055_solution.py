#!/usr/bin/env python3

import time


def is_palindromic_number(num):
    digits = list(str(num))
    for i in range(len(digits)//2 + 1):
        if digits[i] != digits[len(digits) - i - 1]:
            return False
    return True


def main():
    noninclusive_upper_limit = 10000
    counter = 0
    for number in range(1, noninclusive_upper_limit):
        iteration = 1
        num = number + int(str(number)[::-1])
        while iteration < 50 and not is_palindromic_number(num):
            iteration += 1
            num = num + int(str(num)[::-1])
        if iteration == 50:
            counter += 1
    print("Solution:", counter)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
