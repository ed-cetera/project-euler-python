#!/usr/bin/env python3

import time


def main():
    total_sum = 0
    for number in range(2, 354295):  # 6 * 9**5 + 1, >6 digit number impossible
        test_sum = 0
        for digit in [int(d) for d in str(number)]:
            test_sum += digit**5
        if test_sum == number:
            total_sum += number
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
