#!/usr/bin/env python3

import time


def main():
    number_of_digits = 1000
    fibonacci_number = 1
    previous = 1
    index = 2
    while len(str(fibonacci_number)) < number_of_digits:
        (previous, fibonacci_number) = (fibonacci_number,
                                        fibonacci_number + previous)
        index += 1
    print("Solution:", index)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
