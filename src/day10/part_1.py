from src.global_helpers import read_input

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

closing_chars_score = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

def find_incorrect_closing(line: str):
  open_stack = []
  for c in line:
    if c in opening_chars:
      open_stack.append(c)
    else:
      opening_char = open_stack.pop()
      if opening_chars.index(opening_char) != closing_chars.index(c): return c

  return None

def main():
  lines = read_input(10, 1)

  incorrect_chars = []
  for line in lines:
    incorrect = find_incorrect_closing(line)
    if incorrect != None: incorrect_chars.append(incorrect)
  
  return sum([closing_chars_score[c] for c in incorrect_chars])

print(main())