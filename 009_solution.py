#!/usr/bin/env python3

import time


def main():
    total_sum = 1000
    for a in range(1, total_sum // 2):
        for b in range(a, total_sum - a):
            c = total_sum - a - b
            if a**2 + b**2 == c**2:
                print("Solution:", a * b * c)
                return


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
