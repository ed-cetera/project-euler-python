#!/usr/bin/env python3

import time


def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    target_sum = 200

    def split_in_coins(counter, current_sum, target_sum, coins):
        for coin in coins:
            if current_sum + coin == target_sum:
                counter += 1
            elif current_sum + coin < target_sum:
                counter = split_in_coins(counter,
                                         current_sum + coin,
                                         target_sum,
                                         coins[coins.index(coin):])
        return counter

    print("Solution:", split_in_coins(0, 0, target_sum, coins))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
