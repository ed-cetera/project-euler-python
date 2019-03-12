#!/usr/bin/env python3

import time


def alphabetical_value(name):
    value = 0
    for character in name:
        value += ord(character) - 64
    return value


def main():
    try:
        with open("p022_names.txt", "r") as names_file:
            names = names_file.read().replace('"', "").split(",")
    except FileNotFoundError:
        print("ERROR: File",
              "https://projecteuler.net/project/resources/p022_names.txt",
              "has to be provided.")
        return
    names.sort()
    total_sum = 0
    for position in range(len(names)):
        total_sum += (position + 1) * alphabetical_value(names[position])
    print("Solution:", total_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
