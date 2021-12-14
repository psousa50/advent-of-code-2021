import helpers
from day03_helpers import most_common_bit

bytes = helpers.read_input(3, 1)

binary_length = len(bytes[0])

most_common = [most_common_bit(bytes, bit_index) for bit_index in range(binary_length)]

most_common_binary = "".join([str(s) for s in most_common])

game_rate = int(most_common_binary, 2)

inverted_most_common = [1 if c == 0 else 0 for c in most_common]

inverted_most_common_binary = "".join([str(s) for s in inverted_most_common])

epsilon_rate = int(inverted_most_common_binary, 2)

print(game_rate * epsilon_rate)

