#!/usr/bin/env python3

import math
import time


def triangle_number(n):
    return (n * (n + 1))//2


def is_pentagonal_number(number):
    return ((math.sqrt(24*number + 1) + 1)/6).is_integer()


def is_hexagonal_number(number):
    return ((math.sqrt(8*number + 1) + 1)/4).is_integer()


def main():
    n = 285
    while True:
        n += 1
        t_n = triangle_number(n)
        if is_pentagonal_number(t_n) and is_hexagonal_number(t_n):
            break
    print("Solution:", t_n)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
