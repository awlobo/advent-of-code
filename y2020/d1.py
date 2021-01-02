# find the two entries that sum to 2020 and then multiply those two numbers together
def first(data): # 1006176
    set_nums = set(data)
    for num in data:
        if 2020 - num in set_nums:
            return num * (2020 - num)

# what is the product of the three entries that sum to 2020
def second(data): # 199132160
    set_nums = set(data)
    for num in data:
        for num2 in data:
            if (2020 - num - num2) in set_nums:
                return num * (2020 - num - num2) * num2

def main(path):
    data = [int(line.strip()) for line in open(path, 'r')]
    print(f"First: {first(data)}")
    print(f"Second: {second(data)}")