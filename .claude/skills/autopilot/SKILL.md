---
name: autopilot
description: Orchestrate a PRD to shipped code unattended — slice it, dispatch one subagent per slice, review each, and refactor. Use after prd.md exists. Pauses only for HITL slices.
---

# autopilot

You are the **orchestrator**. You hold the slice graph and `CONTEXT.md`, dispatch
**one subagent per slice**, and keep only the returned summaries in your own
context. Run to completion, pausing only for HITL slices.

**Precondition:** CI is green and the git/secret guardrails in `.claude/settings.json`
are active. If not, stop and tell the developer.

## 1 · Slice

Break `prd.md` into **vertical tracer-bullet slices** (schema → API → UI → tests),
dependency-ordered, written in `CONTEXT.md` vocabulary, each with **observable
acceptance criteria**. Tag each slice:

- **AFK** — safe to implement unattended.
- **HITL** — auth, payments, security, large refactors, or product judgment.

Record the slice graph (with `Blocked by` edges) in `progress.txt`.

## 2 · Dispatch (one `slice-implementer` subagent per AFK slice)

Dispatch in dependency order; independent slices (no `Blocked by`) may run as
parallel subagents. Each subagent starts fresh with `CONTEXT.md`, the relevant
ADRs, `AGENTS.md`, and that **single** slice. It runs TDD:

- Plan the acceptance-criteria tests as a checklist.
- **RED**: one failing test against the public interface.
- **GREEN**: minimum code to pass.
- **REFACTOR**: only once green.
- Affected test file in-loop; full suite + typecheck + lint + build once before commit.
- **Never weaken a test to pass it.**
- Commit if green; append learnings to `progress.txt` and `AGENTS.md` Gotchas.
- Return a **summary only**: what changed, what ran, acceptance-criteria status.

**HITL slices are never handed to a subagent.** Park them with a one-line summary
in `progress.txt` and ping the developer.

## 3 · Review

After each slice, run the read-only `reviewer` subagent against the slice, its
acceptance criteria, `CONTEXT.md`, and ADRs. Address findings before moving on.

## 4 · improve-code (final step)

Once the whole slice graph is finished, run the `improve-code` skill: deepen
shallow modules, archive `prd.md` and completed issues, mark superseded ADRs
(don't delete), keep `CONTEXT.md` current.

## Execution rules

- One model for the whole run (subagents inherit it).
- One subagent per slice, in its own context.
- Affected tests in-loop; full suite once before commit.
- Vertical slices only.

## Handoff

End by printing:

> "Feature shipped (built + refactored). Archive PRD + issues. Next feature: `/idea` or `/grill`."
