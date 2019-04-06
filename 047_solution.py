#!/usr/bin/env python3

# GIVES CORRECT SOLUTION BUT DOES NOT SOLVE WITHIN THE TIME CONSTRAINTS OF 60s!

import time


def number_of_distinct_prime_factors(number):
    prime_factor_set = set()
    divisor = 1
    while number > 1:
        divisor += 1
        while number % divisor == 0:
            prime_factor_set.add(divisor)
            number = number // divisor
    return len(prime_factor_set)


def main():
    number = 1
    while True:
        number += 1
        if number_of_distinct_prime_factors(number) == 4:
            if number_of_distinct_prime_factors(number + 1) == 4:
                if number_of_distinct_prime_factors(number + 2) == 4:
                    if number_of_distinct_prime_factors(number + 3) == 4:
                        break
                    else:
                        number += 3
                else:
                    number += 2
            else:
                number += 1
    print("Solution:", number)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
