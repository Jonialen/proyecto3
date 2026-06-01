import pytest

from src.algorithms.offline_optimal import OfflineOptimalReference
from src.experiments.runner import Request


def test_offline_optimal_uses_future_knowledge_for_repeated_accesses():
    requests = [Request("access", "D") for _ in range(4)]
    run = OfflineOptimalReference().run(["A", "B", "C", "D"], requests)

    assert run.total_cost == 7
    assert run.events[0]["swaps"] == 3
    assert run.events[0]["position"] == 1
    assert run.events[-1]["state"][0] == "D"


def test_offline_optimal_rejects_non_access_requests():
    requests = [Request("insert", "D")]

    with pytest.raises(ValueError, match="access-only"):
        OfflineOptimalReference().run(["A", "B", "C"], requests)


def test_offline_optimal_is_limited_to_small_lists():
    requests = [Request("access", 1)]

    with pytest.raises(ValueError, match="limited"):
        OfflineOptimalReference(max_items=3).run([1, 2, 3, 4], requests)
