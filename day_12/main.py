#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

import numpy as np


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = [x.strip() for x in f.readlines()]
    initial_state = content[0].split()[2]
    rules = [rule.split(" => ") for rule in content[2:]]
    return initial_state, rules


def convert(plants):
    if type(plants) is str:
        return [int(x == "#") for x in plants]
    elif type(plants) is list:
        return "".join(["#" if x else "." for x in plants])
    else:
        raise TypeError


def part_1(generations=20):
    initial_state, rules = load_import()
    previous = convert(initial_state)
    current = list(previous)

    patterns = {}
    for before, after in rules:
        patterns[before] = int(after == "#")

    offset = 0
    for generation in range(generations):
        # print(generation, convert(current), offset)
        prev_offset = offset
        previous = [0] * 5 + previous + [0] * 5
        current = [0] * 5 + current + [0] * 5
        offset += 5

        for i in range(2, len(previous) - 3):
            pattern = convert(previous[i - 2: i + 3])
            current[i] = patterns[pattern] if pattern in patterns else 0

        current = np.trim_zeros(current, "f")
        offset -= len(previous) - len(current)
        current = np.trim_zeros(current, "b")
        previous = np.trim_zeros(previous)
        if np.array_equal(previous, current):
            # print(generation + 1, convert(current), offset)
            diff_offset = offset - prev_offset
            offset += diff_offset * (generations - generation - 1)
            break
        previous = list(current)

    # print(generations, convert(current), offset)
    total = 0
    for i in range(len(current)):
        if current[i]:
            total += i - offset
    return total


def part_2():
    return part_1(generations=50000000000)


if __name__ == '__main__':
    print("Day 12 - Part 1 - After 20 generations, what is the sum of "
          "the numbers of all pots which contain a plant?:", part_1())
    # Result: -- 3337

    print("Day 12 - Part 2 - After fifty billion (50000000000) generations, "
          "what is the sum of the numbers of all pots which contain a plant?:", part_2())
    # Result: -- 4300000000349
