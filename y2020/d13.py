# https://adventofcode.com/2020/day/13

import math


def first(start, buses):
    min_arrival = float("inf")
    min_bus = None
    for b in filter(bool, buses):
        next_arrival = b - start % b
        if next_arrival < min_arrival:
            min_arrival, min_bus = next_arrival, b
    return min_bus * min_arrival


def second(start, buses):
    M = math.prod(b for b in buses if b is not None)
    result = 0

    for i, b in enumerate(buses):
        if b is None:
            continue

        Mi = M // b
        mi = pow(Mi, -1, b)
        result += (-i) * Mi * mi

    return result % M


def readFile(path):
    data = [line.splitlines() for line in open(path, 'r')]
    start = int(data[0][0])
    buses = [int(b) if b != "x" else None for b in data[1][0].split(",")]
    return start, buses


def main(path):
    start, buses = readFile(path)
    print(f"First: {first(start, buses)}")
    print(f"Second: {second(start, buses)}")
