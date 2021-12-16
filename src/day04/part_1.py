import global_helpers
from typing import List, Dict
from src.day04.helpers import read_boards

def main():
  lines = global_helpers.read_input(4, 1)

  rolled_numbers, boards = read_boards(lines)

  has_bingo = False
  for rolled_number in rolled_numbers:
    for board in boards:
      board.roll_number(rolled_number)
      has_bingo = board.has_bingo()
      if has_bingo: break
    if has_bingo: break
  
  unmarked_sum = sum(board.unmarked_numbers())

  return rolled_number * unmarked_sum

print(main())