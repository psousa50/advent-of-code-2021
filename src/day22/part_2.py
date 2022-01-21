from src.day22.helpers import apply_steps, read_steps
from src.global_helpers import read_input


def main():

    lines = read_input(22, 1)

    steps = read_steps(lines)

    cubes = apply_steps(steps)

    return sum([cube.size() for cube in cubes])


if __name__ == "__main__":
    print(main())
