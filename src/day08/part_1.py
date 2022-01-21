from typing import List
from src.global_helpers import read_input
from src.day08.helpers import read_entries


def main():
    lines = read_input(8, 1)

    entries = read_entries(lines)

    output_values: List[int] = []
    for entry in entries:
        output_values += entry.output_values

    unique = [u for u in output_values if len(u) in [2, 3, 4, 7]]

    return len(unique)


if __name__ == "__main__":
    print(main())
