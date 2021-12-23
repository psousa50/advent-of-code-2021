from typing import Callable, Dict
from src.global_helpers import read_input

def main():
  lines = read_input(14, 1)

  polymer_template = lines[0]

  pair_insertions = {}
  for line in lines[2:]:
    p = line.split("->")
    pair_insertions[p[0].strip()] =  p[1].strip()

  polymer = polymer_template
  for _ in range(10):
    new_polymer = polymer[0]
    for i, _ in enumerate(polymer[0:-1]):
      pair = polymer[i:i+2]
      insertion = pair_insertions.get(pair, None)
      if insertion != None: new_polymer += insertion
      new_polymer += pair[1]
    polymer = new_polymer

  character_count: Dict[str, int] = {}
  for c in polymer:
    character_count[c] = character_count.get(c, 0) + 1

  sorted_character_count = dict(sorted(character_count.items(), key = lambda i: i[1]))
  values = list(sorted_character_count.values())
  return values[-1] - values[0]

print(main())
