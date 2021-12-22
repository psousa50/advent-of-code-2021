from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
  cave: str
  parent: 'Node' = None
  max_visits_for_small_cave: int = 0
  visits_for_small_cave: int = 0
  path: List[str] = field(default_factory=list)

  def __repr__(self):
    return f'{self.path}'

  def __post_init__(self):
    path = [] if self.parent == None else self.parent.path
    self.path = path + [self.cave]
    if self.parent != None:
      self.max_visits_for_small_cave = self.parent.max_visits_for_small_cave
      self.visits_for_small_cave = self.parent.visits_for_small_cave


