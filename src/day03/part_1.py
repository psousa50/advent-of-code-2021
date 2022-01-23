from src.global_helpers import read_input
from src.day03.helpers import most_common_bit


def main():
    bytes = read_input(3, 1)

    binary_length = len(bytes[0])

    most_common = [most_common_bit(bytes, bit_index) for bit_index in range(binary_length)]

    most_common_binary = "".join([str(s) for s in most_common])

    game_rate = int(most_common_binary, 2)

    inverted_most_common = [1 if c == 0 else 0 for c in most_common]

    inverted_most_common_binary = "".join([str(s) for s in inverted_most_common])

    epsilon_rate = int(inverted_most_common_binary, 2)

    return game_rate * epsilon_rate


if __name__ == "__main__":
    print(main())
