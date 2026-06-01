from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.algorithms.base import ListAlgorithm


@dataclass(frozen=True)
class Request:
    operation: str
    item: Any


@dataclass(frozen=True)
class AlgorithmRun:
    name: str
    total_cost: int
    events: list[dict[str, Any]]


def run_algorithm(algorithm: ListAlgorithm, requests: list[Request]) -> AlgorithmRun:
    events: list[dict[str, Any]] = []
    total_cost = 0

    for request in requests:
        if request.operation == "access":
            result = algorithm.access(request.item)
        elif request.operation == "insert":
            result = algorithm.insert(request.item)
        elif request.operation == "delete":
            result = algorithm.delete(request.item)
        else:
            raise ValueError(f"Unsupported operation: {request.operation}")

        total_cost += result.cost
        events.append(
            {
                "operation": result.operation,
                "item": result.item,
                "cost": result.cost,
                "position": result.position,
                "swaps": result.swaps,
                "moved_to_front": result.moved_to_front,
                "state": result.state,
            }
        )

    return AlgorithmRun(algorithm.name, total_cost, events)
