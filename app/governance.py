from .models import Claim, Policy, Proposal, PolicyResult


def enforce_policy(claim: Claim, policy: Policy, proposal: Proposal) -> PolicyResult:
    """Authorize proposed actions without trusting model rationale or amount."""
    if proposal.claim_id != claim.claim_id:
        return PolicyResult("DENY", "proposal claim does not match requested claim")
    if proposal.action != "approve_claim":
        return PolicyResult("DENY", "action is outside the execution allowlist")
    if claim.loss_type not in policy.covered_loss_types:
        return PolicyResult("DENY", "loss type is not covered by policy")
    if proposal.amount != claim.amount:
        return PolicyResult("DENY", "proposed amount does not match authoritative claim amount")
    if proposal.amount > policy.approval_limit:
        return PolicyResult("DENY", "claim exceeds policy approval limit")
    if proposal.amount > policy.requires_human_review_above:
        return PolicyResult("REQUIRE_HUMAN_REVIEW", "claim exceeds autonomous approval threshold")
    return PolicyResult("ALLOW", "claim is covered and within autonomous approval threshold")
