#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

from collections import deque


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.read()
    values = content.split()
    players = int(values[0])
    last_marble = int(values[6])
    return players, last_marble


def main(players, last_marble):
    marbles = deque([0])
    scores = [0] * players
    for i in range(1, last_marble + 1):
        if i % 23 == 0:
            marbles.rotate(7)
            removed = marbles.pop()
            scores[i % players] += i + removed
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(i)

    return max(scores)


def part_1():
    players, last_marble = load_import()
    highest_score = main(players, last_marble)
    return highest_score


def part_2():
    players, last_marble = load_import()
    last_marble *= 100
    highest_score = main(players, last_marble)
    return highest_score


if __name__ == '__main__':
    print("Day 9 - Part 1 - What is the winning Elf's score?:", part_1())
    # Result: -- 398371

    print("Day 9 - Part 2 - What would the new winning Elf's score be"
          "if the number of the last marble were 100 times larger?:", part_2())
    # Result: -- 3212830280
