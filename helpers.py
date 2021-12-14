def read_input(day, sample=False):
    filename = "input.txt" if not sample else "sample.txt"
    filepath = f'day{day:02d}/inputs/{filename}'
    with open(filepath, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines
