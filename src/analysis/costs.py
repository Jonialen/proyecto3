def access_cost(position: int) -> int:
    if position < 1:
        raise ValueError("Position must be 1-indexed and positive")
    return position


def delete_cost(position: int) -> int:
    return access_cost(position)


def insert_cost(size_before_insert: int) -> int:
    if size_before_insert < 0:
        raise ValueError("Size cannot be negative")
    return size_before_insert + 1


def adjacent_swap_cost(swaps: int = 1) -> int:
    if swaps < 0:
        raise ValueError("Swaps cannot be negative")
    return swaps
