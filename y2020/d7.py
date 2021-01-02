import re

rules = {}
result = set()


def check(target_color):
    for color, contains in rules.items():
        if any(sub_color == target_color for _, sub_color in contains):
            result.add(color)
            check(color)


def check_count(color):
    return 1 + sum(count * check_count(sub_color) for count, sub_color in rules[color])



# How many bag colors can eventually contain at least one shiny gold bag?
def first():
    check("shiny gold")
    return len(result)



# How many individual bags are required inside your single shiny gold bag?
def second():
    return check_count("shiny gold") - 1


def main(path):
    with open(path) as f:
        for line in f.read().splitlines():
            color, rule = re.match(re.compile(r'(\w+ \w+) bags contain (.*)'), line).groups()
            rules[color] = [(int(match.group(1)), match.group(2)) for match in re.finditer(re.compile(r'(\d+) (\w+ \w+) bags?'), rule)]
    print(f"First: {first()}")
    print(f"Second: {second()}")
