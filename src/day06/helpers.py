import collections

def generations(days, lantern_fish_timers):

  fish_classes = collections.defaultdict(int)

  for f in lantern_fish_timers:
    fish_classes[f] += 1

  for _ in range(days):
    next_fish_classes = collections.defaultdict(int)
    for f, count in fish_classes.items():
      if f == 0:
        next_fish_classes[6] += count
        next_fish_classes[8] += count
      else:
        next_fish_classes[f-1] += count
    fish_classes = next_fish_classes

  return fish_classes
