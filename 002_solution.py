#!/usr/bin/env python3

import time


def main():
    upper_limit = 4000000
    fibonacci_number = 1
    previous = 1
    total_sum = 0
    while fibonacci_number < upper_limit:
        (previous, fibonacci_number) = (fibonacci_number,
                                        fibonacci_number + previous)
        if fibonacci_number % 2 == 0:
            total_sum += fibonacci_number
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
