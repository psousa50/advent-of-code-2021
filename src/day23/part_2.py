from src.day23.helpers import read_amphipods, solve
from src.global_helpers import execute, read_input_raw


def main():
    lines = read_input_raw(23, 1)

    extra_lines = [
        "  #D#C#B#A#  ",
        "  #D#B#A#C#  ",
    ]

    lines = lines[0:3] + extra_lines + lines[3:]

    amphipods = read_amphipods(lines, 4)

    minimum_cost = solve(amphipods)

    return minimum_cost


if __name__ == "__main__":
    execute(main)
