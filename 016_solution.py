#!/usr/bin/env python3

import time


def main():
    digits = [int(x) for x in list(str(2**1000))]
    print("Solution:", sum(digits))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
