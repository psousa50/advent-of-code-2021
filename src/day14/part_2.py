from src.day14.helpers import calc_most_common_and_less_common, read_template_and_insertions
from src.global_helpers import read_input


def main():
  lines = read_input(14, 1)

  polymer_template, pair_insertions = read_template_and_insertions(lines)
  
  return calc_most_common_and_less_common(40, polymer_template, pair_insertions)

print(main())
