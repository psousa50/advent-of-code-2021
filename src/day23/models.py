from dataclasses import dataclass, field
from turtle import pos
from zoneinfo import available_timezones

@dataclass()
class Room:
    col: int
    cost: int
    index: int

rooms: dict[str, Room] = {
    "A": Room(2, 1, 1),
    "B": Room(4, 10, 1),
    "C": Room(6, 100, 1),
    "D": Room(8, 1000, 1),
}


@dataclass(frozen=True)
class Position:
    place: str
    pos: int

    def __str__(self):
        return f"({self.place},{self.pos})"

    def row(self):
        return 0 if self.place == "H" else self.pos + 1

    def col(self):
        return self.pos if self.place == "H" else rooms[self.place].col


@dataclass(frozen=True)
class Amphipod:
    name: str
    type: str
    pos: Position

    def __str__(self):
        return f"{self.name} -> {self.pos}"

    def state(self):
        return f"{self.type}{self.pos.place}{self.pos.pos}"


@dataclass(frozen=True)
class Move:
    amphipod: Amphipod
    pos: Position

    def __str__(self):
        return f"({self.amphipod.name},{self.pos})"

    def path(self):
        p1 = self.amphipod.pos
        p2 = self.pos            
        step = 1 if p1.col() <= p2.col() else -1
        hallway = [Position("H", c) for c in range(p1.col(), p2.col() + step, step)]
        p1_room_positions = [Position(p1.place, p) for p in range(p1.pos - 1, -1, -1)]
        p2_room_positions = [Position(p2.place, p) for p in range(0, p2.pos + 1)]
        positions: list[Position] = []
        place1 = "H" if p1.place == "H" else "R"
        place2 = "H" if p2.place == "H" else "R"
        match f'{place1}{place2}':
            case 'HH':
                positions += hallway[1:]
            case "HR":
                positions += hallway[1:]
                positions += p2_room_positions
            case "RH":
                positions += p1_room_positions
                positions += hallway
            case "RR":
                if p1.place == p2.place:
                    if p1.pos != p2.pos:
                        positions.append(p2)
                else:
                    positions += p1_room_positions
                    positions += hallway
                    positions += p2_room_positions

        return positions

    def cost(self):
        return len(self.path()) * rooms[self.amphipod.type].cost


@dataclass(frozen=True)
class State:
    amphipods: list[Amphipod]
    number_of_rows: int
    cost: int = field(default=0)

    @classmethod
    def new(cls, amphipods, number_of_rows, cost):
        return State(list(amphipods), number_of_rows, cost)

    def is_empty(self, p: Position):
        return len([a for a in self.amphipods if a.pos == p]) == 0

    def possible_positions(self, amphipod: Amphipod):
        p = amphipod.pos
        positions = [Position(amphipod.type, p) for p in range(0, self.number_of_rows)]
        if p.place != "H":
            positions += [Position("H", p) for p in [0, 1, 3, 5, 7, 9, 10]]
        
        return positions

    def available_moves(self, amphipod: Amphipod):
        if amphipod.pos.place == amphipod.type and amphipod.pos.pos == 1:
            return []

        positions = self.possible_positions(amphipod)
        moves = [Move(amphipod, p) for p in positions if self.is_empty(p)]

        return [move for move in moves if all(self.is_empty(p) for p in move.path())]

    def apply_move(self, move: Move):
        new_amphipods = [
            Amphipod(move.amphipod.name, move.amphipod.type, move.pos) if a == move.amphipod else a
            for a in self.amphipods
        ]
        return State.new(new_amphipods, self.number_of_rows, self.cost + move.cost())

    def next_states(self):
        return [self.apply_move(move) for amphipod in self.amphipods for move in self.available_moves(amphipod) ]

    def is_final(self):
        return all(a.pos.place == a.type for a in self.amphipods)

    def id(self):
        return "".join([a.state() for a in sorted(self.amphipods, key=lambda a: a.state())])

    def __lt__(self, other):
        return self.cost < other.cost if self.cost != other.cost else id(self) < id(other)

    def __str__(self):
        board = [
            "#############",
            "#...........#",
            "###.#.#.#.###",
            "  #.#.#.#.#",
            "  #########"
        ]

        s = [list(l) for l in board]

        for a in self.amphipods:
            s[a.pos.row() + 1][a.pos.col() + 1] = a.type

        return "\n".join(["".join(ss) for ss in s])
