from __future__ import annotations

from typing import Any


def inversion_count(left: list[Any], right: list[Any]) -> int:
    if set(left) != set(right) or len(left) != len(right):
        raise ValueError("Lists must contain the same unique items")

    right_positions = {item: index for index, item in enumerate(right)}
    mapped = [right_positions[item] for item in left]
    inversions = 0

    for i, value in enumerate(mapped):
        for later in mapped[i + 1 :]:
            if value > later:
                inversions += 1

    return inversions


def potential_delta(before_alg: list[Any], before_ref: list[Any], after_alg: list[Any], after_ref: list[Any]) -> int:
    return inversion_count(after_alg, after_ref) - inversion_count(before_alg, before_ref)


def amortized_cost(real_cost: int, delta_phi: int) -> int:
    return real_cost + delta_phi
