import pytest

from src.analysis.potential import amortized_cost, inversion_count, potential_delta


def test_inversion_count_between_two_lists():
    assert inversion_count(["A", "B", "C"], ["A", "B", "C"]) == 0
    assert inversion_count(["C", "B", "A"], ["A", "B", "C"]) == 3
    assert inversion_count(["B", "A", "C"], ["A", "B", "C"]) == 1


def test_inversion_count_requires_same_items():
    with pytest.raises(ValueError):
        inversion_count(["A", "B"], ["A", "C"])


def test_potential_delta_and_amortized_cost():
    delta = potential_delta(["A", "B", "C"], ["A", "B", "C"], ["C", "A", "B"], ["A", "B", "C"])
    assert delta == 2
    assert amortized_cost(5, delta) == 7
