from app.agent import assess_claim


def test_covered_low_value_claim_is_executed():
    result = assess_claim("claim-001")
    assert result["decision"] == "ALLOW"
    assert result["execution"]["executed"] is True
    assert [step["stage"] for step in result["trace"]["steps"]] == [
        "claim_lookup", "policy_retrieval", "agent_proposal", "policy_gate", "execution"
    ]


def test_high_value_claim_requires_human_review_before_execution():
    result = assess_claim("claim-002")
    assert result["decision"] == "DENY"
    assert result["execution"]["executed"] is False
