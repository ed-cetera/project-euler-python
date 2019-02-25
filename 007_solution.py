#!/usr/bin/env python3

import time


def main():
    stop = 10001
    primes = [2]
    counter = 1
    while len(primes) < stop:
        counter += 2
        for prime in primes[1:]:
            if counter % prime == 0:
                break
        else:
            primes.append(counter)
    print("Solution:", primes[stop - 1])


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
