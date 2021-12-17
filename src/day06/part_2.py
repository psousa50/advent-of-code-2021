from src.day06.helpers import generations
import global_helpers

def main():
  lines = global_helpers.read_input(6, 1)

  lantern_fish_timers = [int(n) for n in lines[0].split(",")]

  next_lantern_fish_timers = generations(256, lantern_fish_timers)

  return sum(next_lantern_fish_timers.values())

print(main())