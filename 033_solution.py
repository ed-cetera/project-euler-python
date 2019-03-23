#!/usr/bin/env python3

import time


def main():
    product_nominator = 1
    product_denominator = 1
    for nominator in range(1, 10):
        for denominator in range(nominator + 1, 10):
            for cancelled in range(1, 10):
                if ((int(str(cancelled)+str(nominator))/nominator
                     == int(str(cancelled)+str(denominator))/denominator)
                    or (int(str(cancelled)+str(nominator))/nominator
                        == int(str(denominator)+str(cancelled))/denominator)
                    or (int(str(nominator)+str(cancelled))/nominator
                        == int(str(cancelled)+str(denominator))/denominator)
                    or (int(str(nominator)+str(cancelled))/nominator
                        == int(str(denominator)+str(cancelled))/denominator)):
                    product_nominator *= nominator
                    product_denominator *= denominator
                    break
    for divisor in range(product_nominator, 2, -1):
        if (product_nominator % divisor == 0
                and product_denominator % divisor == 0):
            product_nominator //= divisor
            product_denominator //= divisor
    print("Solution:", product_denominator)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
