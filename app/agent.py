from dataclasses import asdict

from .execution import execute_proposal
from .governance import enforce_policy
from .models import Proposal
from .store import get_claim, get_policy
from .tools import search_policy_tool
from .trace import Trace


def assess_claim(claim_id: str, *, proposed_action: str = "approve_claim", proposed_amount: int | None = None) -> dict:
    """Run an offline agent-shaped workflow with a provider-independent proposal boundary."""
    trace = Trace()
    claim = get_claim(claim_id)
    if claim is None:
        trace.record("claim_lookup", {"claim_id": claim_id}, {"found": False})
        return {"decision": "DENY", "execution": {"executed": False}, "trace": trace.as_dict()}
    trace.record("claim_lookup", {"claim_id": claim_id}, {"found": True, "claim": asdict(claim)})

    policy = get_policy(claim.policy_id)
    assert policy is not None
    evidence = search_policy_tool(policy.policy_id, claim.loss_type)
    trace.record("policy_retrieval", {"policy_id": policy.policy_id}, evidence)

    proposal = Proposal(
        claim_id=claim.claim_id,
        action=proposed_action,
        amount=claim.amount if proposed_amount is None else proposed_amount,
        rationale="Evidence supports a policy assessment; rationale is advisory only.",
        evidence_ids=tuple(item["id"] for item in evidence["results"]),
    )
    trace.record("agent_proposal", {"claim_id": claim.claim_id}, {"proposal": asdict(proposal)})

    policy_result = enforce_policy(claim, policy, proposal)
    trace.record("policy_gate", asdict(proposal), asdict(policy_result))
    execution = execute_proposal(claim, proposal, policy_result)
    trace.record("execution", asdict(policy_result), execution)
    return {"decision": policy_result.decision, "execution": execution, "trace": trace.as_dict()}
