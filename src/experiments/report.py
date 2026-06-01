from __future__ import annotations

from typing import Any

from src.algorithms.bit import Bit
from src.algorithms.move_to_front import MoveToFront
from src.algorithms.offline_optimal import OfflineOptimalReference
from src.algorithms.static_list import StaticList
from src.analysis.competitive import competitive_ratio
from src.analysis.potential import amortized_cost, inversion_count
from src.experiments.runner import AlgorithmRun, Request, run_algorithm


def build_default_runs(
    initial_items: list[Any],
    requests: list[Request],
    bit_seed: int | None = 0,
    include_offline: bool = False,
) -> list[AlgorithmRun]:
    algorithms = [StaticList(initial_items), MoveToFront(initial_items), Bit(initial_items, seed=bit_seed)]
    runs = [run_algorithm(algorithm, requests) for algorithm in algorithms]

    if include_offline:
        runs.append(OfflineOptimalReference().run(initial_items, requests))

    return runs


def build_report(initial_items: list[Any], runs: list[AlgorithmRun], reference_name: str = "StaticList") -> dict[str, Any]:
    reference = _find_run(runs, reference_name)
    summary = []

    for run in runs:
        summary.append(
            {
                "algorithm": run.name,
                "total_cost": run.total_cost,
                "competitive_ratio": competitive_ratio(run.total_cost, reference.total_cost),
                "final_state": run.events[-1]["state"] if run.events else list(initial_items),
            }
        )

    return {
        "reference": reference.name,
        "summary": summary,
        "move_to_front_analysis": _move_to_front_analysis(initial_items, runs, reference),
    }


def format_report(report: dict[str, Any]) -> str:
    lines = [f"Reference: {report['reference']}", "", "Summary:"]
    lines.append("Algorithm | Total cost | Ratio | Final state")
    lines.append("--- | ---: | ---: | ---")

    for row in report["summary"]:
        lines.append(
            f"{row['algorithm']} | {row['total_cost']} | {row['competitive_ratio']:.2f} | {row['final_state']}"
        )

    mtf_rows = report["move_to_front_analysis"]
    if mtf_rows:
        lines.extend(["", "MoveToFront potential analysis:"])
        lines.append("Step | Item | Real cost | Phi | Delta Phi | Amortized cost")
        lines.append("---: | --- | ---: | ---: | ---: | ---:")
        for row in mtf_rows:
            lines.append(
                f"{row['step']} | {row['item']} | {row['real_cost']} | {row['phi']} | "
                f"{row['delta_phi']} | {row['amortized_cost']}"
            )

    return "\n".join(lines)


def _find_run(runs: list[AlgorithmRun], name: str) -> AlgorithmRun:
    for run in runs:
        if run.name == name:
            return run
    raise ValueError(f"Run not found: {name}")


def _move_to_front_analysis(initial_items: list[Any], runs: list[AlgorithmRun], reference: AlgorithmRun) -> list[dict[str, Any]]:
    try:
        mtf = _find_run(runs, "MoveToFront")
    except ValueError:
        return []

    rows = []
    previous_phi = inversion_count(list(initial_items), list(initial_items))

    for index, event in enumerate(mtf.events):
        reference_state = reference.events[index]["state"]
        phi = inversion_count(event["state"], reference_state)
        delta_phi = phi - previous_phi
        rows.append(
            {
                "step": index + 1,
                "item": event["item"],
                "real_cost": event["cost"],
                "phi": phi,
                "delta_phi": delta_phi,
                "amortized_cost": amortized_cost(event["cost"], delta_phi),
            }
        )
        previous_phi = phi

    return rows
