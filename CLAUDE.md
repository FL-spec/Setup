# CLAUDE.md — Workflow Guide

This repo follows a spec-driven, test-driven build flow:

```
/idea (optional)  →  /grill  →  /autopilot
```

`/idea` and `/grill` are human-in-the-loop — that's where the design thinking
happens. Once `prd.md` exists, the rest is `/autopilot`: it slices the PRD,
dispatches one subagent per slice, reviews each, and refactors before it finishes.

**At the start of every session:** detect the current step from the files
present, tell the developer where they are, run that step, and at the end print
the next command and whether to `/clear`.

---

## Detect the current step

| Files present                        | You are here → run                    |
| ------------------------------------ | ------------------------------------- |
| no `idea.md`, no `prd.md`            | fresh start → suggest `/idea` (optional), else `/grill` |
| `idea.md`, no `prd.md`              | design captured → `/grill`            |
| `prd.md`, no `progress.txt`         | design locked → `/autopilot`          |
| `progress.txt` with open slices     | mid-build → `/autopilot` (continue)   |
| feature archived (`prd.md` gone)    | shipped → next feature: `/idea` or `/grill` |

## End every step with the handoff

- after `/idea` → "Idea doc ready. Next: `/grill`. Recommend `/clear` first."
- after `/grill` → "PRD ready. Next: `/autopilot`. Recommend `/clear` first."
- during `/autopilot` → each slice runs in its own subagent and returns a summary; take the next slice.
- after `/autopilot` → "Feature shipped (built + refactored). Archive PRD + issues. Next feature: `/idea` or `/grill`."

## When to /clear

- **Between phases** (after `/idea`, after `/grill`): `/clear`.
- Slices run in their own subagent, so **no per-slice clear** is needed.
- `/clear` the orchestrator only if its context grows large across many slices.
- Within a single grilling: **do NOT clear**.
- **Never `/compact`** — it leaves context sediment.

---

## Source of truth

| File             | Holds                                              | Lifecycle                |
| ---------------- | -------------------------------------------------- | ------------------------ |
| `CONTEXT.md`     | Domain language — every fuzzy term pinned          | Always current           |
| `prd.md`         | The destination for the current feature            | Archived after ship      |
| `docs/adr/`      | Decisions that are hard to reverse                 | Superseded, never deleted |
| `progress.txt`   | Build log — what each slice did                     | Per feature              |
| `AGENTS.md`      | Repo conventions, commands, gotchas                 | Always current           |
| code + tests     | The real, executable truth                          | Always current           |

After a feature ships, the source of truth is **code + tests + `CONTEXT.md` + ADRs**.

---

## Operating rules

- **One model for the whole run.** Subagents inherit it.
- **One subagent per slice**, each in its own fresh context with only `CONTEXT.md`,
  the relevant ADRs, `AGENTS.md`, and that single slice.
- **Vertical slices only** (schema → API → UI → tests), dependency-ordered.
- **Never weaken a test to make it pass.** Affected tests run in-loop; the full
  suite + typecheck + lint + build run once before each commit.
- **HITL slices** (auth, payments, security, large refactors, product judgment)
  are never handed to a subagent — park them and ping the developer.
- **Guardrails first.** Do not run `/autopilot` until CI is green and the git/secret
  guardrails are in place (see `.claude/settings.json`).

---

## The skills & agents in this repo

Skills (`.claude/skills/<name>/SKILL.md`):
- **idea** — captures intent into `idea.md`.
- **grill** — runs the design interview, then synthesizes `prd.md`.
- **autopilot** — orchestrates slice → subagent-per-slice → review → improve-code.
- **improve-code** — end-of-build refactor and archival.

Agents (`.claude/agents/<name>.md`):
- **slice-implementer** — implements one slice via TDD, commits if green. Returns a summary only.
- **reviewer** — read-only. Reviews one slice against the issue, acceptance criteria, `CONTEXT.md`, and ADRs.

New to the flow? Read **HOW_WE_BUILD.md** — it has the ready-to-copy prompts.
