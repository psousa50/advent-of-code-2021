import helpers

lines = helpers.read_input(3, 1)

values = [line for line in lines]

binary_length = len(values[0])
number_of_binaries = len(values)

ones_counter = [0] * binary_length

for binary in values:
  for bit_index, bit in enumerate(binary):
    if int(bit) == 1: ones_counter[bit_index] += 1

most_common = [1 if c > number_of_binaries - c else 0 for c in ones_counter]

most_common_binary = "".join([str(s) for s in most_common])

game_rate = int(most_common_binary, 2)

inverted_most_common = [1 if c == 0 else 0 for c in most_common]

inverted_most_common_binary = "".join([str(s) for s in inverted_most_common])

epsilon_rate = int(inverted_most_common_binary, 2)

print(game_rate * epsilon_rate)
