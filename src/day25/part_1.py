from dataclasses import dataclass

from src.global_helpers import execute, read_input
from src.global_models import Point


@dataclass(frozen=True)
class Cocumber:
    type: str
    pos: Point

    def __repr__(self):
        return "{} {}".format(self.type, repr(self.pos))


@dataclass(frozen=True)
class Sea:
    cocumbers: list[Cocumber]
    width: int
    height: int

    @classmethod
    def from_new_cocumbers(cls, sea: "Sea", cocumbers: list[Cocumber]):
        return cls(cocumbers, sea.width, sea.height)

    def __repr__(self):
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                c = self.cocumber_at(Point(x, y))
                s += c.type if c is not None else "."
            s += "\n"
        return s

    def cocumber_at(self, pos: Point):
        cocumbers = [c for c in self.cocumbers if c.pos == pos]
        return next(iter(cocumbers), None)

    def is_empty(self, pos: Point):
        return self.cocumber_at(pos) is None

    def move_type(self, type: str, d: Point):
        moved_cocumbers: list[Cocumber] = []
        moved = False
        for c in self.cocumbers:
            new_x = (c.pos.x + d.x) % self.width
            new_y = (c.pos.y + d.y) % self.height
            new_pos = Point(new_x, new_y)
            if c.type == type and self.is_empty(new_pos):
                moved_cocumbers += [Cocumber(c.type, new_pos)]
                moved = True
            else:
                moved_cocumbers += [c]

        return moved, Sea.from_new_cocumbers(self, moved_cocumbers) if moved else self

    def move(self):
        moved_east, new_sea = self.move_type(">", Point(1, 0))
        moved_south, new_sea = new_sea.move_type("v", Point(0, 1))
        return moved_east or moved_south, new_sea


def main():
    lines = read_input(25, 1)

    cocumbers: list[Cocumber] = []
    for y, line in enumerate(lines):
        for x, d in enumerate(line):
            if d in [">", "v"]:
                cocumbers += [Cocumber(d, Point(x, y))]

    sea = Sea(cocumbers, len(lines[0]), len(lines))
    # print(sea)

    moved = True
    c = 0
    while moved:
        moved, sea = sea.move()
        c += 1
        # if (c % 10) == 0:
        print(c)
        # print(sea)
        # if c == 1:
        #     break

    return c


if __name__ == "__main__":
    execute(main)
