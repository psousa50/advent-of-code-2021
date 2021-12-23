from collections import defaultdict

def read_template_and_insertions(lines):
  polymer_template = lines[0]

  pair_insertions = {}
  for line in lines[2:]:
    p = line.split("->")
    pair_insertions[p[0].strip()] =  p[1].strip()

  return polymer_template, pair_insertions


def calc_most_common_and_less_common(steps, polymer_template, pair_insertions):
  pair_count = defaultdict(int) 
  for count, _ in enumerate(polymer_template[0:-1]):
    pair = polymer_template[count:count+2]
    pair_count[pair] += 1  

  for _ in range(steps):
    new_pair_count = defaultdict(int)
    new_pair_count |= pair_count
    for p in pair_count.keys():
      count = pair_count[p]
      if count > 0:
        insertion = pair_insertions.get(p, None)
        if insertion != None: 
          new_pair_count[p] -= count
          new_pair_count[p[0] + insertion] += count
          new_pair_count[insertion + p[1]] += count

    pair_count = new_pair_count

  character_count = defaultdict(int) 
  for pair, count in pair_count.items():
    character_count[pair[0]] += count
  character_count[polymer_template[-1]] += 1

  sorted_character_count = dict(sorted(character_count.items(), key = lambda i: i[1]))
  values = list(sorted_character_count.values())
  
  return values[-1] - values[0]
  