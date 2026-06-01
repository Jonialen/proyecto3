from __future__ import annotations

from typing import Any

from src.algorithms.base import ListAlgorithmBase, OperationResult
from src.analysis.costs import access_cost, adjacent_swap_cost, delete_cost, insert_cost


class MoveToFront(ListAlgorithmBase):
    name = "MoveToFront"

    def access(self, item: Any) -> OperationResult:
        position = self._position_of(item)
        swaps = position - 1
        cost = access_cost(position) + adjacent_swap_cost(swaps)
        self._move_position_to_front(position)
        return OperationResult(
            "access",
            item,
            cost,
            position,
            swaps=swaps,
            moved_to_front=swaps > 0,
            state=self.state(),
        )

    def insert(self, item: Any) -> OperationResult:
        if item in self._items:
            raise ValueError(f"Item already exists: {item!r}")
        size_before = len(self._items)
        self._items.append(item)
        position = size_before + 1
        swaps = position - 1
        cost = insert_cost(size_before) + adjacent_swap_cost(swaps)
        self._move_position_to_front(position)
        return OperationResult(
            "insert",
            item,
            cost,
            position,
            swaps=swaps,
            moved_to_front=swaps > 0,
            state=self.state(),
        )

    def delete(self, item: Any) -> OperationResult:
        position = self._position_of(item)
        cost = delete_cost(position)
        self._items.pop(position - 1)
        return OperationResult("delete", item, cost, position, state=self.state())

    def _move_position_to_front(self, position: int) -> None:
        item = self._items.pop(position - 1)
        self._items.insert(0, item)
