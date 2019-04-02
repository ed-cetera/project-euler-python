#!/usr/bin/env python3

import time


def permutations(lst):
    if len(lst) == 1:
        yield lst
    else:
        for permutation in permutations(lst[1:]):
            for position in range(len(lst)):
                yield permutation[:position] + lst[:1] + permutation[position:]


def main():
    total_sum = 0
    for permutation in permutations(["0", "1", "2", "3", "4",
                                     "5", "6", "7", "8", "9"]):
        number_str = "".join(permutation)
        if (int(number_str[1:4]) % 2 == 0
                and int(number_str[2:5]) % 3 == 0
                and int(number_str[3:6]) % 5 == 0
                and int(number_str[4:7]) % 7 == 0
                and int(number_str[5:8]) % 11 == 0
                and int(number_str[6:9]) % 13 == 0
                and int(number_str[7:10]) % 17 == 0):
            total_sum += int(number_str)
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
