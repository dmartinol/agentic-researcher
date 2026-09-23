#!/usr/bin/env python3
"""Generate benchmark.json for execute-research evaluation."""

import json
from pathlib import Path
import statistics

def load_json(path):
    """Load JSON file."""
    with open(path) as f:
        return json.load(f)

def main():
    base_dir = Path(__file__).parent

    eval_names = ["generic-execution", "existing-conflict", "blocked-dependency"]

    # Collect data for each configuration
    with_skill_data = []
    without_skill_data = []
    eval_details = []

    for eval_name in eval_names:
        # Load grading and timing for both variants
        with_skill_grading = load_json(base_dir / eval_name / "with_skill" / "grading.json")
        without_skill_grading = load_json(base_dir / eval_name / "without_skill" / "grading.json")
        with_skill_timing = load_json(base_dir / eval_name / "with_skill" / "timing.json")
        without_skill_timing = load_json(base_dir / eval_name / "without_skill" / "timing.json")

        with_skill_data.append({
            "passed": with_skill_grading["passed_assertions"],
            "total": with_skill_grading["total_assertions"],
            "tokens": with_skill_timing["total_tokens"],
            "duration": with_skill_timing["total_duration_seconds"],
        })

        without_skill_data.append({
            "passed": without_skill_grading["passed_assertions"],
            "total": without_skill_grading["total_assertions"],
            "tokens": without_skill_timing["total_tokens"],
            "duration": without_skill_timing["total_duration_seconds"],
        })

        # Calculate improvement
        ws_rate = with_skill_grading["pass_rate"]
        wos_rate = without_skill_grading["pass_rate"]
        delta = ws_rate - wos_rate

        if delta == 0:
            improvement = "Tied"
        else:
            improvement = f"+{delta*100:.0f}%"

        eval_details.append({
            "eval_name": eval_name,
            "with_skill": {
                "passed": with_skill_grading["passed_assertions"],
                "total": with_skill_grading["total_assertions"],
                "pass_rate": ws_rate,
                "tokens": with_skill_timing["total_tokens"],
                "duration_seconds": with_skill_timing["total_duration_seconds"],
            },
            "without_skill": {
                "passed": without_skill_grading["passed_assertions"],
                "total": without_skill_grading["total_assertions"],
                "pass_rate": wos_rate,
                "tokens": without_skill_timing["total_tokens"],
                "duration_seconds": without_skill_timing["total_duration_seconds"],
            },
            "delta": {
                "pass_rate": delta,
                "improvement": improvement,
            }
        })

    # Calculate aggregate statistics
    with_skill_total_passed = sum(d["passed"] for d in with_skill_data)
    with_skill_total_assertions = sum(d["total"] for d in with_skill_data)
    without_skill_total_passed = sum(d["passed"] for d in without_skill_data)
    without_skill_total_assertions = sum(d["total"] for d in without_skill_data)

    with_skill_pass_rate = with_skill_total_passed / with_skill_total_assertions
    without_skill_pass_rate = without_skill_total_passed / without_skill_total_assertions

    with_skill_tokens = [d["tokens"] for d in with_skill_data]
    without_skill_tokens = [d["tokens"] for d in without_skill_data]
    with_skill_durations = [d["duration"] for d in with_skill_data]
    without_skill_durations = [d["duration"] for d in without_skill_data]

    # Build benchmark
    benchmark = {
        "skill_name": "execute-research",
        "iteration": 0,
        "timestamp": "2026-09-22T18:45:00Z",
        "configurations": [
            {
                "name": "with_skill",
                "total_evals": len(eval_names),
                "total_assertions": with_skill_total_assertions,
                "passed_assertions": with_skill_total_passed,
                "pass_rate": with_skill_pass_rate,
                "mean_tokens": statistics.mean(with_skill_tokens),
                "stddev_tokens": statistics.stdev(with_skill_tokens) if len(with_skill_tokens) > 1 else 0,
                "mean_duration_seconds": statistics.mean(with_skill_durations),
                "stddev_duration_seconds": statistics.stdev(with_skill_durations) if len(with_skill_durations) > 1 else 0,
            },
            {
                "name": "without_skill",
                "total_evals": len(eval_names),
                "total_assertions": without_skill_total_assertions,
                "passed_assertions": without_skill_total_passed,
                "pass_rate": without_skill_pass_rate,
                "mean_tokens": statistics.mean(without_skill_tokens),
                "stddev_tokens": statistics.stdev(without_skill_tokens) if len(without_skill_tokens) > 1 else 0,
                "mean_duration_seconds": statistics.mean(without_skill_durations),
                "stddev_duration_seconds": statistics.stdev(without_skill_durations) if len(without_skill_durations) > 1 else 0,
            }
        ],
        "delta": {
            "pass_rate_delta": with_skill_pass_rate - without_skill_pass_rate,
            "pass_rate_improvement": f"+{(with_skill_pass_rate - without_skill_pass_rate)*100:.1f}%",
            "token_delta": statistics.mean(with_skill_tokens) - statistics.mean(without_skill_tokens),
            "token_improvement": f"{((statistics.mean(with_skill_tokens) - statistics.mean(without_skill_tokens)) / statistics.mean(without_skill_tokens) * 100):+.1f}%",
            "duration_delta": statistics.mean(with_skill_durations) - statistics.mean(without_skill_durations),
            "duration_improvement": f"{((statistics.mean(with_skill_durations) - statistics.mean(without_skill_durations)) / statistics.mean(without_skill_durations) * 100):+.1f}%",
        },
        "eval_details": eval_details,
    }

    # Write benchmark.json
    with open(base_dir / "benchmark.json", 'w') as f:
        json.dump(benchmark, f, indent=2)

    print(f"Benchmark generated:")
    print(f"  Pass rate: {with_skill_pass_rate:.1%} vs {without_skill_pass_rate:.1%} ({benchmark['delta']['pass_rate_improvement']})")
    print(f"  Tokens: {statistics.mean(with_skill_tokens):.0f} vs {statistics.mean(without_skill_tokens):.0f} ({benchmark['delta']['token_improvement']})")
    print(f"  Duration: {statistics.mean(with_skill_durations):.1f}s vs {statistics.mean(without_skill_durations):.1f}s ({benchmark['delta']['duration_improvement']})")

if __name__ == "__main__":
    main()
