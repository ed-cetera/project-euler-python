#!/usr/bin/env python3

import math
import time


def is_triangle_word(word):
    word_value = 0
    for character in word:
        word_value += ord(character) - 64
    return ((math.sqrt(8 * word_value + 1) - 1) / 2).is_integer()


def main():
    try:
        with open("p042_words.txt", "r") as words_file:
            words = words_file.read().replace('"', "").split(",")
    except FileNotFoundError:
        print("ERROR: File",
              "https://projecteuler.net/project/resources/p042_words.txt",
              "has to be provided.")
        return
    counter = 0
    for word in words:
        if is_triangle_word(word):
            counter += 1
    print("Solution:", counter)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
