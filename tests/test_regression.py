from evaluation.run import run


def test_evaluation_regression_threshold():
    report = run()
    assert report["passed"] == report["total"]
