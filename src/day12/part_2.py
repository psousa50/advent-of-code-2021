from collections import defaultdict, deque

from src.global_helpers import read_input
from src.day12.helpers import read_paths, find_solutions


def main():
    lines = read_input(12, 1)

    paths = read_paths(lines)

    solutions = find_solutions(paths, 1)

    return len(solutions)


if __name__ == "__main__":
    print(main())
