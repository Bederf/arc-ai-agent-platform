from .store import get_claim, get_policy, search_policy


def get_claim_tool(claim_id: str) -> dict:
    claim = get_claim(claim_id)
    return {"found": claim is not None, "claim": claim.__dict__ if claim else None}


def get_policy_tool(policy_id: str) -> dict:
    policy = get_policy(policy_id)
    return {
        "found": policy is not None,
        "policy": {
            "policy_id": policy.policy_id,
            "covered_loss_types": sorted(policy.covered_loss_types),
            "approval_limit": policy.approval_limit,
            "requires_human_review_above": policy.requires_human_review_above,
        }
        if policy
        else None,
    }


def search_policy_tool(policy_id: str, query: str) -> dict:
    return {"results": search_policy(policy_id, query)}
