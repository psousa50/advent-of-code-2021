from dataclasses import dataclass, field

from src.global_helpers import execute, read_input


@dataclass()
class Sea:
    cucumbers: list[list[str]]
    width: int = field(default=0)
    height: int = field(default=0)

    def __post_init__(self):
        self.width = len(self.cucumbers[0])
        self.height = len(self.cucumbers)

    def __repr__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += self.cucumbers[y][x]
            s += "\n"
        return s

    def move(self):
        moved = False
        for y in range(self.height):
            to_move = []
            for x in range(self.width):
                if self.cucumbers[y][x] == ">" and self.cucumbers[y][(x + 1) % self.width] == ".":
                    to_move += [x]
            for x in to_move:
                self.cucumbers[y][x] = "."
                self.cucumbers[y][(x + 1) % self.width] = ">"
            moved = moved or len(to_move) > 0

        for x in range(self.width):
            to_move = []
            for y in range(self.height):
                if self.cucumbers[y][x] == "v" and self.cucumbers[(y + 1) % self.height][x] == ".":
                    to_move += [y]
            for y in to_move:
                self.cucumbers[y][x] = "."
                self.cucumbers[(y + 1) % self.height][x] = "v"
            moved = moved or len(to_move) > 0

        return moved


def main():
    lines = read_input(25, 1)

    sea = Sea([[c for c in line] for line in lines])

    done = False
    c = 0
    while not done:
        moved = sea.move()
        c += 1
        # if (c % 10) == 0:
        # print(c)
        # print(sea)
        # if c == 10:
        #     break
        done = not moved

    return c


if __name__ == "__main__":
    execute(main)
