# F == "front", B == "back", L == "left", R == "right"
# 128 rows on the plane (numbered 0 through 127)
# seat ID: multiply the row by 8, then add the column number
"""
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""


# What is the highest seat ID on a boarding pass?
def first(data, seatIDs):
    for boardingPass in data:
        lo, hi = 0, (2 ** len(boardingPass)) - 1
        for c in boardingPass:
            mid = (lo + hi) // 2
            if c in "FL":
                hi = mid
            elif c in "BR":
                lo = mid
        seatID = hi
        seatIDs.append(seatID)
    return "{}".format(max(seatIDs))


# the seats at the very front and back of the plane don't exist
# The seats with IDs +1 and -1 from yours will be in your list.
# What is the ID of your seat?
def second(data, seatIDs):
    allSeats = set(range(min(seatIDs), max(seatIDs) + 1))
    missingSeats = allSeats - set(seatIDs)  # Assume len(missingSeats) == 1
    return "{}".format(missingSeats.pop())


def main(path):
    seatIDs = []
    data = [line.strip() for line in open(path, 'r')]
    print(f"First: {first(data, seatIDs)}")
    print(f"Second: {second(data, seatIDs)}")
