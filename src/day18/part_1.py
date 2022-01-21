from src.day18.helpers import add, magnitude, parse_pair, reduce_pair
from src.global_helpers import read_input


def main():

    lines = read_input(18, 1)

    pairs = [parse_pair(line) for line in lines]

    pairs_sum = pairs[0]
    for pair in pairs[1:]:
        pairs_sum = reduce_pair(add(pairs_sum, pair))

    return magnitude(pairs_sum)


if __name__ == "__main__":
    print(main())
