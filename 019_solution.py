#!/usr/bin/env python3

import time


def days_since_1900_01_01(y, m, d):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for Y in range(1900, y):
        days += 365
        if Y % 4 == 0:
            days += 1
        if Y % 100 == 0:
            days -= 1
        if Y % 400 == 0:
            days += 1
    for M in range(1, m):
        days += days_in_month[M - 1]
        if M == 2:
            if y % 4 == 0:
                days += 1
            if y % 100 == 0:
                days -= 1
            if y % 400 == 0:
                days += 1
    days += d - 1
    return days


def main():
    counter = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if days_since_1900_01_01(year, month, 1) % 7 == 6:
                counter += 1
    print("Solution:", counter)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
