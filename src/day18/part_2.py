from src.day18.models import Pair
from src.day18.helpers import add, magnitude, parse_pair, reduce_pair
from src.global_helpers import read_input


def main():

    lines = read_input(18, 1)

    pairs = [parse_pair(line) for line in lines]

    largest_magnitude = 0
    for i1 in range(len(pairs)):
        for i2 in range(len(pairs)):
            if i1 != i2:
                largest_magnitude = max(largest_magnitude, magnitude(reduce_pair(add(pairs[i1], pairs[i2]))))

    return largest_magnitude


if __name__ == "__main__":
    print(main())
