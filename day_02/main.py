#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

from string import ascii_lowercase
import difflib


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.readlines()
    return [str(x.strip()) for x in content]


def part_1():
    words = load_import()
    _2times = 0
    _3times = 0
    for box in words:
        count = {}
        for letter in ascii_lowercase:
            count[letter] = box.count(letter)
        #  print(f'{box}: {count}')
        if any(value == 2 for value in count.values()):
            _2times += 1
        if any(value == 3 for value in count.values()):
            _3times += 1
    return _2times * _3times


def part_2():
    def xor_two_str(a, b):
        s_xor = []
        for i in range(max(len(a), len(b))):
            xor_value = ord(a[i % len(a)]) ^ ord(b[i % len(b)])
            s_xor.append(hex(xor_value)[2:])
        return s_xor

    words = load_import()
    hold = []
    diff = []
    length = len(words[0])
    for box in words:
        for second_box in words:
            if box == second_box:
                # Ignore
                pass
            else:
                xor = xor_two_str(box, second_box)
                equals = xor.count("0")
                # print(f'{box} ^ {second_box} = {xor} ({equals})')
                if equals == length - 1:
                    hold.append(f'{box} - {second_box} ({xor})')
                    diff = list(difflib.ndiff(box, second_box))

    # pnebjqsalrdnckzfihvtxysomg - prebjqsalrdnckzfihvtxysomg
    # (['0', '1c', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    final = ''
    for letter in diff:
        if letter[0] == ' ':
            final += letter[2]
    return final


if __name__ == '__main__':
    print("Day 2 - Part 1 - What is the checksum for your list of box IDs?:", part_1())
    # Result: -- 4693

    print("Day 2 - Part 2 - What letters are common between the two correct box IDs?:", part_2())
    # Result: -- pebjqsalrdnckzfihvtxysomg