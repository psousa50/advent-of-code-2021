import heapq

from src.day23.models import Amphipod, Position, State, rooms


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


def solve(amphipods: list[Amphipod]):
    number_of_rows = 1 + max([a.pos.pos for a in amphipods if a.type != "H"])
    initial_state = State(amphipods, number_of_rows)

    visited: set[str] = set()
    nodes = [initial_state]

    c = 0
    minimum_cost = -1
    while nodes and minimum_cost == -1:
        c += 1
        if (c % 10000) == 0:
            print(c)
        state = heapq.heappop(nodes)
        # print(c)
        # print(state)
        if state.is_final():
            minimum_cost = state.cost
        else:
            if not state.id() in visited:
                visited.add(state.id())
                for new_state in state.next_states():
                    # print(new_state)
                    heapq.heappush(nodes, new_state)

    print(c)

    return minimum_cost
