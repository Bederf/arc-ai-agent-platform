from .models import Claim, PolicyResult, Proposal


def execute_proposal(claim: Claim, proposal: Proposal, result: PolicyResult) -> dict:
    if result.decision != "ALLOW":
        return {"executed": False, "status": result.decision, "reason": result.reason}
    return {
        "executed": True,
        "status": "approved",
        "claim_id": claim.claim_id,
        "amount": proposal.amount,
    }
