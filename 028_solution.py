#!/usr/bin/env python3

import time


def main():
    limit_size = 1001
    number = 1
    diagonal_sum = 1
    for size in range(1, (limit_size + 1)//2):
        for i in range(4):
            (number, diagonal_sum) = (number + 2 * size,
                                      diagonal_sum + number + 2 * size)
    print("Solution:", diagonal_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
