from dataclasses import asdict, dataclass, field
import json
import uuid


@dataclass
class Trace:
    run_id: str = field(default_factory=lambda: f"run-{uuid.uuid4().hex[:12]}")
    steps: list[dict] = field(default_factory=list)

    def record(self, stage: str, input_data: dict, output_data: dict) -> None:
        self.steps.append({"stage": stage, "input": input_data, "output": output_data})

    def as_dict(self) -> dict:
        return asdict(self)

    def as_json(self) -> str:
        return json.dumps(self.as_dict(), indent=2, sort_keys=True)
