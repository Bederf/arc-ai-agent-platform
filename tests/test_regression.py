from evaluation.run import run


def test_evaluation_regression_threshold():
    report = run()
    assert report["passed"] == report["total"]
    assert report["decision_counts"] == {"ALLOW": 1, "DENY": 4}
    assert report["execution_successes"] == 1
