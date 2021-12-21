from src.global_helpers import read_input
from src.day03.helpers import most_common_bit

def main():
  lines = read_input(3, 1)

  oxygen_bytes = list(lines)

  bit_index = 0
  while len(oxygen_bytes) > 1:
    most_common = most_common_bit(oxygen_bytes, bit_index)
    oxygen_bytes = [byte for byte in oxygen_bytes if byte[bit_index] == str(most_common)]
    bit_index += 1


  co2_bytes = list(lines)

  bit_index = 0
  while len(co2_bytes) > 1:
    most_common = most_common_bit(co2_bytes, bit_index)
    co2_bytes = [byte for byte in co2_bytes if  byte[bit_index] == str(1 - most_common)]
    bit_index += 1

  return int(oxygen_bytes[0], 2) * int(co2_bytes[0], 2)

print(main())
