#!/usr/bin/env python3

import time


def number_of_divisors(number):
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
    individual_primes = set(prime_factors)
    result = 1
    for prime in individual_primes:
        result *= prime_factors.count(prime) + 1
    return result


def main():
    counter = 2
    while number_of_divisors(counter * (counter + 1)//2) <= 500:
        counter += 1
    print("Solution:", counter * (counter + 1)//2)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
