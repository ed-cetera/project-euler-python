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
    pandigital_products = set()
    for permutation in permutations(["1", "2", "3", "4", "5",
                                     "6", "7", "8", "9"]):
        for size_multiplicant in range(1, 8):
            for size_multiplier in range(1, 9 - size_multiplicant):
                multiplicant = int("".join(permutation[0:size_multiplicant]))
                multiplier = int("".join(permutation[
                    size_multiplicant:size_multiplicant + size_multiplier]))
                product = int("".join(permutation[
                    size_multiplicant + size_multiplier:]))
                if multiplicant * multiplier == product:
                    pandigital_products.add(product)
    print("Solution:", sum(pandigital_products))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
