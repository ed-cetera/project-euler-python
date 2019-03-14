#!/usr/bin/env python3

import time


def main():
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    limit = 1000000

    def find_permutation(limit, counter, remaining_digits):
        permutation = None
        if len(remaining_digits) == 1:
            counter += 1
            if counter == limit:
                permutation = remaining_digits[0]
        else:
            for digit in remaining_digits:
                (counter, permutation) = find_permutation(
                        limit,
                        counter,
                        [d for d in remaining_digits if d != digit])
                if permutation is not None:
                    return (counter, digit + permutation)
        return (counter, permutation)

    (counter, permutation) = find_permutation(limit, 0, digits)
    print("Solution:", permutation)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
