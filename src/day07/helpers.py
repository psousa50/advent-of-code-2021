
def distance_sum(positions, position, calc_cost):
  return sum([calc_cost(p, position) for p in positions])


def calc_minimum_fuel_cost(positions, calc_cost):
  sorted_positions = list(positions)
  sorted_positions.sort()

  last_fuel_cost = distance_sum(positions, positions[0], calc_cost)
  for p in range(min(positions), max(positions)):
    fuel_cost = distance_sum(positions, p, calc_cost)
    if fuel_cost > last_fuel_cost: break
    last_fuel_cost = fuel_cost

  return last_fuel_cost 
