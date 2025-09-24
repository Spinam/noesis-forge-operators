from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class OperatorVersion:
    version: str
    spec: Dict[str, Any]

@dataclass
class OperatorRecord:
    id: str
    name: str
    versions: List[OperatorVersion] = field(default_factory=list)

class AppendOnlyRegistry:
    """Minimal append-only registry for operator specs.
    This keeps everything in memory for the demo; production should persist to storage.
    """
    def __init__(self) -> None:
        self._records: Dict[str, OperatorRecord] = {}

    def register(self, op_id: str, name: str, version: str, spec: Dict[str, Any]) -> None:
        rec = self._records.get(op_id)
        if rec is None:
            rec = OperatorRecord(id=op_id, name=name, versions=[])
            self._records[op_id] = rec
        # Append only: refuse overwrite of an existing version tag
        if any(v.version == version for v in rec.versions):
            raise ValueError(f"Version {version} already exists for operator {op_id}. Append a new version tag.")
        rec.versions.append(OperatorVersion(version=version, spec=spec))

    def latest(self, op_id: str) -> OperatorVersion | None:
        rec = self._records.get(op_id)
        if not rec or not rec.versions:
            return None
        return rec.versions[-1]

    def list(self) -> List[OperatorRecord]:
        return list(self._records.values())
