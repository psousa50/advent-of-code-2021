from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Coordinate:
  row: int
  col: int

def five_zero_list():
    return [0] * 5

@dataclass
class Board:
  rows: List[int]
  numbers: Dict[int, Coordinate] = field(default_factory=dict)
  marked_row_counters : List[int] = field(default_factory=five_zero_list)
  marked_col_counters : List[int] = field(default_factory=five_zero_list)
  rolled_numbers : List[int] = field(default_factory=list)

  def __post_init__(self):
    self.add_numbers()

  def add_number(self, n, row_index, col_index):
    self.numbers[n] = Coordinate(row_index, col_index)

  def add_numbers(self):
    for row_index, row in enumerate(self.rows):
      for col_index, _ in enumerate(row):
        self.add_number(self.rows[row_index][col_index], row_index, col_index)

  def roll_number(self, n):
    coord = self.numbers.get(n)
    if coord != None:
      self.marked_row_counters[coord.row] += 1
      self.marked_col_counters[coord.col] += 1
    self.rolled_numbers.append(n)

  def has_bingo(self):
    return len([r for r in self.marked_row_counters if r == 5]) > 0 or len([c for c in self.marked_col_counters if c == 5]) > 0

  def unmarked_numbers(self):
    all_numbers = []
    for row in self.rows:
      all_numbers += row
    return set(all_numbers) - set(self.rolled_numbers)


