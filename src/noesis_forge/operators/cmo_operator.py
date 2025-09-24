from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Tuple

@dataclass
class CMOConfig:
    curiosity_weight: float = 0.2
    rebuttal_weight: float = 0.2
    safety_weight: float = 0.4
    consistency_weight: float = 0.2

class CMOOperator:
    """A tiny, sanitized demo of the CMO gating/activation operator.
    This *does not* call models. It just shows how weights & invariants might be used.
    """
    def __init__(self, config: CMOConfig) -> None:
        self.cfg = config

    def apply(self, task: Dict[str, Any], context: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """Return (allow, rationale). Task is a small dict from the toy dataset.
        Expected task fields: risk_score, complexity_score, needs_tools (bool).
        """
        risk = float(task.get("risk_score", 0.0))
        complexity = float(task.get("complexity_score", 0.0))
        needs_tools = bool(task.get("needs_tools", False))

        # simple heuristic: higher risk tightens the safety gate
        safety_gate = self.cfg.safety_weight * (1.0 - risk)
        # higher complexity favors more curiosity/rebuttal
        exploration = self.cfg.curiosity_weight * complexity + self.cfg.rebuttal_weight * (1.0 - complexity)
        # consistency placeholder pulls toward moderate decisions
        consistency = self.cfg.consistency_weight * 0.5

        score = safety_gate + exploration + consistency
        allow = score >= 0.6 and (not needs_tools or context.get("tools_available", False))

        rationale = {
            "score": round(score, 4),
            "components": {
                "safety_gate": round(safety_gate, 4),
                "exploration": round(exploration, 4),
                "consistency": round(consistency, 4),
            },
            "needs_tools": needs_tools,
            "tools_available": bool(context.get("tools_available", False)),
        }
        return allow, rationale
