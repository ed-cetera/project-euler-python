#!/usr/bin/env python3

# GIVES CORRECT SOLUTION BUT DOES NOT SOLVE WITHIN THE TIME CONSTRAINTS OF 60s!

import math
import time


def pentagonal_number(n):
    return (n * (3*n - 1))//2


def is_pentagonal_number(number):
    return ((math.sqrt(24*number + 1) + 1)/6).is_integer()


def main():
    difference_n = 0
    solved = False
    while not solved:
        difference_n += 1
        difference = pentagonal_number(difference_n)
        # P_{n} - P_{n-1} = 3n - 2
        for k in range(difference_n, (difference + 2)//3 + 1):
            p_k = pentagonal_number(k)
            if (is_pentagonal_number(p_k - difference)
                    and is_pentagonal_number(2*p_k - difference)):
                solved = True
                break
    print("Solution:", difference)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
