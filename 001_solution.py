#!/usr/bin/env python3

import time


def main():
    noninclusive_upper_limit = 1000
    total_sum = 0
    for number in range(1, noninclusive_upper_limit):
        if number % 3 == 0 or number % 5 == 0:
            total_sum += number
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
