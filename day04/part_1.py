from typing import List, Dict
from dataclasses import dataclass, field
import helpers

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


def read_board(lines, line_index):
  if line_index >= len(lines): return None

  rows = []
  for row_index in range(5):
    row = [int(n) for n in lines[line_index + row_index + 1].split()]
    rows.append(row)

  return Board(rows)
    

def main():
  lines = helpers.read_input(4, 1)

  rolled_numbers = [int(n) for n in lines[0].split(",")]
  boards: List[Board] = []
  line_index = 1
  while (board := read_board(lines, line_index)) != None:
    line_index += 6
    boards.append(board)

  for rolled_number in rolled_numbers:
    for board in boards:
      board.roll_number(rolled_number)
      if board.has_bingo(): break
    if board.has_bingo(): break
  
  unmarked_sum = sum(board.unmarked_numbers())

  return rolled_number * unmarked_sum

print(main())