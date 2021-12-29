from collections import namedtuple
from dataclasses import dataclass

Element = namedtuple('Element', 'literal pair')

@dataclass(frozen=True)
class Pair:
  left: Element = None
  right: Element = None

  def __repr__(self):
    return f'[{self.left}, {self.right}]'

