import collections
import global_helpers

def main():
  lines = global_helpers.read_input(6, 1)

  lantern_fish_timers = [int(n) for n in lines[0].split(",")]

  fish_classes = collections.defaultdict(int)

  for f in lantern_fish_timers:
    fish_classes[f] += 1

  for day in range(80):
    next_fish_classes = collections.defaultdict(int)
    for f, count in fish_classes.items():
      if f == 0:
        next_fish_classes[6] += count
        next_fish_classes[8] += count
      else:
        next_fish_classes[f-1] += count
    fish_classes = next_fish_classes

  return sum(fish_classes.values())


print(main())