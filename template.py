def first(data):

    return


def second(data):

    return


def readFile(path):
    data = [line.strip() for line in open(path, 'r')]
    return data


def main(path):
    data = readFile(path)
    print(f"First: {first(data)}")
    print(f"Second: {second(data)}")
