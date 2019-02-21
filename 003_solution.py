#!/usr/bin/env python3

import time


def main():
    number = 600851475143
    prime_factors = []
    divisor = 1
    solved = False
    while not solved:
        divisor += 1
        while number % divisor == 0:
            prime_factors.append(divisor)
            number = number / divisor
            if number == 1:
                solved = True
    print("Solution:", max(prime_factors))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
