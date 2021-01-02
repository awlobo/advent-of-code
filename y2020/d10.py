# https://adventofcode.com/2020/day/10

def first(data):
    data.sort()
    j1, j3 = 0, 0
    cur = 0
    for n in data:
        delta = n - cur
        j1 += int(delta == 1)
        j3 += int(delta == 3)
        cur += delta
    j3 += 1
    return j1*j3


def second(data):
    memo = [0] * (max(data) + 1)
    memo[0] = 1
    for n in data:
        l1 = memo[n-1] if n-1 >= 0 else 0
        l2 = memo[n-2] if n-2 >= 0 else 0
        l3 = memo[n-3] if n-3 >= 0 else 0
        memo[n] = l1 + l2 + l3
    return memo[-1]


def readFile(path):
    data = [int(line.strip()) for line in open(path, 'r')]
    return data


def main(path):
    data = readFile(path)
    print(f"First: {first(data)}")
    print(f"Second: {second(data)}")
