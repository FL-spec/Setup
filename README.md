<div align="center">

# Setup

**A conversation-first foundation for AI-driven software development.**

PRD-led · Test-driven · Multi-agent · Codex + Claude · Main stays green

</div>

---

Use this repository as the template for a new product. Then work normally in chat:

> Let’s plan a new feature for [user] so they can [outcome].

The coding agent inspects the product, interviews you where judgment is required, recommends the strongest option, and finishes with a complete PRD. When you approve that PRD, the handoff is automatic:

`feature branch → vertical slices → TDD → slice commits → independent review → CI repair → merge to main`

You do not create spec files, invoke workflow commands, or repeat the PRD in a second prompt. The branch, durable state, specialist agents, pull request, checks, review loop, and promotion are agent-owned.

## The human contract

| Phase | Human role | Agent result |
|---|---|---|
| Explore | Explain the goal and answer material questions | Repository-aware product options |
| Lock PRD | Approve, reject, or refine decisions | Versioned PRD with acceptance criteria |
| Deliver | No repeated prompting | Tested and independently reviewed feature |
| Promote | No manual merge when policy allows | Green PR merged to `main` |

PRD approval means “continue through delivery and promotion” unless you explicitly say **plan only** or **PR only**. Promotion never means production deployment unless deployment is separately authorized.

## Why this is the 2026 pattern

- **Durable intent.** The conversation becomes a versioned PRD, not ephemeral chat context.
- **One feature branch.** The PRD, slices, implementation commits, review evidence, and PR stay together.
- **Vertical slices.** Each commit proves an observable outcome across the necessary boundaries.
- **TDD by construction.** Every behavior change follows RED → GREEN → REFACTOR.
- **Independent review.** The implementation agent never approves its own slice.
- **Context isolation.** Read-heavy analysis and reviews run in focused subagents that return summaries.
- **Mechanical gates.** Tests, types, lint, build, security, and evals decide promotion—not agent confidence.
- **Finite autonomy.** Recoverable failures loop; unsafe choices, permissions, and repeated failures stop with a precise blocker.

## Codex and Claude

`AGENTS.md` and `WORKFLOW.md` are the canonical, vendor-neutral contract.

- Codex loads `AGENTS.md` and project agents from `.codex/agents/`.
- Claude loads the thin `CLAUDE.md` adapter and agents from `.claude/agents/`.
- Both use the same role contracts under `.agents/roles/`.

Platform-specific files may configure discovery and permissions, but they must not redefine the lifecycle.

## Repository map

| Path | Purpose |
|---|---|
| `AGENTS.md` | Durable operating rules loaded by coding agents |
| `WORKFLOW.md` | Conversation-to-main state machine |
| `CLAUDE.md` | Thin Claude adapter to the canonical contract |
| `.agents/roles/` | Vendor-neutral specialist responsibilities |
| `.codex/agents/` | Project-scoped Codex agent definitions |
| `.claude/agents/` | Claude agent adapters |
| `specs/_template/` | Internal PRD and execution-state scaffold |
| `CONTEXT.md` | Project vocabulary and invariants |
| `docs/adr/` | Hard-to-reverse decisions |
| `scripts/` and `tests/` | Mechanical workflow validation |

## Template setup

Create a private repository from this GitHub template and open it with either Codex or Claude. The agent will detect a fresh project and begin by understanding the product and its first feature. See [SETUP.md](SETUP.md) for Codespaces and local installation.

Before the first product slice, the agent selects the real stack, replaces placeholder project commands in `AGENTS.md`, and makes CI green. The workflow itself is already testable with:

```bash
make check
```

That command is for agents and CI; it is not part of the human feature-planning flow.

