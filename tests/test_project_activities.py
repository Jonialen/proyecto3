from src.project_activities import (
    DEFAULT_CONFIGURATION,
    SEQUENCE_1,
    SEQUENCE_2,
    brute_force_extremes,
    build_activity_answers,
    minimum_mtf_sequence,
    run_imtf_access_cost,
    run_mtf_access_cost,
    worst_mtf_sequence,
)


def test_project_sequence_1_total_access_cost():
    run = run_mtf_access_cost(DEFAULT_CONFIGURATION, SEQUENCE_1)

    assert run.total_cost == 90
    assert run.steps[0].before == [0, 1, 2, 3, 4]
    assert run.steps[-1].after == [4, 3, 2, 1, 0]


def test_project_sequence_2_total_access_cost():
    run = run_mtf_access_cost(DEFAULT_CONFIGURATION, SEQUENCE_2)

    assert run.total_cost == 67


def test_minimum_and_worst_sequences_match_bruteforce_for_short_length():
    expected_best, expected_worst = brute_force_extremes(DEFAULT_CONFIGURATION, 5)

    assert minimum_mtf_sequence(DEFAULT_CONFIGURATION, 5).total_cost == expected_best.total_cost
    assert worst_mtf_sequence(DEFAULT_CONFIGURATION, 5).total_cost == expected_worst.total_cost


def test_project_minimum_and_worst_for_twenty_requests():
    assert minimum_mtf_sequence(DEFAULT_CONFIGURATION, 20).sequence == [0] * 20
    assert minimum_mtf_sequence(DEFAULT_CONFIGURATION, 20).total_cost == 20
    assert worst_mtf_sequence(DEFAULT_CONFIGURATION, 20).sequence == [4, 3, 2, 1, 0] * 4
    assert worst_mtf_sequence(DEFAULT_CONFIGURATION, 20).total_cost == 100


def test_repeated_sequences_pattern():
    answers = build_activity_answers()

    assert answers["repeat_2"].total_cost == 22
    assert answers["repeat_3"].total_cost == 23


def test_imtf_lookahead_moves_only_when_request_reappears_soon():
    run = run_imtf_access_cost(DEFAULT_CONFIGURATION, [2, 0, 2])

    assert run.total_cost == 6
    assert run.steps[0].moved_to_front is True
    assert run.steps[-1].moved_to_front is False


def test_imtf_on_mtf_extreme_sequences():
    answers = build_activity_answers()

    assert answers["imtf_minimum"].total_cost == 20
    assert answers["imtf_worst"].total_cost == 60
