# Feature specifications

Each feature owns one durable workspace under `specs/<spec-id>/` and one `feature/<spec-id>` branch.

The agent creates the workspace automatically during the planning conversation. The human owns product decisions and PRD approval; the agent owns the repository state.

## Required files

| File | Purpose |
|---|---|
| `prd.md` | Approved outcome, scope, quality boundaries, and acceptance criteria |
| `plan.md` | Architecture, risks, rollout, rollback, and verification plan |
| `slices.md` | Dependency-aware vertical delivery units |
| `acceptance.md` | Criterion-to-evidence traceability |
| `verification.md` | Exact final commands and observed results |
| `execution-state.json` | Branch, PR, phase, promotion, and slice state |

Lifecycle: `draft → ready → planning → executing → verifying → promoting → completed`.

Any active state may move to `blocked`. Completed specs remain as historical product and verification records.

