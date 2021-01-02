# open squares (.) and trees (#) the same pattern repeats
"""
Right 1, down 1.
Right 3, down 1. (first)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""


def count_trees(data, slope_x, slope_y):
    x = 0
    y = 0
    trees = 0
    while y < len(data):
        trees += data[y][x % len(data[0])] == '#'
        x += slope_x
        y += slope_y
    return trees

# Starting at the top-left corner of your map and following a slope
# of right 3 and down 1, how many trees would you encounter?


def first(data):
    return count_trees(data, 3, 1)

# What do you get if you multiply together the number of trees
# encountered on each of the listed slopes?


def second(data):
    return count_trees(data, 1, 1) * count_trees(data, 3, 1) * count_trees(data, 5, 1) * count_trees(data, 7, 1) * count_trees(data, 1, 2)


def main(path):
    data = [line.strip() for line in open(path, 'r')]
    print(f"First: {first(data)}")
    print(f"Second: {second(data)}")
