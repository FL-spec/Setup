# How we build

## One continuous conversation

Start with the product outcome:

> I want to plan a feature that lets [user] achieve [outcome].

The agent inspects the current product and interviews you only where judgment is needed. For each material choice it recommends the strongest answer and explains the trade-off. It creates the feature branch and writes the PRD as decisions are agreed.

When the PRD is complete:

- **Approved / lock it / go ahead** — lock the PRD and continue automatically through implementation and merge.
- **Almost** — revise the identified decisions, then present it again.
- **Plan only** — preserve the PRD and stop without implementation.
- **PR only** — implement and verify, but leave the green PR ready instead of merging.

There is no separate build prompt.

## What happens after approval

| Stage | Agent behavior | Durable evidence |
|---|---|---|
| Plan | Map criteria and dependencies into vertical slices | `plan.md`, `slices.md` |
| TDD | RED → GREEN → REFACTOR one slice | Tests and slice commit |
| Review | Separate read-only agent checks behavior and risk | Review findings |
| Repair | Writer fixes blockers and reruns gates | Updated commit/evidence |
| Verify | Full repository and specialist checks | `verification.md` |
| Promote | Reconcile `main`, require green checks, merge | PR and final commit |

The orchestrator continues until the completion contract is met or a mandatory blocker requires a human decision. It does not stop merely because one test or review failed; recoverable failures re-enter the loop.

## Branch model

- `main` must remain releasable.
- Each PRD owns one `feature/<spec-id>` branch.
- Each vertical slice normally owns one commit.
- The feature branch owns one draft PR from locked PRD through final promotion.
- Parallel writes use isolated worktrees/branches only when they cannot overlap.

## Cross-agent model

The lifecycle is not a Claude command and not a Codex-specific prompt. `AGENTS.md`, `WORKFLOW.md`, the spec workspace, and role contracts are portable. Codex and Claude use native adapter files only for discovering the same instructions and subagents.

