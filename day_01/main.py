#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]


def part_1():
    commands = load_import()
    return sum(commands)


def part_2():
    commands = load_import()
    occurrences = {0}
    value = 0

    while True:
        for i in commands:
            value += i
            if value not in occurrences:
                occurrences.add(value)
            else:
                return value


if __name__ == '__main__':
    print("Day 1 - Part 1 - What is the resulting frequency?:", part_1())
    # Result: -- 416

    print("Day 1 - Part 2 - What is the first frequency your device reaches twice?:", part_2())
    # Result: -- 56752
