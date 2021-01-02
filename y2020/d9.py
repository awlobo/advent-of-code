def first(data):

    data.append(0)
    data.append(max(data) + 3)
    data.sort()

    ones = sum([data[i + 1] - data[i] == 1 for i in range(len(data) - 1)])
    threes = sum([data[i + 1] - data[i] == 3 for i in range(len(data) - 1)])

    return ones*threes

def second(data):

    max_list = max(data) + 3
    data.append(max_list)
    data.append(0)
    data = sorted(data, reverse=True)

    to_end = {max_list: 1}

    for item in data[1:]:
        total = 0
        for i in range(3):
            if item + i + 1 in to_end:
                total += to_end[item + i + 1]

        to_end[item] = total

    return to_end[0]