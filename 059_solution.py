#!/usr/bin/env python3

import time


def main():
    english_letter_frequency = [0.08167, 0.01492, 0.02782, 0.04253, 0.01270,
                                0.02228, 0.02015, 0.06094, 0.06966, 0.00153,
                                0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
                                0.01929, 0.00095, 0.05987, 0.06327, 0.09056,
                                0.02758, 0.00978, 0.02360, 0.00150, 0.01974,
                                0.00074]
    maximum_similarity = 0
    try:
        with open("p059_cipher.txt", "r") as ciphertext_file:
            ciphertext = [int(c) for c in ciphertext_file.read().split(",")]
    except FileNotFoundError:
        print("ERROR: File",
              "https://projecteuler.net/project/resources/p059_cipher.txt",
              "has to be provided.")
        return
    for password in [[a, b, c] for a in range(97, 123) for b in range(97, 123)
                     for c in range(97, 123)]:
        key = (len(ciphertext)//len(password) + 1) * password
        text = [ciphertext[i] ^ key[i] for i in range(len(ciphertext))]
        letter_frequency = 26 * [0]
        for character in text:
            if 65 <= character <= 90:
                letter_frequency[character - 65] += 1/len(text)
            elif 97 <= character <= 122:
                letter_frequency[character - 97] += 1/len(text)
        similarity = sum([english_letter_frequency[i] * letter_frequency[i]
                          for i in range(26)])
        if similarity > maximum_similarity:
            maximum_similarity = similarity
            character_sum = sum(text)
    print("Solution:", character_sum)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
