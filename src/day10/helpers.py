opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']

def find_incorrect_closing(line: str):
  open_stack = []
  for c in line:
    if c in opening_chars:
      open_stack.append(c)
    else:
      opening_char = open_stack.pop()
      if opening_chars.index(opening_char) != closing_chars.index(c): return c, open_stack

  return None, open_stack

