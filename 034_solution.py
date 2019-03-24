#!/usr/bin/env python3

import math
import time


def main():
    total_sum = 0
    for number in range(10, 2540161):  # 7 * 9! + 1, >7 digit number impossible
        sum_of_factorials = 0
        for digit in [int(d) for d in str(number)]:
            sum_of_factorials += math.factorial(digit)
        if sum_of_factorials == number:
            total_sum += number
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
