from src.day23.models import Amphipod, Position, State, AStar, rooms


def read_amphipods(lines: list[str], number_of_rows):
    amphipods: list[Amphipod] = []
    for row in range(2, number_of_rows + 2):
        r = 0
        for col in range(3, 10, 2):
            type = lines[row][col]
            room = rooms[type]
            room_name = [k for k in rooms.keys() if rooms[k].col == col - 1][0]
            amphipods.append(Amphipod(f"{type}{room.index}", type, Position(room_name, row - 2)))
            room.index += 1
            r += 1

    return amphipods


def solve(amphipods: list[Amphipod], debug: bool = False):
    number_of_rows = 1 + max([a.pos.coord for a in amphipods if a.type != "H"])

    a_star = AStar(State(amphipods, number_of_rows), debug=debug)

    minimum_cost = a_star.solve()

    return minimum_cost
