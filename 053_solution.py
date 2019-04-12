#!/usr/bin/env python3

import math
import time


def binomial_coefficient(n, r):
    return math.factorial(n)//(math.factorial(r) * math.factorial(n - r))


def main():
    n_limit = 100
    lower_noninclusive_limit = 1000000
    counter = 0
    for n in range(1, n_limit + 1):
        for r in range(1, n + 1):
            if binomial_coefficient(n, r) > lower_noninclusive_limit:
                counter += 1
    print("Solution:", counter)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
