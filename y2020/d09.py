# https://adventofcode.com/2020/day/9

import itertools

def first(data):
    for i in range(25, len(data)):
        p = data[i-25:i]
        v = {-1}
        for a in p:
            v |= {a+b for b in p if a != b}
        if not data[i] in v:
            return data[i]


def second(data, first):
    for i in range(len(data)):
        sum = 0
        k = i
        while sum < first:
            sum += data[k]
            k += 1
        if sum == first:
            return min(data[i:k]) + max(data[i:k])


def readFile(path):
    data = [int(line.strip()) for line in open(path, 'r')]
    return data


def main(path):
    data = readFile(path)
    print(f"First: {first(data)}")
    print(f"Second: {second(data, first(data))}")
