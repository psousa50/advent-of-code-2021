from src.day10.helpers import find_incorrect_closing
from src.global_helpers import read_input

closing_chars_score = {
  '(': 1,
  '[': 2,
  '{': 3,
  '<': 4,
}

def calc_score(opening_chars):
  score = 0
  for c in opening_chars:
    score = score * 5 + closing_chars_score[c]

  return score

def main():
  lines = read_input(10, 1)

  scores = []
  for line in lines:
    incorrect, open_stack = find_incorrect_closing(line)
    if incorrect == None: scores.append(calc_score(list(reversed(open_stack))))
  
  scores.sort()
  return scores[int(len(scores) / 2)]

print(main())
