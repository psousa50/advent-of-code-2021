from src.global_helpers import read_input
from src.day17.helpers import find_solutions


def main():
    lines = read_input(17, 1)

    solutions = find_solutions(lines)

    return len(solutions)


if __name__ == "__main__":
    print(main())
