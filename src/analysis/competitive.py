def competitive_ratio(algorithm_cost: int, reference_cost: int) -> float:
    if reference_cost <= 0:
        raise ValueError("Reference cost must be positive")
    return algorithm_cost / reference_cost
