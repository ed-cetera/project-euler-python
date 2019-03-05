#!/usr/bin/env python3

import math
import time


def main():
    grid_size = 20
    print("Solution:",
          math.factorial(2 * grid_size)//(math.factorial(grid_size)
                                          * math.factorial(grid_size)))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
