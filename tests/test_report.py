from pathlib import Path

from src.experiments.loader import load_experiment
from src.experiments.report import build_default_runs, build_report, format_report


def test_build_report_summarizes_costs_and_potential():
    experiment = load_experiment(Path("data/examples/repeated_accesses.json"))
    runs = build_default_runs(experiment.initial_items, experiment.requests, bit_seed=1)
    report = build_report(experiment.initial_items, runs)

    summary = {row["algorithm"]: row for row in report["summary"]}
    assert summary["StaticList"]["total_cost"] == 16
    assert summary["MoveToFront"]["total_cost"] == 10
    assert report["move_to_front_analysis"][0]["phi"] == 3
    assert report["move_to_front_analysis"][0]["amortized_cost"] == 10


def test_format_report_includes_main_sections():
    experiment = load_experiment(Path("data/examples/repeated_accesses.json"))
    runs = build_default_runs(experiment.initial_items, experiment.requests, bit_seed=1)
    text = format_report(build_report(experiment.initial_items, runs))

    assert "Summary:" in text
    assert "MoveToFront potential analysis:" in text
    assert "MoveToFront | 10" in text


def test_report_can_use_offline_reference():
    experiment = load_experiment(Path("data/examples/repeated_accesses.json"))
    runs = build_default_runs(experiment.initial_items, experiment.requests, bit_seed=1, include_offline=True)
    report = build_report(experiment.initial_items, runs, reference_name="OfflineOptimalReference")

    summary = {row["algorithm"]: row for row in report["summary"]}
    assert report["reference"] == "OfflineOptimalReference"
    assert summary["OfflineOptimalReference"]["total_cost"] == 7
    assert summary["MoveToFront"]["competitive_ratio"] == 10 / 7
