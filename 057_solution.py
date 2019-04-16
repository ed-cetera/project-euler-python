#!/usr/bin/env python3

import time


def main():
    limit = 1000
    (numerator, denominator) = (1, 2)  # sqrt(2) = 1 + numerator/denumerator
    counter = 0
    for iteration in range(2, limit + 1):
        (numerator, denominator) = (denominator, 2*denominator + numerator)
        if len(str(numerator + denominator)) > len(str(denominator)):
            counter += 1
    print("Solution:", counter)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
