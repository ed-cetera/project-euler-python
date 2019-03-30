#!/usr/bin/env python3

import time


def champernowne_fractional_digit(position):
    counter = 1
    pos = 1
    while pos < position:
        counter += 1
        pos += len(str(counter))
    return int(str(counter)[position - pos - 1])


def main():
    product = (champernowne_fractional_digit(1)
               * champernowne_fractional_digit(10)
               * champernowne_fractional_digit(100)
               * champernowne_fractional_digit(1000)
               * champernowne_fractional_digit(10000)
               * champernowne_fractional_digit(100000)
               * champernowne_fractional_digit(1000000))
    print("Solution:", product)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
