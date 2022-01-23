import pytest
import src.day23.part_1
import src.day23.part_2
from src.day23.models import Amphipod, Move, Position, State


@pytest.mark.parametrize(
    "start, end, expected, reason",
    [
        (("H", 1), ("H", 3), [("H", 2), ("H", 3)], "H to H"),
        (("H", 3), ("H", 1), [("H", 2), ("H", 1)], "H to H, reverse"),
        (("H", 1), ("A", 0), [("H", 2), ("A", 0)], "H ro R"),
        (("A", 0), ("H", 1), [("H", 2), ("H", 1)], "R to H"),
        (("A", 0), ("B", 1), [("H", 2), ("H", 3), ("H", 4), ("B", 0), ("B", 1)], "R to R"),
        (("B", 1), ("A", 0), [("B", 0), ("H", 4), ("H", 3), ("H", 2), ("A", 0)], "R to R, reverse"),
        (("A", 0), ("A", 0), [], "Same R, same position"),
        (("A", 0), ("A", 1), [("A", 1)], "Same R, different position"),
        (("A", 1), ("A", 0), [("A", 0)], "Same R, different position, reverse"),
    ],
)
def test_move_path(start, end, expected, reason):
    move = Move(Amphipod("A", "A", Position(start[0], start[1])), Position(end[0], end[1]))
    assert move.path() == [Position(e[0], e[1]) for e in expected], reason


@pytest.mark.parametrize(
    "start, expected, reason",
    [
        (
            ("A", 0),
            [("A", 0), ("A", 1), ("H", 0), ("H", 1), ("H", 3), ("H", 5), ("H", 7), ("H", 9), ("H", 10)],
            "from R",
        ),
        (("H", 3), [("A", 0), ("A", 1)], "from H"),
    ],
)
def test_possible_positions(start, expected, reason):
    a = Amphipod("A", "A", Position(start[0], start[1]))
    state = State([], 2)
    assert state.possible_positions(a) == [Position(e[0], e[1]) for e in expected], reason
