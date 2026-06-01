import pytest

from src.analysis.costs import access_cost, adjacent_swap_cost, delete_cost, insert_cost


def test_cost_model_matches_course_definition():
    assert access_cost(3) == 3
    assert delete_cost(2) == 2
    assert insert_cost(4) == 5
    assert adjacent_swap_cost(3) == 3


def test_position_must_be_positive():
    with pytest.raises(ValueError):
        access_cost(0)
