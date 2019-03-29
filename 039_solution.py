#!/usr/bin/env python3

import time


def main():
    limit = 1000
    largest_number_of_solutions = 0
    for p in range(3, limit + 1):
        counter = 0
        for a in range(1, p//3 + 1):
            for b in range(a, (p - a)//2 + 1):
                if a**2 + b**2 == (p - a - b)**2:
                    counter += 1
        if counter > largest_number_of_solutions:
            largest_number_of_solutions = counter
            p_for_largest_number_of_solutions = p
    print("Solution:", p_for_largest_number_of_solutions)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
