#!/usr/bin/env python3

import time


def main():
    limit = 1000000
    primes = [False] * 2 + [True] * (limit - 1)
    for i in range(limit + 1):
        if primes[i] is True:
            counter = 2 * i
            while counter <= limit:
                primes[counter] = False
                counter += i
    primes = [prime for prime in range(limit + 1) if primes[prime] is True]
    number_of_consecutive_primes = 1
    while sum(primes[:number_of_consecutive_primes]) <= limit:
        number_of_consecutive_primes += 1
    solved = False
    while not solved:
        number_of_consecutive_primes -= 1
        for start in range(len(primes)):
            if sum(primes[start:start+number_of_consecutive_primes]) > limit:
                break
            if sum(primes[start:start+number_of_consecutive_primes]) in primes:
                solved = True
                break
    print("Solution:", sum(primes[start:start+number_of_consecutive_primes]))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
