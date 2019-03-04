#!/usr/bin/env python3

import time


def length_of_collatz_sequence(starting_number):
    sequence = [starting_number]
    number = starting_number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return len(sequence)


def main():
    longest_sequence = 0
    seed = 0
    for number in range(1, 1000000):
        length = length_of_collatz_sequence(number)
        if length > longest_sequence:
            longest_sequence = length
            seed = number
    print("Solution:", seed)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
