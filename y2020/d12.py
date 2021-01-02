# The ship starts by facing east
dirs = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
rot = {'L': 1j, 'R': -1j}


def main(path):
    raw = [line.strip() for line in open(path, 'r')]
    data = [(line[0], int(line[1:])) for line in raw]
    print(f"First: {first(data)}")
    print(f"Second: {second(data)}")


"""
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing. 
"""


# Figure out where the navigation instructions lead.
# What is the Manhattan distance between that location and the ship's starting position?
def first(data):
    loc = 0
    d = 1
    for a, value in data:
        if a in dirs:
            loc += dirs[a] * value
        elif a in rot:
            d *= rot[a] ** (value/90)
        else:
            loc += d * value
    return int(abs(loc.real) + abs(loc.imag))


"""
Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
"""


# Figure out where the navigation instructions actually lead.
# What is the Manhattan distance between that location and the ship's starting position?
def second(data):
    loc = 0
    waypoint = 10 + 1j
    for a, value in data:
        if a in dirs:
            waypoint += dirs[a] * value
        elif a in rot:
            waypoint *= rot[a] ** (value/90)
        else:
            loc += waypoint * value
    return int(abs(loc.real) + abs(loc.imag))
