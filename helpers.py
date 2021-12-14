def read_input(day, part, sample=False):
    filename = "input" if not sample else "sample"
    filepath = f'day{day:02d}/inputs/{filename}_{part:02d}.txt'
    with open(filepath, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines
