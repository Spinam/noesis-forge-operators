from __future__ import annotations
import json
from typing import List, Dict, Any
from pathlib import Path

from noesis_forge.operators.cmo_operator import CMOOperator, CMOConfig

def load_tasks(path: str) -> List[Dict[str, Any]]:
    tasks = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        tasks.append(json.loads(line))
    return tasks

def run_demo(tasks_path: str, tools_available: bool = True) -> Dict[str, Any]:
    cfg = CMOConfig()
    cmo = CMOOperator(cfg)
    tasks = load_tasks(tasks_path)

    context = {"tools_available": tools_available}
    results = []
    for i, t in enumerate(tasks):
        allow, rationale = cmo.apply(t, context)
        results.append({
            "id": i,
            "prompt": t.get("prompt", ""),
            "allow": allow,
            "score": rationale.get("score"),
            "needs_tools": rationale.get("needs_tools"),
            "components": rationale.get("components"),
        })
    allow_rate = sum(1 for r in results if r["allow"]) / max(1, len(results))
    return {"results": results, "allow_rate": allow_rate}
