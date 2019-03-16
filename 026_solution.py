#!/usr/bin/env python3

import time


def main():
    limit = 999
    longest_recurring_cycle = 0
    d_for_longest_recurring_cycle = 0
    for d in range(2, limit + 1):
        remainders = []
        remainder = 1
        while remainder != 0 and remainder not in remainders:
            remainders.append(remainder)
            remainder = 10 * remainder - ((10 * remainder)//d) * d
            if remainder == 0:
                continue
            if remainder in remainders:
                recurring_cycle = len(remainders) - remainders.index(remainder)
                if recurring_cycle > longest_recurring_cycle:
                    longest_recurring_cycle = recurring_cycle
                    d_for_longest_recurring_cycle = d
                continue
    print("Solution:", d_for_longest_recurring_cycle)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
