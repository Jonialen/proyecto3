from __future__ import annotations

from itertools import permutations
from math import inf
from typing import Any

from src.analysis.costs import access_cost, adjacent_swap_cost
from src.analysis.potential import inversion_count
from src.experiments.runner import AlgorithmRun, Request


class OfflineOptimalReference:
    name = "OfflineOptimalReference"

    def __init__(self, max_items: int = 7) -> None:
        self.max_items = max_items

    def run(self, initial_items: list[Any], requests: list[Request]) -> AlgorithmRun:
        if len(initial_items) > self.max_items:
            raise ValueError(f"Offline optimal is limited to {self.max_items} items")
        if any(request.operation != "access" for request in requests):
            raise ValueError("Offline optimal currently supports access-only experiments")

        states = [tuple(state) for state in permutations(initial_items)]
        start = tuple(initial_items)
        costs = {state: inf for state in states}
        costs[start] = 0
        parents: dict[tuple[int, tuple[Any, ...]], tuple[tuple[Any, ...], int, int, int]] = {}

        for step, request in enumerate(requests):
            next_costs = {state: inf for state in states}
            for current_state, current_cost in costs.items():
                if current_cost == inf:
                    continue

                for access_state in states:
                    swaps = inversion_count(list(current_state), list(access_state))
                    position = access_state.index(request.item) + 1
                    event_cost = adjacent_swap_cost(swaps) + access_cost(position)
                    candidate = current_cost + event_cost

                    if candidate < next_costs[access_state]:
                        next_costs[access_state] = candidate
                        parents[(step, access_state)] = (current_state, event_cost, position, swaps)

            costs = next_costs

        if not requests:
            return AlgorithmRun(self.name, 0, [])

        final_state = min(costs, key=costs.get)
        total_cost = int(costs[final_state])
        events = []

        state = final_state
        for step in range(len(requests) - 1, -1, -1):
            previous_state, event_cost, position, swaps = parents[(step, state)]
            request = requests[step]
            events.append(
                {
                    "operation": request.operation,
                    "item": request.item,
                    "cost": event_cost,
                    "position": position,
                    "swaps": swaps,
                    "moved_to_front": False,
                    "state": list(state),
                }
            )
            state = previous_state

        events.reverse()
        return AlgorithmRun(self.name, total_cost, events)
