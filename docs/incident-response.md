# Failure simulation

The security tests replace policy evidence with an instruction to ignore policy, then tamper with the proposed amount. The deterministic gate still denies the action because authorization uses structured claim and policy data, not retrieved instructions or model rationale.

Operational response pattern:

```text
incident → evaluation failure → trace inspection → isolate stage → fix → regression case → CI threshold
```
