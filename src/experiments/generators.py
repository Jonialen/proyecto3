from __future__ import annotations

import random
from typing import Any

from src.experiments.runner import Request


def repeated_accesses(item: Any, times: int) -> list[Request]:
    if times < 0:
        raise ValueError("Times cannot be negative")
    return [Request("access", item) for _ in range(times)]


def random_accesses(items: list[Any], times: int, seed: int | None = 0) -> list[Request]:
    if not items:
        raise ValueError("Items cannot be empty")
    if times < 0:
        raise ValueError("Times cannot be negative")
    rng = random.Random(seed)
    return [Request("access", rng.choice(items)) for _ in range(times)]
