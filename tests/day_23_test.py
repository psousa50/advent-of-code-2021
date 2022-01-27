import pytest
import src.day23.part_1
import src.day23.part_2
from src.day23.models import Amphipod, Move, Position, State


def position(p: str):
    return Position(p[0:1], int(p[1:]))


def test_available_moves_when_at_hallway_should_go_lower_room_spot():
    amphipod = Amphipod("A1", "A", position("H0"))
    non_blocking = Amphipod("A2", "A", position("H3"))
    state = State([amphipod, non_blocking], 3)
    expected = ["A2"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_hallway_blocked():
    amphipod = Amphipod("A", "A", position("H5"))
    blocking = Amphipod("D", "D", position("H3"))
    state = State([amphipod, blocking], 3)
    expected = []
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_hallway_with_peer_at_room():
    amphipod = Amphipod("A1", "A", position("H0"))
    peer = Amphipod("A2", "A", position("A2"))
    state = State([amphipod, peer], 4)
    expected = ["A1"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_hallway_with_stranger_at_room():
    amphipod = Amphipod("A", "A", position("H0"))
    stranger = Amphipod("D", "D", position("A2"))
    state = State([amphipod, stranger], 4)
    expected = []
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_hallway_with_room_full():
    amphipod = Amphipod("A", "A", position("H0"))
    blocking1 = Amphipod("D", "D", position("A0"))
    blocking2 = Amphipod("D", "D", position("A1"))
    state = State([amphipod, blocking1, blocking2], 2)
    expected = []
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_other_room():
    amphipod = Amphipod("A", "A", position("B0"))
    state = State([amphipod], 4)
    expected = ["A3"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_other_room_with_blocked_room():
    amphipod = Amphipod("A1", "A", position("B0"))
    blocking = Amphipod("A1", "A", position("A1"))
    state = State([amphipod, blocking], 3)
    expected = ["A0"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_other_room_blocked_in_hallway():
    amphipod = Amphipod("C", "C", position("B0"))
    other = Amphipod("A", "A", position("H5"))
    state = State([amphipod, other], 3)
    expected = ["H0", "H1", "H3"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_other_room_blocked():
    amphipod = Amphipod("A", "A", position("B2"))
    blocking = Amphipod("D", "D", position("B0"))
    state = State([amphipod, blocking], 3)
    expected = []
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_other_room_with_room_full():
    amphipod = Amphipod("A1", "A", position("B0"))
    blocking1 = Amphipod("A2", "A", position("A0"))
    blocking2 = Amphipod("D", "D", position("A1"))
    state = State([amphipod, blocking1, blocking2], 2)
    expected = ["H0", "H1", "H3", "H5", "H7", "H9", "H10"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_correct_room():
    amphipod = Amphipod("A", "A", position("A1"))
    state = State([amphipod], 4)
    expected = ["A3"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_correct_room_blocking():
    amphipod = Amphipod("A", "A", position("A0"))
    stranger = Amphipod("D", "D", position("A1"))
    state = State([amphipod, stranger], 2)
    expected = ["H0", "H1", "H3", "H5", "H7", "H9", "H10"]
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_correct_room_blocked():
    amphipod = Amphipod("A1", "A", position("A1"))
    other1 = Amphipod("A2", "A", position("A0"))
    other2 = Amphipod("D", "D", position("A2"))
    state = State([amphipod, other1, other2], 3)
    expected = []
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]


def test_available_moves_when_at_correct_place():
    amphipod = Amphipod("A", "A", position("A3"))
    state = State([amphipod], 4)
    expected = []
    assert state.available_moves(amphipod) == [Move(amphipod, position(e)) for e in expected]
