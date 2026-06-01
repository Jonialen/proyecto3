from src.algorithms.bit import Bit
from src.algorithms.move_to_front import MoveToFront
from src.algorithms.static_list import StaticList
from src.experiments.runner import Request, run_algorithm


def test_static_list_access_does_not_reorder():
    algorithm = StaticList(["A", "B", "C"])
    result = algorithm.access("C")

    assert result.cost == 3
    assert algorithm.state() == ["A", "B", "C"]


def test_move_to_front_access_cost_and_reorder():
    algorithm = MoveToFront(["A", "B", "C"])
    result = algorithm.access("C")

    assert result.cost == 5
    assert result.swaps == 2
    assert algorithm.state() == ["C", "A", "B"]


def test_move_to_front_repeated_access_becomes_cheap():
    algorithm = MoveToFront(["A", "B", "C"])
    requests = [Request("access", "C"), Request("access", "C")]
    run = run_algorithm(algorithm, requests)

    assert run.total_cost == 6
    assert run.events[-1]["cost"] == 1


def test_bit_is_reproducible_with_seed():
    first = Bit(["A", "B", "C"], seed=7)
    second = Bit(["A", "B", "C"], seed=7)

    assert first.bit_state() == second.bit_state()
