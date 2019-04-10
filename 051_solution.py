#!/usr/bin/env python3

import math
import time


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def string_mixer(str1, str2, current_mix):
    if len(str1) == 0 and len(str2) == 0:
        yield current_mix
    else:
        if len(str1) > 0:
            for mix in string_mixer(str1[:-1], str2, str1[-1] + current_mix):
                yield mix
        if len(str2) > 0:
            for mix in string_mixer(str1, str2[:-1], str2[-1] + current_mix):
                yield mix


def main():
    solved = False
    number_of_digits = 2
    while not solved:
        number_of_digits += 1
        smallest_prime = 10**number_of_digits
        for number_of_stars in range(3, number_of_digits - 1 + 1, 3):
            for base in range(1, 10**(number_of_digits - number_of_stars), 2):
                base_str = str(base)
                for template in string_mixer(
                        base_str[:-1],
                        "*" * number_of_stars,
                        base_str[-1]):
                    if (is_prime(int(template.replace("*", "1")))
                            or is_prime(int(template.replace("*", "2")))
                            or is_prime(int(template.replace("*", "3")))):
                        counter = 0
                        for digit_str in [str(d) for d in range(1, 10)]:
                            if is_prime(int(template.replace("*", digit_str))):
                                counter += 1
                        if (template[0] != "*"
                                and is_prime(int(template.replace("*", "0")))):
                            counter += 1
                        if counter == 8:
                            solved = True
                            if (template[0] != "*"
                                    and is_prime(int(
                                        template.replace("*", "0")))):
                                prime = int(template.replace("*", "0"))
                            elif is_prime(int(template.replace("*", "1"))):
                                prime = int(template.replace("*", "1"))
                            else:
                                prime = int(template.replace("*", "2"))
                            if prime < smallest_prime:
                                smallest_prime = prime
    print("Solution:", smallest_prime)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
