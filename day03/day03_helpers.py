def most_common_bit(bytes, bit):
  ones_count = 0
  for byte in bytes:
    if byte[bit] == "1": ones_count += 1
  return 1 if ones_count >= len(bytes) - ones_count else 0

