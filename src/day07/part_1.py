import collections
from typing import List
import global_helpers

def distance_sum(positions, position):
  return sum([abs(p - position) for p in positions])

def main():
  lines = global_helpers.read_input(7, 1)

  positions: List[int] = [int(n) for n in lines[0].split(",")]
  positions.sort()

  last_fuel_cost = distance_sum(positions, positions[0])
  for p in range(min(positions), max(positions)):
    fuel_cost = distance_sum(positions, p)
    if fuel_cost > last_fuel_cost: break
    last_fuel_cost = fuel_cost

  return last_fuel_cost 

print(main())


