from __future__ import annotations

import random
from typing import Any

from src.algorithms.base import ListAlgorithmBase, OperationResult
from src.analysis.costs import access_cost, adjacent_swap_cost, delete_cost, insert_cost


class Bit(ListAlgorithmBase):
    name = "Bit"

    def __init__(self, initial_items: list[Any], seed: int | None = 0) -> None:
        super().__init__(initial_items)
        rng = random.Random(seed)
        self._bits = {item: rng.randint(0, 1) for item in initial_items}

    def access(self, item: Any) -> OperationResult:
        position = self._position_of(item)
        self._bits[item] = 1 - self._bits[item]
        should_move = self._bits[item] == 1
        swaps = position - 1 if should_move else 0
        cost = access_cost(position) + adjacent_swap_cost(swaps)
        if should_move:
            self._move_position_to_front(position)
        return OperationResult(
            "access",
            item,
            cost,
            position,
            swaps=swaps,
            moved_to_front=should_move and swaps > 0,
            state=self.state(),
        )

    def insert(self, item: Any) -> OperationResult:
        if item in self._items:
            raise ValueError(f"Item already exists: {item!r}")
        size_before = len(self._items)
        self._items.insert(0, item)
        self._bits[item] = 1
        return OperationResult("insert", item, insert_cost(size_before), 1, moved_to_front=True, state=self.state())

    def delete(self, item: Any) -> OperationResult:
        position = self._position_of(item)
        cost = delete_cost(position)
        self._items.pop(position - 1)
        self._bits.pop(item, None)
        return OperationResult("delete", item, cost, position, state=self.state())

    def bit_state(self) -> dict[Any, int]:
        return dict(self._bits)

    def _move_position_to_front(self, position: int) -> None:
        item = self._items.pop(position - 1)
        self._items.insert(0, item)
