import math
from collections import namedtuple
from dataclasses import dataclass
from typing import List

from src.global_helpers import read_input

Element = namedtuple('Element', 'literal pair')

@dataclass
class Pair:
  left: Element = None
  right: Element = None

  def __repr__(self):
    return f'[{self.left}, {self.right}]'


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

def explode(pair: Pair, level):
  one_found = False
  if is_pair(pair):
    if level >= 4: 
      return pair, 'nested', True
    else:

      left_pair, pair_type, one_found = explode(pair.left, level + 1)
      if left_pair != None:
        match (pair_type):
          case 'nested':
            pair.left = 0
            pair.right = add_to_left(pair.right, left_pair.right)
            return left_pair, 'left', True
          case 'left':
            return left_pair, 'left', True
          case 'right':
            pair.right = add_to_left(pair.right, left_pair.right)
            return None, None, True

      else:
        if not one_found:
          right_pair, pair_type, one_found = explode(pair.right, level + 1)
          if right_pair != None:
            match (pair_type):
              case 'nested': 
                pair.right = 0
                pair.left = add_to_right(pair.left, right_pair.left)
                return right_pair, 'right', True
              case 'right':
                return right_pair, 'right', True
              case 'left':
                pair.left = add_to_right(pair.left, right_pair.left)
                return None, None, True

  return None, None, one_found

def reduce_pair(pair: Pair):
  done = False
  while not done:
    _, _, exploded = explode(pair, 0)
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

def main():

  lines = read_input(18, 1)

  pairs = [parse_pair(line) for line in lines]

  pairs_sum = pairs[0]
  for pair in pairs[1:]:
    pairs_sum = reduce_pair(add(pairs_sum, pair))
  
  return magnitude(pairs_sum)

print(main())
