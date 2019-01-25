#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

from string import ascii_uppercase
# from pprint import pprint


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.readlines()
    rules = {
        "input": [str(x.strip()) for x in content],
        "size": len(ascii_uppercase),
        "offset": 60,
        "workers": 5
    }
    if file != "input":
        rules["size"] = 6
        rules["offset"] = 0
        rules["workers"] = 2
    return rules


def part_1():
    rules = load_import()
    requirements = {}
    for letter in ascii_uppercase:
        requirements[letter] = []
    for rule in rules["input"]:
        lines = rule.split(" ")
        needs = lines[1]
        step = lines[7]
        requirements[step].append(needs)
    # pprint(requirements)
    solution = []
    while len(solution) < rules["size"]:
        # Check for steps with no dependencies:
        buffer = []
        for step, req in requirements.items():
            # Check if is empty
            if not req:
                buffer.append(step)
        buffer.sort()
        # Solve just one step
        solved = buffer[0]
        solution.append(solved)
        # Remove solved steps from requirements:
        requirements.pop(solved)
        for step in requirements:
            try:
                requirements[step].remove(solved)
            except ValueError:
                pass
    # print(solution)
    # Example solution: CABDFE
    return "".join(solution)


def part_2():
    def time(c):
        return rules["offset"] + ord(c) - ord("A")

    def next_step(steps, l):
        return [s for s in steps if all(b != s for (_, b) in l)]

    rules = load_import()
    lines = []
    for rule in rules["input"]:
        line = rule.split(" ")
        needs = line[1]
        step = line[7]
        lines.append((needs, step))

    steps = set([s[0] for s in lines] + [s[1] for s in lines])

    t = 0
    workers = [0 for _ in range(rules["workers"])]
    work = [None for _ in range(rules["workers"])]
    while steps or any(w > 0 for w in workers):
        cand = list(next_step(steps, lines))
        cand.sort()
        cand = cand[::-1]

        for i in range(rules["workers"]):
            workers[i] = max(workers[i] - 1, 0)
            if workers[i] == 0:
                if work[i] is not None:
                    lines = [(a, b) for (a, b) in lines if a != work[i]]
                if cand:
                    n = cand.pop()
                    workers[i] = time(n)
                    work[i] = n
                    steps.remove(n)
        t += 1
    return t


if __name__ == '__main__':
    print("Day 7 - Part 1 - In what order should the steps in your instructions be completed?:", part_1())
    # Result: -- OUGLTKDJVBRMIXSACWYPEQNHZF

    print("Day 7 - Part 2 - How much time with 5 workers:", part_2())
    # Result: -- 929
