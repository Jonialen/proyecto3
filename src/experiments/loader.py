from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.experiments.runner import Request


@dataclass(frozen=True)
class ExperimentInput:
    initial_items: list[Any]
    requests: list[Request]


def load_experiment(path: Path) -> ExperimentInput:
    with path.open(encoding="utf-8") as file:
        payload = json.load(file)

    try:
        initial_items = payload["initial_items"]
        raw_requests = payload["requests"]
    except KeyError as exc:
        raise ValueError(f"Missing required experiment field: {exc.args[0]}") from exc

    if not isinstance(initial_items, list) or not initial_items:
        raise ValueError("initial_items must be a non-empty list")
    if len(initial_items) != len(set(initial_items)):
        raise ValueError("initial_items must contain unique values")
    if not isinstance(raw_requests, list):
        raise ValueError("requests must be a list")

    requests = []
    for index, request in enumerate(raw_requests):
        if not isinstance(request, dict):
            raise ValueError(f"Request {index} must be an object")
        try:
            requests.append(Request(request["operation"], request["item"]))
        except KeyError as exc:
            raise ValueError(f"Request {index} missing field: {exc.args[0]}") from exc

    return ExperimentInput(initial_items, requests)
