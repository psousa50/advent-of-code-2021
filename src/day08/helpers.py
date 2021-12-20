from typing import List
from src.day08.models import Entry

def sort_chars(s):
  a = [c for c in s]
  a.sort()
  return "".join(a)


def sort_digit(segments):
  key_sort_order = [2, 3, 4, 7, 5, 6]
  return key_sort_order.index(len(segments))

def read_entries(lines):
  entries: List[Entry] = []

  for line in lines:
    [signal_patterns_part, output_values_part] = line.split("|")
    signal_patterns = [sort_chars(s) for s in signal_patterns_part.split()]
    output_values = [sort_chars(s) for s in output_values_part.split()]
    signal_patterns.sort(key = len)
    entries.append(Entry(signal_patterns, output_values))

  return entries
