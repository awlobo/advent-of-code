# Each line gives the password policy and then the password.
# 1-3 a means that the password must contain a X letter at least 1 time and at most 3 times
# How many passwords are valid according to their policies?
def first(data): # 393
    valid = 0
    for w in data:
        lo, hi = list(map(int, w[0].split('-')))
        char = w[1][0]
        valid += lo <= w[2].count(char) <= hi
    return valid

# 1 means the first character, 2 means the second character, and so on.
# Exactly one of these positions must contain the given letter
def second(data): # 690
    valid = 0
    for w in data:
        a, b = list(map(int, w[0].split('-')))
        char = w[1][0]
        valid += (w[2][a - 1] == char) ^ (w[2][b - 1] == char)
    return valid


def main(path):
    data = [line.strip().split() for line in open(path, 'r')]
    print(f"First: {first(data)}")
    print(f"Second: {second(data)}")