import global_helpers
from day04.helpers import Board, read_board, read_boards

def main():
  lines = global_helpers.read_input(4, 1)

  rolled_numbers, boards = read_boards(lines)

  all_has_bingo = False
  for rolled_number in rolled_numbers:
    for board in boards:
      board.roll_number(rolled_number)
      all_has_bingo = all([b.has_bingo() for b in boards])
      if all_has_bingo: break
    if all_has_bingo: break
  
  unmarked_sum = sum(board.unmarked_numbers())

  return rolled_number * unmarked_sum

print(main())