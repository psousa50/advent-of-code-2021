import math
from typing import List

from src.day18.models import Pair

def is_pair(element):
  return isinstance(element, Pair)

def parse_literal_at_pos(line: List[str], pos):
  n = ""
  for i, c in enumerate(line[pos + 1:]):
    if c.isdigit(): 
      n += c 
    else: 
      break
  return int(n), pos + i + 1

def parse_element_at_pos(line: List[str], pos):
  return parse_pair_at_pos(line, pos + 1) if line[pos + 1] == "[" else parse_literal_at_pos(line, pos)

def parse_pair_at_pos(line, pos):
  left, pos = parse_element_at_pos(line, pos)
  right, pos = parse_element_at_pos(line, pos)

  return Pair(left, right), pos + 1

def parse_pair(line):
  pair, pos =  parse_pair_at_pos(line, 0)
  return pair

def add_to_left(pair: Pair, to_add: int):
  if is_pair(pair):    
    return Pair(add_to_left(pair.left, to_add), pair.right)
  else:
    return pair + to_add

def add_to_right(pair: Pair, to_add: int):
  if is_pair(pair):
    return Pair(pair.left, add_to_right(pair.right, to_add))
  else:
    return pair + to_add

def split(pair: Pair):
  if (is_pair(pair)):
    splitted, one_found = split(pair.left)
    if one_found:
      return Pair(splitted, pair.right), True
    else:
      splitted, one_found = split(pair.right)
      if one_found: 
        return Pair(pair.left, splitted), True
      else:
        return pair, False
  else:
    return (Pair(int(math.floor(pair / 2)), int(math.ceil(pair / 2))), True) if pair >= 10 else (pair, False)

def try_explode(pair: Pair, level):
  one_found = False
  if is_pair(pair):
    if level >= 4: 
      return pair, True, pair, 'nested'
    else:

      left, one_found, left_pair, pair_type = try_explode(pair.left, level + 1)
      pair = Pair(left, pair.right)
      if left_pair != None:
        match (pair_type):
          case 'nested':
            return Pair(0, add_to_left(pair.right, left_pair.right)), True, left_pair, 'left'
          case 'left':
            return pair, True, left_pair, 'left'
          case 'right':
            return Pair(pair.left, add_to_left(pair.right, left_pair.right)), True, None, None

      else:
        if not one_found:
          right, one_found, right_pair, pair_type = try_explode(pair.right, level + 1)
          pair = Pair(pair.left, right)
          if right_pair != None:
            match (pair_type):
              case 'nested': 
                return Pair(add_to_right(pair.left, right_pair.left), 0), True, right_pair, 'right'
              case 'right':
                return pair, True, right_pair, 'right'
              case 'left':
                return Pair(add_to_right(pair.left, right_pair.left), pair.right), True, None, None

  return pair, one_found, None, None

def explode(pair: Pair):
  pair, exploded, _, _ = try_explode(pair, 0)
  return pair, exploded

def reduce_pair(pair: Pair):
  done = False
  while not done:
    pair, exploded  = explode(pair)
    if not exploded:
      pair, splitted = split(pair)
    done = not exploded and not splitted

  return pair

def add(p1: Pair, p2: Pair):
  return Pair(p1, p2)

def magnitude(pair: Pair):
  if is_pair(pair):
    return 3 * magnitude(pair.left) + 2 * magnitude(pair.right)
  else:
    return pair

