#!/usr/bin/env python3

import time


def value_from_hand(cards):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    cards = [(ranks.index(card[0]), card[1]) for card in cards]
    cards = sorted(cards, key=lambda card: card[0])

    straight = True
    flush = True
    for i in range(1, 5):
        if cards[i][0] - cards[i-1][0] != 1:
            straight = False
        if cards[i][1] != cards[0][1]:
            flush = False
    if straight and flush:
        value_str = hex(cards[4][0])[2:] + "00000000000000"
    elif flush:
        value_str = "000010000000000"
    elif straight:
        value_str = "00000" + hex(cards[4][0])[2:] + "000000000"
    else:
        if ((cards[0][0] == cards[1][0] or cards[4][0] == cards[1][0])
                and cards[1][0] == cards[2][0] == cards[3][0]):
            value_str = "0" + hex(cards[1][0])[2:] + "0000000000000"
        elif (cards[0][0] == cards[1][0] == cards[2][0]
                and cards[3][0] == cards[4][0]):
            value_str = ("00" + hex(cards[0][0])[2:] + hex(cards[3][0])[2:]
                         + "00000000000")
        elif (cards[0][0] == cards[1][0]
                and cards[2][0] == cards[3][0] == cards[4][0]):
            value_str = ("00" + hex(cards[2][0])[2:] + hex(cards[0][0])[2:]
                         + "00000000000")
        elif (cards[0][0] == cards[1][0] == cards[2][0]
                or cards[1][0] == cards[2][0] == cards[3][0]
                or cards[2][0] == cards[3][0] == cards[4][0]):
            value_str = "000000" + hex(cards[2][0])[2:] + "00000000"
        elif cards[0][0] == cards[1][0]:
            if cards[2][0] == cards[3][0]:
                value_str = ("0000000" + hex(cards[2][0])[2:]
                             + hex(cards[0][0])[2:] + "0"
                             + hex(cards[4][0])[2:] + "0000")
            elif cards[3][0] == cards[4][0]:
                value_str = ("0000000" + hex(cards[3][0])[2:]
                             + hex(cards[0][0])[2:] + "0"
                             + hex(cards[2][0])[2:] + "0000")
            else:
                value_str = ("000000000" + hex(cards[0][0])[2:]
                             + hex(cards[4][0])[2:] + hex(cards[3][0])[2:]
                             + hex(cards[2][0])[2:] + "00")
        elif cards[1][0] == cards[2][0]:
            if cards[3][0] == cards[4][0]:
                value_str = ("0000000" + hex(cards[3][0])[2:]
                             + hex(cards[1][0])[2:] + "0"
                             + hex(cards[0][0])[2:] + "0000")
            else:
                value_str = ("000000000" + hex(cards[1][0])[2:]
                             + hex(cards[4][0])[2:] + hex(cards[3][0])[2:]
                             + hex(cards[0][0])[2:] + "00")
        elif cards[2][0] == cards[3][0]:
            value_str = ("000000000" + hex(cards[2][0])[2:]
                         + hex(cards[4][0])[2:] + hex(cards[1][0])[2:]
                         + hex(cards[0][0])[2:] + "00")
        elif cards[3][0] == cards[4][0]:
            value_str = ("000000000" + hex(cards[3][0])[2:]
                         + hex(cards[2][0])[2:] + hex(cards[1][0])[2:]
                         + hex(cards[0][0])[2:] + "00")
        else:
            value_str = ("0000000000" + hex(cards[4][0])[2:]
                         + hex(cards[3][0])[2:] + hex(cards[2][0])[2:]
                         + hex(cards[1][0])[2:] + hex(cards[0][0])[2:])
    return int(value_str, 16)


def main():
    wins_player1 = 0
    try:
        with open("p054_poker.txt", "r") as hands_file:
            for cards in hands_file:
                hand_player1 = cards.strip().split(" ")[:5]
                hand_player2 = cards.strip().split(" ")[5:]
                if (value_from_hand(hand_player1)
                        > value_from_hand(hand_player2)):
                    wins_player1 += 1
    except FileNotFoundError:
        print("ERROR: File",
              "https://projecteuler.net/project/resources/p054_poker.txt",
              "has to be provided.")
        return
    print("Solution:", wins_player1)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Duration: {0:0.6f}s".format(end - start))
