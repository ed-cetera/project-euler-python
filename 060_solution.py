#!/usr/bin/env python3

import math
import time

primes = set()
divisibles = set()


def is_prime(number):
    if number < 2:
        return False
    if number in divisibles:
        return False
    if number in primes:
        return True
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            divisibles.add(number)
            return False
    primes.add(number)
    return True


def may_i_join(number, ensemble):
    for member in ensemble:
        if (not is_prime(int(str(number) + str(member)))
                or not is_prime(int(str(member) + str(number)))):
            return False
    return True


def main():
    number = 1
    solos = []
    duos = []
    trios = []
    quartets = []
    smallest_sum = None
    while (smallest_sum is None
            or number + 2 < smallest_sum - 792):  # smallest prime quartet
        number += 2
        if is_prime(number):
            for quartet in quartets:
                if (smallest_sum is None
                        or number < smallest_sum - sum(quartet)):
                    if may_i_join(number, quartet):
                        smallest_sum = number + sum(quartet)
            for trio in trios:
                if (smallest_sum is None
                        or 2*number + 2 < smallest_sum - sum(trio)):
                    if may_i_join(number, trio):
                        quartets.append(trio + [number])
            for duo in duos:
                if (smallest_sum is None
                        or 3*number + 2 + 4 < smallest_sum - sum(duo)):
                    if may_i_join(number, duo):
                        trios.append(duo + [number])
            for solo in solos:
                if (smallest_sum is None
                        or 4*number + 2 + 4 + 6 < smallest_sum - solo[0]):
                    if may_i_join(number, solo):
                        duos.append(solo + [number])
            solos.append([number])
    print("Solution:", smallest_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
