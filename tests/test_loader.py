from pathlib import Path

import pytest

from src.experiments.loader import load_experiment


def test_load_experiment_from_json():
    experiment = load_experiment(Path("data/examples/repeated_accesses.json"))

    assert experiment.initial_items == ["A", "B", "C", "D"]
    assert len(experiment.requests) == 4
    assert experiment.requests[0].operation == "access"
    assert experiment.requests[0].item == "D"


def test_load_experiment_rejects_missing_file():
    with pytest.raises(FileNotFoundError):
        load_experiment(Path("data/examples/missing.json"))
