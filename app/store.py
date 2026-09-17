from .models import Claim, Policy


CLAIMS = {
    "claim-001": Claim("claim-001", "customer-001", "policy-001", "water_damage", 1200),
    "claim-002": Claim("claim-002", "customer-002", "policy-001", "theft", 1800),
}

POLICIES = {
    "policy-001": Policy(
        "policy-001", frozenset({"water_damage", "fire"}), approval_limit=5000, requires_human_review_above=1500
    )
}

DOCUMENTS = {
    "policy-001": (
        {"id": "policy-001-coverage", "text": "Water damage and fire are covered losses."},
        {"id": "policy-001-limit", "text": "Claims above 1500 require human review."},
    )
}


def get_claim(claim_id: str) -> Claim | None:
    return CLAIMS.get(claim_id)


def get_policy(policy_id: str) -> Policy | None:
    return POLICIES.get(policy_id)


def search_policy(policy_id: str, query: str) -> list[dict[str, str]]:
    del query
    return list(DOCUMENTS.get(policy_id, ()))
