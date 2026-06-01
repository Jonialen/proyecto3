from __future__ import annotations

from typing import Any

from src.algorithms.base import ListAlgorithmBase, OperationResult
from src.analysis.costs import access_cost, delete_cost, insert_cost


class StaticList(ListAlgorithmBase):
    name = "StaticList"

    def access(self, item: Any) -> OperationResult:
        position = self._position_of(item)
        return OperationResult("access", item, access_cost(position), position, state=self.state())

    def insert(self, item: Any) -> OperationResult:
        if item in self._items:
            raise ValueError(f"Item already exists: {item!r}")
        cost = insert_cost(len(self._items))
        self._items.append(item)
        return OperationResult("insert", item, cost, len(self._items), state=self.state())

    def delete(self, item: Any) -> OperationResult:
        position = self._position_of(item)
        cost = delete_cost(position)
        self._items.pop(position - 1)
        return OperationResult("delete", item, cost, position, state=self.state())
