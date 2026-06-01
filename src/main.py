from __future__ import annotations

import argparse
from pathlib import Path

from src.experiments.loader import load_experiment
from src.experiments.report import build_default_runs, build_report, format_report
from src.project_activities import format_activity_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run online list-update algorithm experiments")
    parser.add_argument(
        "experiment",
        nargs="?",
        default="data/examples/repeated_accesses.json",
        help="Path to an experiment JSON file",
    )
    parser.add_argument("--bit-seed", type=int, default=0, help="Seed used by the BIT algorithm")
    parser.add_argument(
        "--include-offline",
        action="store_true",
        help="Include the exact offline reference for small access-only experiments",
    )
    parser.add_argument(
        "--reference",
        default="StaticList",
        help="Algorithm name used as report reference",
    )
    parser.add_argument(
        "--project-activities",
        action="store_true",
        help="Print the answers required by ADA 2026 Project 3",
    )
    args = parser.parse_args()

    if args.project_activities:
        print(format_activity_summary())
        return

    experiment = load_experiment(Path(args.experiment))
    runs = build_default_runs(
        experiment.initial_items,
        experiment.requests,
        bit_seed=args.bit_seed,
        include_offline=args.include_offline,
    )
    report = build_report(experiment.initial_items, runs, reference_name=args.reference)
    print(format_report(report))


if __name__ == "__main__":
    main()
