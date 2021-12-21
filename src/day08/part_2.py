
import itertools
from typing import List

from src.global_helpers import read_input
from src.day08.helpers import read_entries
from src.day08.models import Entry

def find(patterns, f):
  return next((p for p in patterns if f(p)), None)

def contains(p1, p2):
  return all(c in [c for c in p1] for c in p2)

def main():
  lines = read_input(8, 1)

  entries = read_entries(lines)

  values = []
  for entry in entries:

    signal_patterns = entry.signal_patterns

    digits = [""] * 10

    digits[1] = find(signal_patterns, lambda p: len(p) == 2)
    digits[4] = find(signal_patterns, lambda p: len(p) == 4)
    digits[7] = find(signal_patterns, lambda p: len(p) == 3)
    digits[8] = find(signal_patterns, lambda p: len(p) == 7)

    digits[6] = find(signal_patterns, lambda p: len(p) == 6 and not contains(p, digits[1]))
    digits[0] = find(signal_patterns, lambda p: len(p) == 6 and not contains(p, digits[4]) and p not in digits)
    digits[9] = find(signal_patterns, lambda p: len(p) == 6 and p not in digits)

    digits[5] = find(signal_patterns, lambda p: len(p) == 5 and contains(digits[6], p))
    digits[3] = find(signal_patterns, lambda p: len(p) == 5 and contains(digits[9], p) and p not in digits)
    digits[2] = find(signal_patterns, lambda p: len(p) == 5 and p not in digits)

    value = int("".join([str(digits.index(p)) for p in entry.output_values]))
    
    values.append(value)

  return sum(values)

print(main())
