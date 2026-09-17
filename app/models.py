from dataclasses import dataclass
from typing import Literal


Decision = Literal["ALLOW", "REQUIRE_HUMAN_REVIEW", "DENY"]


@dataclass(frozen=True)
class Claim:
    claim_id: str
    customer_id: str
    policy_id: str
    loss_type: str
    amount: int


@dataclass(frozen=True)
class Policy:
    policy_id: str
    covered_loss_types: frozenset[str]
    approval_limit: int
    requires_human_review_above: int


@dataclass(frozen=True)
class Proposal:
    claim_id: str
    action: str
    amount: int
    rationale: str
    evidence_ids: tuple[str, ...]


@dataclass(frozen=True)
class PolicyResult:
    decision: Decision
    reason: str

