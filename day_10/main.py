#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

import re
import numpy as np
from PIL import Image


string = r"position=<([- ]?\d+), ([- ]?\d+)> velocity=<([- ]?\d+), ([- ]?\d+)>"


def load_import(file="input"):
    points = []
    velocities = []
    with open(f"{file}.txt", "r") as lines:
        for line in lines:
            m = re.match(string, line)
            points.append([int(i) for i in m.groups()[0:2]])
            velocities.append([int(i) for i in m.groups()[2:4]])
    points = np.array(points)
    velocities = np.array(velocities)
    return points, velocities


def points_to_matrix(points):
    normed_points = points - points.min(axis=0)
    matrix = np.zeros((normed_points[:, 1].max() + 1, normed_points[:, 0].max() + 1), np.uint8)
    matrix[normed_points[:, 1], normed_points[:, 0]] = 1
    return matrix


def get_points_shape(points):
    return points[:, 1].max() - points[:, 1].min(), points[:, 0].max() - points[:, 0].min()


def part_1():
    points, velocities = load_import()
    curr_points = points.copy()
    matrix_sizes = []
    smallest_time = 0
    for i in range(100000):
        curr_points += velocities
        matrix_shape = get_points_shape(curr_points)
        matrix_sizes.append(matrix_shape)
        if i > 2 and (matrix_sizes[-1][0] > matrix_sizes[-2][0]\
                      or matrix_sizes[-1][1] > matrix_sizes[-2][1]):
            # print(matrix_shape)
            smallest_time = i
            break
    # print(smallest_time)
    for i in range(smallest_time - 5, smallest_time + 5):
        curr_points = points + i * velocities
        matrix = points_to_matrix(curr_points)
        string_matrix = np.chararray(matrix.shape)
        string_matrix[:] = "."
        string_matrix[matrix == 1] = "#"
        # [print("".join(i)) for i in string_matrix.decode("utf-8")]
        # print()
        Image.fromarray((1 - matrix) * 255).save(f"img-{i}.png")
    return "Check Images"


def part_2():
    points, velocities = load_import()
    curr_points = points.copy()
    matrix_sizes = []
    smallest_time = 0
    for i in range(100000):
        curr_points += velocities
        matrix_shape = get_points_shape(curr_points)
        matrix_sizes.append(matrix_shape)
        # print(matrix_shape)
        if i > 2 and (matrix_sizes[-1][0] > matrix_sizes[-2][0]\
                      or matrix_sizes[-1][1] > matrix_sizes[-2][1]):
            # print(matrix_shape)
            smallest_time = i
            break
    # print(smallest_time)
    return smallest_time


if __name__ == '__main__':
    print("Day 9 - Part 1 - What message will eventually appear in the sky?", part_1())
    # Result: -- XLZAKBGZ

    print("Day 9 - Part 2 - exactly how many seconds would they have needed "
          "to wait for that message to appear?:", part_2())
    # Result: -- 10656
