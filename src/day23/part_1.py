from src.day23.helpers import read_amphipods, solve
from src.global_helpers import execute, read_input_raw


def main():
    lines = read_input_raw(23, 1)

    amphipods = read_amphipods(lines, 2)

    minimum_cost = solve(amphipods)

    return minimum_cost


if __name__ == "__main__":
    execute(main)
