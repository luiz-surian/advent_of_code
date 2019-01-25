#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

from pprint import pprint


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.readlines()
    coordinates = [str(x.strip()) for x in content]

    if file == "input":
        size = 1000
    else:
        size = 8

    claims = {}
    for c in coordinates:
        claim_id, _, xy, wh = c.split(' ')
        x, y = xy.split(',')
        width, height = wh.split('x')
        claims[int(claim_id[1:])] = {
            'x': int(x),
            'y': int(y[:-1]),
            'width': int(width),
            'height': int(height)
        }

    return claims, size


def build_matrix(size):
    hold = [0] * size
    matrix = []
    for row in range(size):
        matrix.append(list(hold))
    return matrix


def part_1():
    claims, size = load_import()
    matrix = build_matrix(size)
    overlaps = 0
    for claim_id, claim in claims.items():
        for vertical in range(claim['height']):
            for horizontal in range(claim['width']):
                if matrix[claim['y'] + vertical][claim['x'] + horizontal] == '#':
                    # Ignore
                    pass
                elif matrix[claim['y'] + vertical][claim['x'] + horizontal] == 0:
                    matrix[claim['y'] + vertical][claim['x'] + horizontal] = claim_id
                else:
                    matrix[claim['y'] + vertical][claim['x'] + horizontal] = '#'
                    overlaps += 1

    # pprint(matrix)
    return overlaps


def part_2():
    claims, size = load_import()
    matrix = build_matrix(size)
    validate = {}
    for n in range(len(claims)):
        validate[n + 1] = 0

    for claim_id, claim in claims.items():
        for vertical in range(claim['height']):
            for horizontal in range(claim['width']):
                if matrix[claim['y'] + vertical][claim['x'] + horizontal] == 0:
                    matrix[claim['y'] + vertical][claim['x'] + horizontal] = claim_id
                else:
                    previous_claim = int(matrix[claim['y'] + vertical][claim['x'] + horizontal])
                    matrix[claim['y'] + vertical][claim['x'] + horizontal] = claim_id
                    validate[previous_claim] += 1
                    validate[claim_id] += 1

    for key, value in validate.items():
        if value == 0:
            return key


if __name__ == '__main__':
    print("Day 3 - Part 1 - How many square inches of fabric are within two or more claims?:", part_1())
    # Result: -- 109716

    print("Day 3 - Part 2 - What is the ID of the only claim that doesn't overlap?:", part_2())
    # Result: -- 124
