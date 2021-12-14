import helpers
from day03.helpers import most_common_bit

def most_common_bit(bytes, bit):
  ones_count = 0
  for byte in bytes:
    if byte[bit] == "1": ones_count += 1
  return 1 if ones_count >= len(bytes) - ones_count else 0

def main():
  bytes = helpers.read_input(3, 1)

  binary_length = len(bytes[0])

  most_common = [most_common_bit(bytes, bit_index) for bit_index in range(binary_length)]

  most_common_binary = "".join([str(s) for s in most_common])

  game_rate = int(most_common_binary, 2)

  inverted_most_common = [1 if c == 0 else 0 for c in most_common]

  inverted_most_common_binary = "".join([str(s) for s in inverted_most_common])

  epsilon_rate = int(inverted_most_common_binary, 2)

  return game_rate * epsilon_rate

print(main())

