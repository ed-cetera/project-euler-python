#!/usr/bin/env python3

import time


def main():
    noninclusive_upper_limit = 100
    largest_digital_sum = 0
    for a in range(1, noninclusive_upper_limit):
        for b in range(1, noninclusive_upper_limit):
            digital_sum = sum([int(d) for d in str(a**b)])
            if digital_sum > largest_digital_sum:
                largest_digital_sum = digital_sum
    print("Solution:", largest_digital_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
