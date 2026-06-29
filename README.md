<div align="center">

# Setup

**A clean-sheet starting point for new projects, with an AI-native development framework built in.**

Spec-driven · Test-driven · Subagent-orchestrated · Phone-ready

</div>

---

Clone this, rename it, and you start every project on the same rails: a
disciplined flow that turns an idea into shipped, tested code with AI doing the
heavy lifting and you staying in control of the decisions that matter.

## How we develop

The whole method is three commands:

```
/idea (optional)  →  /grill  →  /autopilot
```

| Phase | Command | Human-in-the-loop? | Output |
| ----- | ------- | ------------------ | ------ |
| **1. Capture** | `/idea` | Yes (optional) | `idea.md` — problem, who it's for, rough shape |
| **2. Design** | `/grill` | Yes | `prd.md` — interviewed into a complete spec |
| **3. Build** | `/autopilot` | No (parks HITL slices) | shipped, tested, reviewed code |

The principle: **think with a human, build with agents.** `/idea` and `/grill`
are where judgment lives — you make the design decisions one question at a time.
Once the PRD exists, `/autopilot` takes over: it breaks the spec into vertical
slices, dispatches **one subagent per slice** (each writing tests first), reviews
every slice with a read-only reviewer, and runs a final refactor pass before it
calls the feature done.

### Why it's built this way

- **Spec before code.** The PRD is the destination. Agents don't guess intent —
  they implement an agreed design.
- **Vertical tracer-bullet slices.** Each slice goes schema → API → UI → tests,
  so every step is observable and shippable, never a half-wired layer.
- **Test-driven, always.** RED → GREEN → REFACTOR. Tests are never weakened to
  pass; the full suite + typecheck + lint + build gate every commit.
- **Context isolation.** Each slice runs in a fresh subagent with only what it
  needs (`CONTEXT.md`, relevant ADRs, `AGENTS.md`, the slice). The orchestrator
  keeps only the returned summaries — no context rot.
- **Decisions are durable.** Domain language lives in `CONTEXT.md`; hard-to-reverse
  choices become ADRs in `docs/adr/`. Code + tests are the final source of truth.

> Full walkthrough with copy-paste prompts: **[HOW_WE_BUILD.md](HOW_WE_BUILD.md)**

## Start a new project

```bash
gh repo create my-project --private --template FL-spec/Setup --clone
cd my-project
claude
```

Claude reads `CLAUDE.md`, detects you're at a fresh start, and points you to
`/idea` or `/grill`. From there, just follow the handoffs it prints at the end of
each step.

> First, mark this repo as a template once: **Settings → Template repository** on
> GitHub (or `gh repo edit FL-spec/Setup --template`).

## Work from your phone

This repo ships with a [dev container](.devcontainer/devcontainer.json) that
pre-installs Claude Code in every GitHub Codespace — so you can drive the whole
flow from a phone browser, no PC left running. See **[SETUP.md](SETUP.md)**.

## What's in here

```
CLAUDE.md            Session guide — Claude reads this every session to navigate the flow
README.md            You are here
HOW_WE_BUILD.md      The method, with ready-to-copy prompts
AGENTS.md            Repo conventions, commands, gotchas
CONTEXT.md           Domain language — every fuzzy term pinned (filled in as you design)
SETUP.md             Phone / Codespaces workflow
docs/adr/            Architecture Decision Records (hard-to-reverse decisions)
.claude/
  skills/            idea · grill · autopilot · improve-code
  agents/            slice-implementer · reviewer
  settings.json      Git & secret guardrails (PreToolUse hook)
.devcontainer/       Codespaces config with Claude Code preinstalled
```

## Conventions

This template is stack-agnostic. Before your first `/autopilot`, set up the
feedback loops the framework relies on and record the commands in
[AGENTS.md](AGENTS.md):

- Strict type checking (e.g. strict TypeScript)
- A unit test runner (e.g. `vitest`)
- E2E on the critical path (e.g. `playwright`)
- Green CI
- Guardrails: the git/secret `PreToolUse` hook in `.claude/settings.json`

**Do not run `/autopilot` until CI is green and the guardrails are in place.**

---

<div align="center">
<sub>Built on the idea → grill → autopilot flow. The interview engine is adapted from Matt Pocock's <code>grill-with-docs</code>; everything else is ours.</sub>
</div>
