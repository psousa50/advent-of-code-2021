from dataclasses import dataclass, field
from typing import List
import global_helpers


@dataclass
class Entry:
  signal_patterns: List[int]
  output_values: List[int]

  def __repr__(self):
    return f'{self.signal_patterns} | {self.output_values}'

def main():
  lines = global_helpers.read_input(8, 1)

  entries: List[Entry] = []

  for line in lines:
    [signal_patterns_part, output_values_part] = line.split("|")
    entries.append(Entry(signal_patterns_part.split(), output_values_part.split()))
  
  output_values: List[int] = []
  for entry in entries:
    output_values += entry.output_values

  unique = [u for u in output_values if len(u) in [2, 3,4, 7]]
  
  return len(unique)

print(main())