#!/usr/bin/python
# -*- coding: utf-8 -*-

"""AOC - Coding Challenge [https://adventofcode.com/2018]"""
__author__ = "Luiz Fernando Surian Filho"

from datetime import datetime
import operator


def load_import(file="input"):
    with open(f"{file}.txt", "r") as f:
        content = f.readlines()
    return [str(x.strip()) for x in content]


def get_timestamp(string):
    return datetime.strptime(string[string.find("[")+1:string.find("]")], '%Y-%m-%d %H:%M')


def part_1():
    timeline = load_import()
    timeline.sort()

    holder_minutes = {"total": 0}
    for i in range(60):
        holder_minutes[i] = 0

    guards = {}
    current_guard = 0
    sleep = None

    for step in timeline:
        timestamp = get_timestamp(step)
        if step[25] == '#':
            current_guard = int(step[26:].strip(' begins shift'))
            if current_guard not in guards:
                guards[current_guard] = dict(holder_minutes)
        elif "falls asleep" in step:
            sleep = timestamp
        elif "wakes up" in step:
            td = timestamp - sleep
            td_mins = int(round(td.total_seconds() / 60))
            guards[current_guard]["total"] += td_mins
            for minute in range(td_mins):
                guards[current_guard][sleep.minute+minute] += 1

    most_slept = {
        "guard_id": 0,
        "minutes": 0
    }
    for guard in guards:
        slept = guards[guard]["total"]
        if slept > most_slept["minutes"]:
            most_slept = {
                "guard_id": guard,
                "minutes": slept
            }

    del guards[most_slept["guard_id"]]["total"]
    minute_most_slept = max(guards[most_slept["guard_id"]].items(), key=operator.itemgetter(1))[0]

    return most_slept["guard_id"] * minute_most_slept


def part_2():
    timeline = load_import()
    timeline.sort()

    holder_minutes = {}
    for i in range(60):
        holder_minutes[i] = 0

    guards = {}
    current_guard = 0
    sleep = None

    for step in timeline:
        timestamp = get_timestamp(step)
        if step[25] == '#':
            current_guard = int(step[26:].strip(' begins shift'))
            if current_guard not in guards:
                guards[current_guard] = dict(holder_minutes)
        elif "falls asleep" in step:
            sleep = timestamp
        elif "wakes up" in step:
            td = timestamp - sleep
            td_mins = int(round(td.total_seconds() / 60))
            for minute in range(td_mins):
                guards[current_guard][sleep.minute+minute] += 1

    answer = {
        'higher': 0,
        'guard': 0,
        'minute': 0
    }
    for guard in guards:
        for minute in guards[guard]:
            slept = guards[guard][minute]
            if slept > answer['higher']:
                answer = {
                    'higher': slept,
                    'guard': guard,
                    'minute': minute
                }

    return answer['guard'] * answer['minute']


if __name__ == '__main__':
    print("Day 4 - Part 1 - What is the ID of the guard you chose multiplied by the minute you chose?:", part_1())
    # Result: -- 125444

    print(f"Day 4 - Part 2 - What is the ID of the guard you chose multiplied by the minute you chose?:", part_2())
    # Result: -- 18325
