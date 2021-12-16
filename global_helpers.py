import math

def read_input(day, part, sample=False):
    filename = "input" if not sample else "sample"
    filepath = f'day{day:02d}/inputs/{filename}_{part:02d}.txt'
    with open(filepath, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

sign = lambda x: 0 if x == 0 else int(math.copysign(1, int(x)))

