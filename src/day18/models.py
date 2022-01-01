from dataclasses import dataclass

@dataclass
class Pair:
  left: 'Element' = None
  right: 'Element' = None

Element = Pair | int

def __repr__(self):
    return f'[{self.left}, {self.right}]'

def is_pair(pair):
  return isinstance(pair, Pair)

