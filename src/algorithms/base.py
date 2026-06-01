from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass(frozen=True)
class OperationResult:
    operation: str
    item: Any
    cost: int
    position: int | None
    swaps: int = 0
    moved_to_front: bool = False
    state: list[Any] = field(default_factory=list)


class ListAlgorithm(Protocol):
    name: str

    def access(self, item: Any) -> OperationResult:
        ...

    def insert(self, item: Any) -> OperationResult:
        ...

    def delete(self, item: Any) -> OperationResult:
        ...

    def state(self) -> list[Any]:
        ...


class ListAlgorithmBase:
    name = "base"

    def __init__(self, initial_items: list[Any]) -> None:
        if len(initial_items) != len(set(initial_items)):
            raise ValueError("Initial items must be unique")
        self._items = list(initial_items)

    def state(self) -> list[Any]:
        return list(self._items)

    def _position_of(self, item: Any) -> int:
        try:
            return self._items.index(item) + 1
        except ValueError as exc:
            raise ValueError(f"Item not found: {item!r}") from exc
