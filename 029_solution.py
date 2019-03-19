#!/usr/bin/env python3

import time


def main():
    lower_bound_a = 2
    upper_bound_a = 100
    lower_bound_b = 2
    upper_bound_b = 100
    distinct_terms = set()
    for a in range(lower_bound_a, upper_bound_a + 1):
        for b in range(lower_bound_b, upper_bound_b + 1):
            distinct_terms.add(a**b)
    print("Solution:", len(distinct_terms))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
