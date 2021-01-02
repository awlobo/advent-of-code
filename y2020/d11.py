# https://adventofcode.com/2020/day/11

moves = [(0, 1), (1, 0), (0, -1), (-1, 0),
         (1, 1), (1, -1), (-1, 1), (-1, -1)]


def first(data):
    h, w = len(data), len(data[0])

    hasChanged = True
    while hasChanged:
        newSeats = [l[:] for l in data]
        hasChanged = False
        for a in range(h):
            for b in range(w):
                n = 0
                for da, db in moves:
                    if da == 0 and db == 0:
                        continue

                    if 0 <= a+da < h and 0 <= b+db < w:
                        if data[a+da][b+db] == "#":
                            n += 1

                if data[a][b] == "L" and n == 0:
                    newSeats[a][b] = "#"
                    hasChanged = True
                elif data[a][b] == "#" and n >= 4:
                    newSeats[a][b] = "L"
                    hasChanged = True

        data = newSeats

    return sum(l.count("#") for l in data)


def second(data):

    h, w = len(data), len(data[0])

    hasChanged = True
    while hasChanged:
        hasChanged = False
        newSeats = [l[:] for l in data]
        for a in range(h):
            for b in range(w):
                n = 0
                for da, db in moves:
                    ca, cb = a, b
                    while 0 <= ca+da < h and 0 <= cb+db < w:
                        ca += da
                        cb += db

                        if data[ca][cb] == "#":
                            n += 1

                        if data[ca][cb] != ".":
                            break

                if data[a][b] == "L" and n == 0:
                    newSeats[a][b] = "#"
                    hasChanged = True
                elif data[a][b] == "#" and n >= 5:
                    newSeats[a][b] = "L"
                    hasChanged = True

        data = newSeats

    return sum(l.count("#") for l in data)


def readFile(path):
    data = [line.strip() for line in open(path, 'r')]
    seats = [l[:] for l in [list(l) for l in data]]
    return seats


def main(path):
    data = readFile(path)
    print(f"First: {first(data)}")
    print(f"Second: {second(data)}")
