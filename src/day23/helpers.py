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


def solve(amphipods: list[Amphipod], debug: bool = False):
    number_of_rows = 1 + max([a.pos.coord for a in amphipods if a.type != "H"])
    initial_state = State(amphipods, number_of_rows)

    ordered_states = [initial_state]
    states: dict[str, State] = {}
    open_nodes: set[str] = set()
    closed_nodes: set[str] = set()
    open_nodes.add(initial_state.id)

    c = 0
    minimum_cost = -1
    while ordered_states and minimum_cost == -1:
        c += 1
        if (c % 10000) == 0:
            print(c)
        state = heapq.heappop(ordered_states)
        states[state.id] = state
        closed_nodes.add(state.id)
        if debug:
            print(c)
            print(state)
        if state.is_final():
            minimum_cost = state.cost
        else:
            for child_state in state.next_states():
                if not child_state.id in closed_nodes:
                    if not child_state.id in open_nodes or child_state.cost < states[child_state.id].cost:
                        if debug:
                            print(child_state)
                        states[child_state.id] = child_state
                        open_nodes.add(child_state.id)
                        heapq.heappush(ordered_states, child_state)

    if debug:
        print(c)

    return minimum_cost
