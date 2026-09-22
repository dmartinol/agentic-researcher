# Skill Evaluations

This directory defines cross-skill evaluations. Per-skill test cases live beside each skill at `skills/<skill>/evals/evals.json`, following the Agent Skills evaluation convention.

Iteration 0 deliberately contains only realistic prompts and human-readable expected outputs. It does **not** add detailed assertions yet. The Agent Skills evaluation guidance recommends first observing outputs, then deriving objective assertions from useful behavioral differences.

## Iteration 0 protocol

For every per-skill case:

1. Start from a clean agent context.
2. Run the prompt with the target skill available.
3. Run the same prompt without the target skill (or later, against a frozen previous version).
4. Preserve the outputs separately.
5. Record token count and duration when the host exposes them.
6. Review the pair for behavioral differences against `expected_output`.
7. Do not modify the skill during the run set.

Suggested workspace layout:

```text
<skill>-workspace/
└── iteration-0/
    ├── <eval-name>/
    │   ├── with_skill/
    │   │   └── outputs/
    │   └── without_skill/
    │       └── outputs/
    └── ...
```

Generated run outputs, timing, grading, and benchmarks should normally remain outside the skill package unless intentionally checked in as release evidence.

## What to learn

Iteration 0 asks whether each skill changes behavior in a useful way. Pay particular attention to:

- behavior the baseline already performs reliably;
- instructions that materially improve correctness/safety;
- ambiguous instructions causing inconsistent behavior;
- unnecessary token/time cost;
- composition failures where a lifecycle skill does not invoke the intended research capability.

After reviewing the first outputs, Iteration 1 should add specific, observable assertions and mechanical checks where possible. Assertions that pass equally with and without the skill are weak evidence of skill value.

## Cross-skill evaluations

`composition/evals.json` tests interactions among execution, evidence, memory, synthesis, and verification.

`lifecycle/evals.json` tests the product-level approval and mutation boundaries across the full lifecycle.

These complement rather than replace per-skill evals.
