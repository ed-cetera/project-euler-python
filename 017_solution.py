#!/usr/bin/env python3

import time


def num_to_string(number):
    # works from 0 to 9999
    string = ""
    ones_strings = ["zero", "one", "two", "three", "four", "five", "six",
                    "seven", "eight", "nine"]
    tens_strings = ["zero", "ten", "twenty", "thirty", "forty", "fifty",
                    "sixty", "seventy", "eighty", "ninety"]
    digits = [int(x) for x in str(number)]
    if len(digits) == 4:
        digit = digits.pop(0)
        string += ones_strings[digit]
        string += " thousand"
    if len(digits) == 3:
        digit = digits.pop(0)
        if digit > 0:
            if len(string) > 0:
                string += " "
            string += ones_strings[digit]
            string += " hundred"
    if len(digits) == 1:
        digit = digits.pop(0)
        string = ones_strings[digit]
    if len(digits) == 2:
        digit1 = digits.pop(0)
        digit2 = digits.pop(0)
        remainder = 10 * digit1 + digit2
        if remainder > 0:
            if len(string) > 0:
                string += " and "
            if 0 < remainder < 10:
                string += ones_strings[remainder]
            elif remainder == 10:
                string += "ten"
            elif remainder == 11:
                string += "eleven"
            elif remainder == 12:
                string += "twelve"
            elif remainder == 13:
                string += "thirteen"
            elif remainder == 14:
                string += "fourteen"
            elif remainder == 15:
                string += "fifteen"
            elif remainder == 16:
                string += "sixteen"
            elif remainder == 17:
                string += "seventeen"
            elif remainder == 18:
                string += "eighteen"
            elif remainder == 19:
                string += "nineteen"
            else:
                string += tens_strings[digit1]
                if digit2 > 0:
                    string += "-" + ones_strings[digit2]
    return string


def letters_in_string(string):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    return len(string)


def main():
    total_sum = 0
    for i in range(1, 1001):
        total_sum += letters_in_string(num_to_string(i))
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
