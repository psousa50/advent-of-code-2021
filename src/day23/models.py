import heapq
from dataclasses import dataclass, field
from typing import Optional


@dataclass()
class Room:
    col: int
    cost_factor: int

rooms: dict[str, Room] = {
    "A": Room(2, 1),
    "B": Room(4, 10),
    "C": Room(6, 100),
    "D": Room(8, 1000),
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

    def length(self):
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
        return (self.length() - 1) * rooms[self.amphipod.type].cost_factor


@dataclass(frozen=True)
class State:
    amphipods: list[Amphipod]
    number_of_rows: int
    cost: int = field(default=0)
    parent: Optional['State'] = field(default=None)
    h_cost: int = field(default=0)
    id: str = field(default="")

    def __post_init__(self):
        state_id = "".join([a.state() for a in sorted(self.amphipods, key=lambda a: a.state())])
        object.__setattr__(self, 'h_cost', self.calc_h_cost())
        object.__setattr__(self, 'id', state_id)

    def calc_h_cost(self):
        cost = 0
        for a1 in self.amphipods:
            if a1.pos.place == "H":
                m = Move(a1, Position(a1.type, 0))
                cost += (m.length() - 1) * rooms[a1.type].cost_factor
                for a2 in self.amphipods:
                    if a2.pos.place == a1.type and a2.type != a1.type:
                        cost += (a2.pos.coord + 2) * rooms[a2.type].cost_factor
                
            if a1.pos.place != "H" and a1.pos.place != a1.type:
                for a2 in self.amphipods:
                    if a2.pos.place == a1.pos.place and a2.pos.coord < a1.pos.coord:
                        cost += (a2.pos.coord + 2) * rooms[a2.type].cost_factor

        return cost

    def __lt__(self, other):
        c1 = self.cost + self.h_cost
        c2 = other.cost + other.h_cost
        return c1 < c2 if c1 != c2 else id(self) < id(other)

    @classmethod
    def new(cls, amphipods, number_of_rows, cost, parent):
        return State(list(amphipods), number_of_rows, cost, parent)

    def available_moves_to_enter_room(self, amphipod: Amphipod):
        moves: list[Move] = []
        others_in_room = [a for a in self.amphipods if a.pos.place == amphipod.type] 
        if all([a.type == amphipod.type for a in others_in_room]):
            room_pos = min([a.pos.coord for a in others_in_room], default=self.number_of_rows) - 1
            moves.append(Move(amphipod, Position(amphipod.type, room_pos)))
        
        return moves

    def available_moves_inside_room(self, amphipod: Amphipod):
        moves: list[Move] = []
        bottom_coord = min([a.pos.coord for a in self.amphipods if a.pos.place == amphipod.type and a.pos.coord > amphipod.pos.coord], default=self.number_of_rows) - 1
        if bottom_coord> amphipod.pos.coord:
            moves.append (Move(amphipod, Position(amphipod.type, bottom_coord)))
        
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
                    if self.is_blocking_other(amphipod) and not self.blocked_in_room(amphipod):
                        moves += self.available_moves_in_hallway(amphipod)
            else:
                if not self.blocked_in_room(amphipod):
                    moves_in_room: list[Move] = []
                    p1 = amphipod.pos.col()
                    p2 = rooms[amphipod.type].col
                    if p1 > p2: p1, p2 = (p2, p1)
                    blocking = [a for a in self.amphipods if a.pos.place == "H" and p1 <= a.pos.coord <= p2]
                    if not blocking:
                        moves_in_room += self.available_moves_to_enter_room(amphipod)

                    if moves_in_room:
                        moves = moves_in_room
                    else:
                        moves = self.available_moves_in_hallway(amphipod)
        
        return moves

    def apply_move(self, move: Move):
        new_amphipods = [
            Amphipod(move.amphipod.name, move.amphipod.type, move.pos) if a == move.amphipod else a
            for a in self.amphipods
        ]
        return State.new(new_amphipods, self.number_of_rows, self.cost + move.cost(), self)

    def next_states(self):
        return [self.apply_move(move) for amphipod in self.amphipods for move in self.available_moves(amphipod) ]

    def is_final(self):
        return all(a.pos.place == a.type for a in self.amphipods)

    def __str__(self):
        burrow = [
            "#############",
            "#...........#",
        ]

        for _ in range(0, self.number_of_rows):
            burrow.append("  #.#.#.#.#  ")

        burrow.append(f"  #########    {self.cost } + {self.h_cost} = {self.cost + self.h_cost}")

        s = [list(l) for l in burrow]

        for a in self.amphipods:
            s[a.pos.row() + 1][a.pos.col() + 1] = a.type

        return "\n".join(["".join(ss) for ss in s])


@dataclass(frozen=True)
class AStar:
    initial_state: State
    debug: bool = False
    ordered_states: list[State] = field(init=False, default_factory=list)
    states: dict[str, State] = field(init=False, default_factory=dict)
    open_nodes: set[str] = field(init=False, default_factory=set)
    closed_nodes: set[str] = field(init=False, default_factory=set)

    def __post_init__(self):
        self.add_state(self.initial_state)

    def add_state(self, state: State):
        heapq.heappush(self.ordered_states, state)
        self.states[state.id] = state
        self.open_nodes.add(state.id)

    def build_path(self, s: State):
        if s.parent is None:
            return [s]
        else:
            return self.build_path(s.parent) + [s]
        

    def solve(self):
        c = 0
        success_state: Optional[State] = None
        while self.ordered_states and success_state is None:
            c += 1
            if (c % 10000) == 0:
                print(c)
            state = heapq.heappop(self.ordered_states)
            self.closed_nodes.add(state.id)
            if self.debug:
                print(c)
                print(state)
            if state.is_final():
                success_state = state
            else:
                for child_state in state.next_states():
                    if not child_state.id in self.closed_nodes and (not child_state.id in self.open_nodes or child_state.cost < self.states[child_state.id].cost):
                            if self.debug:
                                print(child_state)
                            self.add_state(child_state)


        return self.build_path(success_state) if success_state is not None else []
