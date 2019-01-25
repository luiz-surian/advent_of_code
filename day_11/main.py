#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

import numpy as np


def load_import(file="input"):
    grid_size = 300
    if file == "input":
        with open(f"{file}.txt", "r") as f:
            content = int(f.read())
        return content, grid_size
    else:
        return 57, grid_size


def find_power_level(grid_serial_number, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    assert -5 <= power_level <= 4
    return power_level


def test():
    """
    Fuel cell at   3,   5, grid serial number  8: power level  4.
    Fuel cell at 122,  79, grid serial number 57: power level -5.
    Fuel cell at 217, 196, grid serial number 39: power level  0.
    Fuel cell at 101, 153, grid serial number 71: power level  4.
    """
    assert find_power_level(8, 3, 5) == 4
    assert find_power_level(57, 122, 79) == -5
    assert find_power_level(39, 217, 196) == -0
    assert find_power_level(71, 101, 153) == 4
    return True


def generate_matrix(grid_serial_number, grid_size):
    array = []
    for x in range(grid_size):
        hold = []
        for y in range(grid_size):
            hold.append(find_power_level(grid_serial_number, x, y))
        array.append(list(hold))
    array = np.array(array)
    return array


def part_1():
    grid_serial_number, grid_size = load_import()
    matrix = generate_matrix(grid_serial_number, grid_size)

    chunk_size = 3
    highest_power = 0
    coordinates = ""
    for x in range(grid_size - chunk_size):
        for y in range(grid_size - chunk_size):
            power = np.sum(matrix[x:x + chunk_size, y:y + chunk_size])
            if power > highest_power:
                highest_power = power
                coordinates = f"{x},{y}"
    # print(coordinates, highest_power)
    return coordinates


def part_2():
    grid_serial_number, grid_size = load_import()
    matrix = generate_matrix(grid_serial_number, grid_size)

    # chunk_size = 1 ~ 300
    highest_power = 0
    coordinates = ""
    for chunk_size in range(1, 301):
        for x in range(grid_size - chunk_size):
            for y in range(grid_size - chunk_size):
                power = np.sum(matrix[x:x + chunk_size, y:y + chunk_size])
                if power > highest_power:
                    highest_power = power
                    coordinates = f"{x},{y},{chunk_size}"
    # print(coordinates, highest_power)
    return coordinates


if __name__ == '__main__':
    assert test()

    print("Day 11 - Part 1 - What is the X,Y coordinate of the top-left fuel cell "
          "of the 3x3 square with the largest total power?:", part_1())
    # Result: -- 21,42

    print("Day 11 - Part 2 - What is the X,Y,size identifier of the "
          "square with the largest total power?:", part_2())
    # Result: -- 230,212,13
