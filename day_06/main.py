#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

import operator


def load_import(file="input"):
    challenge = []
    with open(f"{file}.txt", "r") as f:
        content = f.readlines()
    content = [x.strip().split(", ") for x in content]
    for item in content:
        challenge.append([int(i) for i in item])
    if file == "input":
        size = 360
    else:
        size = 10
    return challenge, size


def part_1():
    challenge, size = load_import()
    coordinates = dict(enumerate(challenge))
    area = {}
    for i in range(len(coordinates)):
        area[i] = {"border": False, "size": 0}
    # Calculate Manhattan Distance of every point
    for a in range(size):
        for b in range(size):
            point = {}
            for coord_id, [c, d] in coordinates.items():
                manhattan_distance = abs(a - c) + abs(b - d)
                # print(f"point: (x: {a}, y: {b}) -- Coord Id {coord_id}, Manhattan Distance: {manhattan_distance}")
                point[coord_id] = manhattan_distance
            shortest = min(point.items(), key=operator.itemgetter(1))[0]
            counts = len([x for x in point.values() if x == point[shortest]])
            if counts == 1:
                area[shortest]["size"] += 1
                # Check if area is finite (Don't touch the border)
                if a == 0 or b == 0 or a == size or b == size:
                    area[shortest]["border"] = True
                # print(f"Shortest distance from point (x: {a}, y: {b})"
                #       f" -- Coord Id: {shortest} (Manhattan Distance: {point[shortest]})")
            else:
                # print(f"Shortest distance from point (x: {a}, y: {b}) -- None (Multiple Occurrences)")
                pass
    # print(area)
    finite = {}
    for coord_id, value in area.items():
        if value["border"] is False:
            finite[coord_id] = value["size"]
    # print(finite)
    largest = max(finite.items(), key=operator.itemgetter(1))[0]
    # print(f"Coord Id: {largest}, size: {finite[largest]}")
    return finite[largest]


def part_2():
    challenge, size = load_import()
    coordinates = dict(enumerate(challenge))
    area = {}
    for x in range(size):
        for y in range(size):
            area[f"{x},{y}"] = 0

    for point in area:
        a, b = [int(i) for i in point.split(",")]
        for coord_id, [c, d] in coordinates.items():
            manhattan_distance = abs(a - c) + abs(b - d)
            area[f"{a},{b}"] += manhattan_distance

    total = 0
    for point, size in area.items():
        if size < 10000:
            total += 1
    return total


if __name__ == '__main__':
    print("Day 6 - Part 1 - What is the size of the largest area that isn't infinite?:", part_1())
    # Result: -- 4887

    print("Day 6 - Part 2 - What is the size of the region containing all locations which"
          "have a total distance to all given coordinates of less than 10000?:", part_2())
    # Result: -- 34096
