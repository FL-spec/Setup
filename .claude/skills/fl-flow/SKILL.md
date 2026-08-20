---
name: fl-flow
description: Route a plain-language request into this repository's delivery workflow — detect what step the project is actually on and continue from there. Invoke automatically whenever the user talks about planning, building, reviewing, fixing, or shipping something here; no slash command is required.
user-invocable: false
---

# Flow router

The `/fl-*` skills are explicit entry points. **This one is the implicit entry point**: when the
user describes what they want in ordinary language instead of naming a command, work out where
the project actually is and continue from there.

`AGENTS.md` and `WORKFLOW.md` are the canonical contract; `CLAUDE.md` holds the detection table.
Read them rather than improvising a lifecycle.

## What to do

1. **Detect the current step** using `CLAUDE.md`'s detection table and its five commands
   (config placeholders, plan folders, open issues, open PRs, live worktrees).
2. **Name where the project is**, in one line, so the user can correct you cheaply if you're wrong.
3. **Invoke the skill that owns that step** — don't reimplement it here. This skill routes; it
   never does the work itself.
4. **Recommend proceeding.** When the next step is unambiguous, say what you'd do and do it.

## Routing

| The user is talking about | Route to |
|---|---|
| a repo that was never configured | `fl-bootstrap` |
| a new idea, a fuzzy goal, "what should we build" | `fl-pm` (which opens a plan via `fl-brainstorm`) |
| what to work on next, the backlog, a merge that just landed | `fl-pm` |
| an external fact — a library's real behavior, an API, a spec | `fl-research` |
| what something should look like, or whether a model holds up | `fl-prototype` |
| something being wrong, wrong values, a failing path | `fl-diagnose` |
| building a specific issue, or resuming one | `fl-implement` |
| review comments on a PR | `fl-implement` (its feedback loop) |
| reviewing a branch or diff | `fl-pr-review` |

## Boundaries

- **This skill adds no authority.** Everything outward-facing still asks first: creating issues,
  opening PRs, posting review comments, changing repository settings.
- **Never merge**, whatever the user's phrasing implies. The PR is where automation stops.
- **Don't skip the gates.** Routing straight to implementation from a fuzzy request is exactly
  the failure this workflow exists to prevent — if there's no issue, the route is `fl-pm`, not
  `fl-implement`.
- If the request genuinely doesn't belong to this workflow (a one-off question, a shell command,
  reading a file), **don't route at all** — just answer.
