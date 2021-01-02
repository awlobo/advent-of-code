# Each group's answers are separated by a blank line,
# Each person's answers are on a single line
# Only counts yes



# For each group, count the number of questions to which anyone answered "yes". 
# What is the sum of those counts?
def first(groups):
    p1 = sum(len(set.union(*group)) for group in groups)
    return p1



# identify the questions to which everyone answered "yes" in the same group
# For each group, count the number of questions to which everyone answered "yes". 
# What is the sum of those counts?
def second(groups):
    p2 = sum(len(set.intersection(*group)) for group in groups)
    return p2


def main(path):
    data = [line.strip() for line in open(path, 'r')]
    for i in range(len(data)):
        if data[i] == "":
            data[i] = "\n"
    rawGroups = " ".join(data).split("\n")
    groups = [[set(answer) for answer in rawGroup.split()]
              for rawGroup in rawGroups]

    print(f"First: {first(groups)}")
    print(f"Second: {second(groups)}")
