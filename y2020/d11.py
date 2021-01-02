import time


def get_immediate_neighbors(puzzle, r, i):
    neigh_diffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                   (0, 1), (1, -1), (1, 0), (1, 1)]
    return [puzzle[r + d[0]][i + d[1]] for d in neigh_diffs
            if 0 <= r + d[0] < len(puzzle)
            and 0 <= i + d[1] < len(puzzle[r])]


def get_view_neighbors(puzzle, r, i):
    neigh_diffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                   (0, 1), (1, -1), (1, 0), (1, 1)]
    neighs = []
    for d in neigh_diffs:
        id_r = r + d[0]
        id_s = i + d[1]
        while 0 <= id_r < len(puzzle) and 0 <= id_s < len(puzzle[r]) and puzzle[id_r][id_s] == '.':
            id_r += d[0]
            id_s += d[1]
        if 0 <= id_r < len(puzzle) and 0 <= id_s < len(puzzle[r]):
            neighs.append(puzzle[id_r][id_s])
    return neighs


def wait_for_seated(puzzle, get_neigh, max_neigh):
    change = True
    while change:
        change = False
        new_puzzle = [r.copy() for r in puzzle]
        for r in range(0, len(puzzle)):
            row = puzzle[r]
            for i in range(0, len(row)):
                if row[i] == ".":
                    continue
                neighs = get_neigh(puzzle, r, i)
                if row[i] == "L" and neighs.count("#") == 0:
                    new_puzzle[r][i] = "#"
                    change = True
                elif row[i] == "#" and neighs.count("#") > max_neigh:
                    new_puzzle[r][i] = "L"
                    change = True
        puzzle = [r.copy() for r in new_puzzle]
    return ''.join([''.join(r) for r in puzzle]).count('#')


def first(data):
    return wait_for_seated(data, get_immediate_neighbors, 3)


def second(data):
    return wait_for_seated(data, get_view_neighbors, 4)
