from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
  cave: str
  parent: 'Node' = None
  path: List[str] = field(default_factory=list)

  def __repr__(self):
    return f'{self.path}'

  def __post_init__(self):
    self.path = [] if self.parent == None else self.parent.path + [self.cave]


