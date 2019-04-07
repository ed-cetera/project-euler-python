#!/usr/bin/env python3

import time


def main():
    limit = 1000
    total_sum = 0
    for number in range(1, limit + 1):
        total_sum += number**number
    print("Solution:", str(total_sum)[-10:])


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
