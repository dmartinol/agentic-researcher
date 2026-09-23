# Evaluation results

Agentic Researcher uses the [Agent Skills evaluation convention](https://agentskills.io/skill-creation/evaluating-skills): realistic cases are run in isolated contexts both with the target skill and without it as a baseline. Iteration 0 measures observable behavior before any optimization of the skills against the eval corpus.

The canonical machine-readable results are each skill's `benchmark.json`; the corresponding `EVALUATION_SUMMARY.md`, grading, timing, fixtures, and raw outputs (where retained) are published in the adjacent `*-workspace/iteration-0/` directory.

## Published Iteration 0 results

Nine of the eleven individual skills currently have published Iteration 0 results. Cross-skill composition and full-lifecycle suites are defined but have not yet been executed.

| Skill | With skill | Baseline | Delta | Results |
| --- | ---: | ---: | ---: | --- |
| `research-evidence` | 93% (16/17) | 71% (12/17) | +22 pp | [benchmark](../skills/research-evidence-workspace/iteration-0/benchmark.json) · [summary](../skills/research-evidence-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `manage-research-memory` | 100% (15/15) | 60% (9/15) | +40 pp | [benchmark](../skills/manage-research-memory-workspace/iteration-0/benchmark.json) · [summary](../skills/manage-research-memory-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `research-synthesis` | 100% (15/15) | 86.7% (13/15) | +13.3 pp | [benchmark](../skills/research-synthesis-workspace/iteration-0/benchmark.json) · [summary](../skills/research-synthesis-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `plan-research` | 100% (9/9) | 33.3% (3/9) | +66.7 pp | [benchmark](../skills/plan-research-workspace/iteration-0/benchmark.json) · [summary](../skills/plan-research-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `initialize-research` | 100% (14/14) | 71.4% (10/14) | +28.6 pp | [benchmark](../skills/initialize-research-workspace/iteration-0/benchmark.json) · [summary](../skills/initialize-research-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `execute-research` | 100% (15/15) | 26.7% (4/15) | +73.3 pp | [benchmark](../skills/execute-research-workspace/iteration-0/benchmark.json) · [summary](../skills/execute-research-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `complete-research` | 100% (13/13) | 61.5% (8/13) | +38.5 pp | [benchmark](../skills/complete-research-workspace/iteration-0/benchmark.json) · [summary](../skills/complete-research-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `jira-research` | 100% (13/13) | 46.2% (6/13) | +53.8 pp | [benchmark](../skills/jira-research-workspace/iteration-0/benchmark.json) · [summary](../skills/jira-research-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `confluence-research` | 100% (10/10) | 30% (3/10) | +70 pp | [benchmark](../skills/confluence-research-workspace/iteration-0/benchmark.json) · [summary](../skills/confluence-research-workspace/iteration-0/EVALUATION_SUMMARY.md) |
| `setup-research` | not run | not run | — | eval corpus defined |
| `verify-research` | not run | not run | — | eval corpus defined |

**Coverage:** 9/11 individual skills evaluated (27 cases, 54 with/baseline runs).

The delta is the absolute percentage-point difference between the with-skill and baseline assertion pass rates. These numbers describe this Iteration 0 corpus and model/runtime configuration; they are not universal skill-quality scores.

## Reading the evidence

Use the table as an index, not as a leaderboard. A high absolute pass rate says how the run performed against the assertions derived for these cases. The delta shows the measured behavioral difference from the no-skill baseline on the same cases. Some cases are intentionally or incidentally non-discriminating.

Token and duration measurements are retained in the individual benchmarks where available rather than aggregated here because the generated benchmark formats and measurement availability differ across early runs.

Historical runs do not all contain the same artifact set. In particular, some early evaluations did not preserve raw model responses. Missing historical raw outputs are treated as an experimental limitation and are not reconstructed.

## Remaining Iteration 0 coverage

The authored but unexecuted suites are:

- `setup-research`
- `verify-research`
- `evals/composition/evals.json`
- `evals/lifecycle/evals.json`

They can be run later without blocking publication of the existing results. The repository preserves the current partial coverage explicitly rather than rerunning or modifying results for presentation.
