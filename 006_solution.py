#!/usr/bin/env python3

import time


def main():
    limit = 100
    sum_of_squares = 0
    square_of_sum = 0
    for number in range(1, limit + 1):
        square_of_sum += number
        sum_of_squares += number**2
    square_of_sum **= 2
    print("Solution:", square_of_sum - sum_of_squares)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
