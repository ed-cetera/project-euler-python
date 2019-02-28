#!/usr/bin/env python3

import time


def main():
    limit = 2000000
    primes = [False] * 2 + [True] * (limit - 1)
    for i in range(limit + 1):
        if primes[i] is True:
            counter = 2 * i
            while counter <= limit:
                primes[counter] = False
                counter += i
    total_sum = 0
    for i in range(limit + 1):
        if primes[i] is True:
            total_sum += i
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
