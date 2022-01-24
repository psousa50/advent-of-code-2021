from dataclasses import dataclass, field
from pydoc import plain
from turtle import pos
from zoneinfo import available_timezones

from click import core

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
    coord: int

    def __repr__(self):
        return "{}{}".format(self.place, self.coord)

    def __str__(self):
        return f"({self.place},{self.coord})"

    def row(self):
        return 0 if self.place == "H" else self.coord + 1

    def col(self):
        return self.coord if self.place == "H" else rooms[self.place].col


@dataclass(frozen=True)
class Amphipod:
    name: str
    type: str
    pos: Position

    def __repr__(self):
        return "{}:{!r}".format(self.name, self.pos)

    def __str__(self):
        return f"{self.name} -> {self.pos}"

    def at_correct_room(self):
        return self.pos.place == self.type

    def state(self):
        return f"{self.type}{self.pos.place}{self.pos.coord}"


@dataclass(frozen=True)
class Move:
    amphipod: Amphipod
    pos: Position

    def __repr__(self):
        return "{!r}->{!r}".format(self.amphipod, self.pos)

    def __str__(self):
        return f"({self.amphipod.name},{self.pos})"

    def __abs__(self):
        length = 0
        p1 = self.amphipod.pos
        p2 = self.pos
        hallway = abs(p1.col() - p2.col()) + 1
        place1 = "H" if p1.place == "H" else "R"
        place2 = "H" if p2.place == "H" else "R"
        match f'{place1}{place2}':
            case 'HH':
                length += hallway
            case "HR":
                length += hallway
                length += p2.coord + 1
            case "RH":
                length += p1.coord + 1
                length += hallway
            case "RR":
                if p1.place == p2.place:
                    length += abs(p1.coord - p2.coord) + 1
                else:
                    length += p1.coord + 1
                    length += hallway
                    length += p2.coord + 1

        return length

    def cost(self):
        return (abs(self) - 1) * rooms[self.amphipod.type].cost


@dataclass(frozen=True)
class State:
    amphipods: list[Amphipod]
    number_of_rows: int
    cost: int = field(default=0)

    @classmethod
    def new(cls, amphipods, number_of_rows, cost):
        return State(list(amphipods), number_of_rows, cost)

    def available_moves_to_enter_room(self, amphipod: Amphipod):
        moves: list[Move] = []
        others_in_room = [a for a in self.amphipods if a.pos.place == amphipod.type] 
        room_pos = min([a.pos.coord for a in others_in_room], default=self.number_of_rows) - 1
        moves += [Move(amphipod, Position(amphipod.type, r)) for r in range(0, room_pos + 1)]
        
        return moves

    def available_moves_inside_room(self, amphipod: Amphipod):
        moves: list[Move] = []
        top_coord = max([a.pos.coord for a in self.amphipods if a.pos.place == amphipod.type and a.pos.coord < amphipod.pos.coord], default=-1)
        bottom_coord = min([a.pos.coord for a in self.amphipods if a.pos.place == amphipod.type and a.pos.coord > amphipod.pos.coord], default=self.number_of_rows)
        moves += [Move(amphipod, Position(amphipod.type, r)) for r in range(top_coord + 1, amphipod.pos.coord)]
        moves += [Move(amphipod, Position(amphipod.type, r)) for r in range(amphipod.pos.coord + 1, bottom_coord)]
        
        return moves

    def available_moves_in_hallway(self, amphipod: Amphipod):
        amphipod_col = rooms[amphipod.pos.place].col
        left_coord = max([a.pos.coord for a in self.amphipods if a.pos.place == "H" and a.pos.coord < amphipod_col], default=-1) + 1
        right_coord = min([a.pos.coord for a in self.amphipods if a.pos.place == "H" and a.pos.coord > amphipod_col], default=11) - 1
        moves = [Move(amphipod, Position("H", c)) for c in [0, 1, 3, 5, 7, 9, 10] if c >= left_coord and c <= right_coord]
        
        return moves

    def blocked_in_hallway(self, amphipod: Amphipod):
        p1 = amphipod.pos.coord
        p2 = rooms[amphipod.type].col
        if p1 > p2: p1, p2 = (p2, p1)
        blocking = [a for a in self.amphipods if a.pos.place == "H" and p1 < a.pos.coord < p2]
        return blocking 
    
    def blocked_in_room(self, amphipod: Amphipod):
        blocking = [a for a in self.amphipods if a.pos.place == amphipod.pos.place and a.pos.coord < amphipod.pos.coord]
        return blocking 
    
    def is_blocking_other(self, amphipod: Amphipod):
        return [a for a in self.amphipods if a.pos.place == amphipod.pos.place and a.type != amphipod.type and a.pos.coord > amphipod.pos.coord]

    def available_moves(self, amphipod: Amphipod):
        moves: list[Move] = []
        if amphipod.pos.place == "H":
            if not self.blocked_in_hallway(amphipod):
                moves += self.available_moves_to_enter_room(amphipod)
        else:
            if amphipod.at_correct_room():
                if amphipod.pos.coord < self.number_of_rows - 1:
                    moves += self.available_moves_inside_room(amphipod)
                    if self.is_blocking_other(amphipod):
                        moves += self.available_moves_in_hallway(amphipod)
            else:
                if not self.blocked_in_room(amphipod):
                    moves_in_hallway = self.available_moves_in_hallway(amphipod)
                    moves += moves_in_hallway
                    if moves_in_hallway and min([m.pos.coord for m in moves_in_hallway]) <= rooms[amphipod.type].col <= max([m.pos.coord for m in moves_in_hallway]):
                        moves += self.available_moves_to_enter_room(amphipod)
        
        # wrong = [m for m in moves if any([a for a in self.amphipods if a.pos == m.pos])]
        # assert not wrong
        # if aa:
        #     breakpoint()

        return moves

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
        burrow = [
            "#############",
            "#...........#",
            "###.#.#.#.###",
        ]

        for _ in range(0, self.number_of_rows - 1):
            burrow.append("  #.#.#.#.#  ")

        burrow.append("  #########")


        s = [list(l) for l in burrow]

        for a in self.amphipods:
            s[a.pos.row() + 1][a.pos.col() + 1] = a.type

        return "\n".join(["".join(ss) for ss in s])
