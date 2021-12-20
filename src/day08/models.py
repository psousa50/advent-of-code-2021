from dataclasses import dataclass, field
from typing import List

@dataclass
class Entry:
  signal_patterns: List[int]
  output_values: List[int]

  def __repr__(self):
    return f'{self.signal_patterns} | {self.output_values}'

