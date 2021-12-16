from typing import List, Dict
from typing import List, Dict
from day04.models import Board

def read_board(lines, line_index):
  if line_index >= len(lines): return None

  rows = []
  for row_index in range(5):
    row = [int(n) for n in lines[line_index + row_index + 1].split()]
    rows.append(row)

  return Board(rows)
    
def read_boards(lines):
  rolled_numbers = [int(n) for n in lines[0].split(",")]
  boards: List[Board] = []
  line_index = 1
  while (board := read_board(lines, line_index)) != None:
    line_index += 6
    boards.append(board)

  return rolled_numbers, boards
