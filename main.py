import sys


def load_module(module):
    module_path = module
    if module_path in sys.modules:
        return sys.modules[module_path]
    return __import__(module_path, fromlist=[module])


# Change only this two variables
year = 2020
day = 13


def main():
    m = load_module(f'y{year}.d{day:02d}')
    m.main(f"y{year}/input/{day}.txt")


if __name__ == '__main__':
    main()
