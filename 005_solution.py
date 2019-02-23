#!/usr/bin/env python3

import time


def main():
    limit = 20
    scd_prime_factors = [0] * limit
    for i in range(2, limit + 1):
        prime_factors = []
        divisor = 1
        finished = False
        while not finished:
            divisor += 1
            while i % divisor == 0:
                prime_factors.append(divisor)
                i = i / divisor
                if i == 1:
                    finished = True
        counted_prime_factors = [0] * limit
        for factor in prime_factors:
            counted_prime_factors[factor - 1] += 1
        for j in range(limit):
            if scd_prime_factors[j] < counted_prime_factors[j]:
                scd_prime_factors[j] = counted_prime_factors[j]
    scd = 1
    for i in range(limit):
        scd *= (i + 1)**scd_prime_factors[i]
    print("Solution:", scd)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
