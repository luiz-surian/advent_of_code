#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

from string import ascii_lowercase
from pprint import pprint
import operator


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.read()
    return content.strip()


def redact(polymer):
    counter = 0
    while True:
        for letter in ascii_lowercase:
            group1 = str(letter + letter.upper())
            group2 = str(letter.upper() + letter)
            # print('Searching: ', group1, group2)
            if group1 in polymer or group2 in polymer:
                # print("found")
                polymer = polymer.replace(group1, '').replace(group2, '')
                counter += 1
            else:
                # print("not found")
                pass
            # print(polymer, "counter: ", counter)
        if counter == 0:
            return polymer
        else:
            # print("\nLet's search again")
            counter = 0


def part_1():
    polymer = load_import()
    # print("Begin:", polymer, "\nlength:", len(polymer))
    polymer = redact(polymer)
    # print("end:", polymer, "\nlength:", len(polymer))
    return len(polymer)


def part_2():
    original_polymer = load_import()
    polymers = {}
    for letter in ascii_lowercase:
        # print(f"Removing ({letter}) and ({letter.upper()})")
        polymer = original_polymer.replace(letter, '').replace(letter.upper(), '')
        polymer = redact(polymer)
        polymers[letter] = len(polymer)
    # pprint(polymers)
    lower = min(polymers.items(), key=operator.itemgetter(1))[0]
    return polymers[lower]


if __name__ == '__main__':
    print("Day 5 - Part 1 - How many units remain after fully reacting the polymer you scanned?:", part_1())
    # Result: -- 11894

    print("Day 5 - Part 2 - What is the length of the shortest polymer you can produce"
          " by removing all units of exactly one type and fully reacting the result?:", part_2())
    # Result: -- Removing k: 5310
