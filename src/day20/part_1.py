from src.global_helpers import read_input

from src.day20.helpers import enhance_multiple


def main():
    lines = read_input(20, 1)

    light_count = enhance_multiple(lines, 2)

    return light_count


print(main())
