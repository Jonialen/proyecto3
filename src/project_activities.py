from __future__ import annotations

from dataclasses import dataclass
from itertools import product


DEFAULT_CONFIGURATION = [0, 1, 2, 3, 4]
SEQUENCE_1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
SEQUENCE_2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
SEQUENCE_5_2 = [2] * 20
SEQUENCE_5_3 = [3] * 20


@dataclass(frozen=True)
class AccessStep:
    before: list[int]
    request: int
    cost: int
    after: list[int]
    moved_to_front: bool


@dataclass(frozen=True)
class ActivityRun:
    sequence: list[int]
    steps: list[AccessStep]
    total_cost: int


def run_mtf_access_cost(initial_configuration: list[int], sequence: list[int]) -> ActivityRun:
    configuration = list(initial_configuration)
    steps: list[AccessStep] = []
    total = 0

    for request in sequence:
        before = list(configuration)
        position = configuration.index(request) + 1
        total += position
        _move_to_front(configuration, position)
        steps.append(AccessStep(before, request, position, list(configuration), position > 1))

    return ActivityRun(list(sequence), steps, total)


def run_imtf_access_cost(initial_configuration: list[int], sequence: list[int]) -> ActivityRun:
    configuration = list(initial_configuration)
    steps: list[AccessStep] = []
    total = 0

    for index, request in enumerate(sequence):
        before = list(configuration)
        position = configuration.index(request) + 1
        total += position
        lookahead = sequence[index + 1 : index + position]
        should_move = request in lookahead
        if should_move:
            _move_to_front(configuration, position)
        steps.append(AccessStep(before, request, position, list(configuration), should_move))

    return ActivityRun(list(sequence), steps, total)


def minimum_mtf_sequence(initial_configuration: list[int], length: int) -> ActivityRun:
    first = initial_configuration[0]
    return run_mtf_access_cost(initial_configuration, [first] * length)


def worst_mtf_sequence(initial_configuration: list[int], length: int) -> ActivityRun:
    configuration = list(initial_configuration)
    sequence = []

    for _ in range(length):
        request = configuration[-1]
        sequence.append(request)
        _move_to_front(configuration, len(configuration))

    return run_mtf_access_cost(initial_configuration, sequence)


def brute_force_extremes(initial_configuration: list[int], length: int) -> tuple[ActivityRun, ActivityRun]:
    best: ActivityRun | None = None
    worst: ActivityRun | None = None

    for sequence in product(initial_configuration, repeat=length):
        run = run_mtf_access_cost(initial_configuration, list(sequence))
        if best is None or run.total_cost < best.total_cost:
            best = run
        if worst is None or run.total_cost > worst.total_cost:
            worst = run

    if best is None or worst is None:
        raise ValueError("Length must be non-negative")
    return best, worst


def build_activity_answers() -> dict[str, ActivityRun]:
    best = minimum_mtf_sequence(DEFAULT_CONFIGURATION, 20)
    worst = worst_mtf_sequence(DEFAULT_CONFIGURATION, 20)
    return {
        "activity_1": run_mtf_access_cost(DEFAULT_CONFIGURATION, SEQUENCE_1),
        "activity_2": run_mtf_access_cost(DEFAULT_CONFIGURATION, SEQUENCE_2),
        "minimum": best,
        "worst": worst,
        "repeat_2": run_mtf_access_cost(DEFAULT_CONFIGURATION, SEQUENCE_5_2),
        "repeat_3": run_mtf_access_cost(DEFAULT_CONFIGURATION, SEQUENCE_5_3),
        "imtf_minimum": run_imtf_access_cost(DEFAULT_CONFIGURATION, best.sequence),
        "imtf_worst": run_imtf_access_cost(DEFAULT_CONFIGURATION, worst.sequence),
    }


def format_activity_run(run: ActivityRun) -> str:
    lines = ["Step | Configuration | Request | Cost | Result", "---: | --- | ---: | ---: | ---"]
    for index, step in enumerate(run.steps, start=1):
        lines.append(f"{index} | {step.before} | {step.request} | {step.cost} | {step.after}")
    lines.append(f"Total access cost: {run.total_cost}")
    return "\n".join(lines)


def format_activity_summary() -> str:
    answers = build_activity_answers()
    lines = ["# Project 3 Activity Answers", ""]

    for title, key in [
        ("Activity 1", "activity_1"),
        ("Activity 2", "activity_2"),
        ("Minimum MTF sequence", "minimum"),
        ("Worst MTF sequence", "worst"),
        ("Repeated 2", "repeat_2"),
        ("Repeated 3", "repeat_3"),
        ("IMTF on minimum MTF sequence", "imtf_minimum"),
        ("IMTF on worst MTF sequence", "imtf_worst"),
    ]:
        run = answers[key]
        lines.extend([f"## {title}", "", f"Sequence: {run.sequence}", "", format_activity_run(run), ""])

    return "\n".join(lines)


def _move_to_front(configuration: list[int], position: int) -> None:
    item = configuration.pop(position - 1)
    configuration.insert(0, item)
