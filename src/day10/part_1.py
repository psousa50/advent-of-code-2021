from src.day10.helpers import find_incorrect_closing
from src.global_helpers import read_input

incorrect_chars_score = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

def main():
  lines = read_input(10, 1)

  score = 0
  for line in lines:
    incorrect, _ = find_incorrect_closing(line)
    if incorrect != None: score += incorrect_chars_score[incorrect]
  
  return score

print(main())
