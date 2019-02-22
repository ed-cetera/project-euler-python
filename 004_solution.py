#!/usr/bin/env python3

import time


def is_palindromic_number(num):
    digits = list(str(num))
    for i in range(len(digits)//2 + 1):
        if digits[i] != digits[len(digits) - i - 1]:
            return False
    return True


def main():
    largest_palindrome = 0
    for num1 in range(100, 1000):
        for num2 in range(num1, 1000):
            if is_palindromic_number(num1 * num2):
                largest_palindrome = max(largest_palindrome, num1 * num2)
    print("Solution:", largest_palindrome)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
