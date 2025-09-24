from __future__ import annotations
from pprint import pprint
from noesis_forge.eval.harness import run_demo

if __name__ == "__main__":
    report = run_demo("data/toy_tasks.jsonl", tools_available=True)
    print("=== CMO Demo Report ===")
    print(f"allow_rate: {report['allow_rate']:.2f}")
    print("results:")
    pprint(report["results"])  # minimal, readable output
