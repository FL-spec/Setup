<div align="center">

# Setup

**A clean-sheet starting point for new projects, with a full AI-native SDLC built in.**

Spec-driven · Test-driven · Cross-agent · GitHub-native · Self-verifying · Phone-ready

`v2.1`

`v2.0`

</div>

---

Clone this, rename it, and you start every project on the same rails: a disciplined flow that
takes a diffuse idea through design, documentation, and buildable issues to reviewed pull
requests—with AI doing the heavy lifting and you keeping every decision that matters.

## How we develop

Work **matures**. It doesn't get pushed through a pipeline.

```
/fl-bootstrap  (once per repo)
      ↓
/fl-pm  ⇄  /fl-brainstorm · /fl-research · /fl-prototype · /fl-diagnose
      ↓        one work item, one next step at a time
/fl-pm  →  docs in wiki/ + specs/  →  GitHub issues
      ↓
/fl-implement <N>  →  worktree → coder → reviewer → PR → feedback loop
      ↓
/fl-pm  post-merge  →  specs reconciled, dependents unblocked
```

A plan is a set of **work items sharing one goal**, each carrying exactly one **next step** from
a fixed vocabulary—brainstorm, research, prototype, diagnose, decide, write-document,
create-issues, implement. `/fl-pm` picks the next step by asking what the item actually *lacks*,
dispatches it, records what comes back, and then re-reads **every other item** in light of it.
That last part is what keeps a plan coherent instead of a set of parallel monologues.

| Phase | Command | Human-in-the-loop? | Output |
| --- | --- | --- | --- |
| **0. Configure** | `/fl-bootstrap` | Yes | a wired repo: config, gates, CI, labels, board, seeded docs |
| **1. Shape** | `/fl-pm` → `/fl-brainstorm` | Yes | a plan of resolved work items |
| **2. Learn** | `/fl-research` · `/fl-prototype` · `/fl-diagnose` | Partly | cited facts, verdicts, proven mechanisms |
| **3. Document** | `/fl-pm` synthesize | Review gate | PRDs, specs, ADRs/FDRs—**then it stops** |
| **4. Slice** | `/fl-pm` issues | Your go-ahead | vertical-slice issues, ≤300 LOC, dependency-linked |
| **5. Build** | `/fl-implement <N>` | Only for risky slices | a reviewed PR that closes the issue |
| **6. Reconcile** | `/fl-pm` post-merge | No | specs updated, dependents unblocked |

### Why it's built this way

- **Think with a human, build with agents.** Judgment lives in phases 1–4. Once an issue exists,
  `/fl-implement` runs a coder subagent and a read-only reviewer subagent (up to three rounds)
  and stops at a PR. **It never merges.**
- **Spec before code, as-built after.** `specs/` holds exact contracts implementers follow
  blindly. Where the code and a spec disagree, **the code wins** and the divergence is recorded.
  A PR that changes behaviour a spec describes updates that spec *in the same PR*—a spec that
  lags a merge is worse than no spec, because the next implementer trusts it.
- **Two separate gates before outward state.** Documentation gets written, then **you read it**,
  then issues get cut. Issues created from unreviewed docs are state you never agreed to.
- **Vertical tracer-bullet slices.** Domain → Infrastructure → Service → API/UI for one narrow
  behavior, capped at 300 changed lines including tests, with named strategies for splitting
  anything bigger.
- **Context isolation.** Every slice runs in its own worktree, in a fresh subagent carrying only
  the glossary, the relevant specs and ADRs, the coding standards, and that one issue. The
  orchestrator keeps only the returned summaries—no context rot.
- **Test-driven, always.** RED → GREEN → REFACTOR through the public interface. Tests are never
  weakened to pass; the gates run once before every commit.
- **Decisions are durable and dated.** Business calls become FDRs, technology, and structure calls
  become ADRs. Superseded, never deleted.
- **GitHub is the state store.** Issues, sub-issues, PRs and review threads—not a local
  progress file that goes stale the moment two sessions run at once.
- **Cross-agent by construction.** `AGENTS.md` and `WORKFLOW.md` are the canonical contract, and
  the six roles in `.agents/roles/` are vendor-neutral. `.claude/agents/` and `.codex/agents/` are
  thin adapters, so Claude and Codex run the same lifecycle—and `make check` fails if they ever
  drift apart.
- **Commands are optional.** The always-on `fl-flow` router detects the step from plain language;
  the `/fl-*` commands are there when you want direct control, not as a prerequisite.
- **The template verifies itself.** `make check` validates that the roles match their adapters,
  every skill is invocable, every Markdown link resolves, wiki links survive the mirror, and the
  config still matches its JSON Schema. CI runs it on every PR.
- **Prose is a gate, not a preference.** `make docs` runs [Vale](https://vale.sh/) over the
  documentation with Google's developer style guide and the `signs-of-ai-writing` rule set, built
  from Wikipedia's *Signs of AI Writing*. Warnings fail. It catches hedging clusters, enumeration
  tics, contrastive "not just X, it's Y" phrasing, and chatbot paste artifacts, which makes
  "reads like a person wrote it" checkable rather than a matter of taste. It lints the agent's
  output and yours identically.
- **Design is a contract.** `/fl-design` carries a deliberate-by-default design standard and binds
  it to `specs/design-tokens.md`, so the palette and type scale outlive the session that chose
  them. A UI slice is not done until someone rendered it and looked at it, at 375px, in both
  themes, with real data.

> Full walkthrough with copy-paste prompts: **[HOW_WE_BUILD.md](HOW_WE_BUILD.md)**

## Start a new project

```bash
gh repo create my-project --private --template FL-spec/Setup --clone
cd my-project
claude
```

Then, in Claude:

```
/fl-bootstrap
```

It interviews you on stack and modules, writes the config and coding standards, verifies the
quality gates **by running them**, wires CI, creates the labels, provisions the project board, and
seeds `wiki/` and `specs/` with your real module names. After that, `/fl-pm` opens your first plan.

**The board is fully provisioned, with no clicking.** A new GitHub project ships with three
statuses; this flow needs five (Backlog, Ready, In progress, In review, Done). Bootstrap creates
the board, derives the project, field, and option ids, and writes the missing statuses through
`updateProjectV2Field`.

That mutation deserves a note, because getting it wrong is silent and expensive: it **replaces**
a single-select field's entire option set rather than appending to it. Resend the existing options
without their ids and every one is recreated with a fresh id, detaching every issue sitting in it.
So bootstrap reads the current options first, resends them **with their ids** alongside the new
ones, and counts the items already on the board: zero items is the ordinary case and it proceeds,
anything else and it stops to show you the difference rather than reshuffling statuses that issues
are living in.

Claude reads `CLAUDE.md` at the start of every session, works out where the project actually is—
from the config, the plan folders, open issues, open PRs and live worktrees—tells you, and
prints the next command.

> Mark this repo as a template once: **Settings → Template repository** on GitHub, or
> `gh repo edit FL-spec/Setup --template`.

### Requirements

- `gh` authenticated. Issues and PRs are required.
- Python 3.11+ for the template's own gates (`make check`); `make install-dev` for the two
  optional libraries that enable deep config validation.
- [Vale](https://vale.sh/) for the prose gate (`make docs`), plus `make docs-sync` once to
  download the rule packages. CI installs it for you.
- A project board is **optional**—`github.project.enabled: false` and the flow works from issue
  state alone. With a board, `gh` needs `read:project` and `write:project`
  (`gh auth refresh -s read:project,write:project`).

## Work from your phone

This repo ships with a [dev container](.devcontainer/devcontainer.json) that pre-installs Claude
Code in every GitHub Codespace—so you can drive the whole flow from a phone browser, no PC left
running. See **[SETUP.md](SETUP.md)**.

## What's in here

```
AGENTS.md            Canonical, vendor-neutral agent contract — every agent reads this
WORKFLOW.md          Canonical delivery state machine (mermaid), all agents
CLAUDE.md            Claude adapter: session navigator, /clear policy, role dispatch
HOW_WE_BUILD.md      The method, with ready-to-copy prompts
README.md            You are here
SETUP.md             Phone / Codespaces workflow
Makefile             make check — the template's own gates
.agents/roles/       Canonical role definitions (vendor-neutral)
.codex/              Codex adapters onto those roles
schemas/             JSON Schema for .sdlc/sdlc-config.yml
scripts/             validate_workflow.py · scan_secrets.py
tests/               The template's contract tests
.sdlc/
  sdlc-config.yml    Every identifier, path template and gate command — skills read this
  policies/          coding-standards.md · wiki-conventions.md · writing-standards.md
.claude/
  skills/            fl-flow (always-on router) · fl-bootstrap · fl-pm · fl-brainstorm
                     fl-research · fl-prototype · fl-design · fl-diagnose · fl-implement
                     fl-pr-review
  agents/            Claude adapters onto .agents/roles/
  hooks/             git-guardrails.sh — blocks force-push, hard reset, .env commits
  settings.json      PreToolUse hook wiring
.github/
  workflows/         ci.yml (template contract + stack presets) · security.yml · sync-wiki.yml
  scripts/           flatten_wiki.py — publishes wiki/ to the GitHub Wiki
  pull_request_template.md
wiki/
  CONTEXT.md         Domain glossary — loaded into every subagent
  prd/               Master + child PRDs, dated FDRs
  architecture/      System shape, dated ADRs
  plans/             Plan folders: work items, acceptance and verification records
  reports/           Point-in-time reviews
specs/               Exact contracts, as-built — 00-contracts.md + one per module
.devcontainer/       Codespaces config with Claude Code preinstalled
.vale.ini            Prose gate: Google style + signs-of-ai-writing
```

## Upgrading from v1

v2.0 folds in **both** earlier lines of work: the original `/idea → /grill → /autopilot` flow and
the conversation-first cross-agent delivery contract that followed it.

From the conversation-first work, v2.0 **keeps**: `AGENTS.md` and `WORKFLOW.md` as the canonical
vendor-neutral contract, the `.agents/roles/` ↔ `.claude/agents/` ↔ `.codex/agents/` structure,
command-free invocation (now the `fl-flow` router), the secret scanner and security workflow, the
PR template, and the self-validating template contract behind `make check`.

It **changes**: `specs/` now means the permanent as-built contract layer, so the per-feature
workspace moved to `wiki/plans/<NN>-<slug>/`—where `acceptance.md` and `verification.md` keep
the criterion-to-evidence trail. The execution-state JSON is gone: GitHub issues and PRs are the
state store, and the JSON Schema now validates `.sdlc/sdlc-config.yml` instead. The
`test-architect` role is gone—the slice implementer owns its own first failing test. And
promotion never auto-merges: the PR is where automation stops.

From the v1 flow, the mapping:

| v1 | v2 |
| --- | --- |
| `/idea`, `/grill` (interview) | `/fl-brainstorm` |
| `/grill` (PRD synthesis) | `/fl-pm` synthesize → `wiki/prd/` + `specs/` |
| `/autopilot` (slicing) | `/fl-pm` issues → GitHub issues with the LOC gate |
| `/autopilot` (dispatch) | `/fl-implement <N>`, or `/fl-implement N to M` |
| `slice-implementer`, `reviewer` agents | `coder.md`, `reviewer.md` briefs → general-purpose subagents |
| `/improve-code` | `/fl-pm` post-merge reconcile |
| `progress.txt` | GitHub issues + `wiki/plans/<NN>-<slug>/0-plan_map.md` |
| `CONTEXT.md` (root) | `wiki/CONTEXT.md` |
| `docs/adr/` | `wiki/architecture/decisions/` (ADRs) + `wiki/prd/decisions/` (FDRs) |
| `AGENTS.md` (conventions) | `.sdlc/policies/coding-standards.md`; `AGENTS.md` is now a pointer |

An existing v1 project keeps working as it is—v2 is for repos you start from the template now.
To migrate one, run `/fl-bootstrap` and move the contents of `CONTEXT.md` and `docs/adr/` to
their new homes.

---

<div align="center">
<sub>v2.0—the plan-maturity SDLC, generalized from a production repo. The interview method
descends from Matt Pocock's <code>grill-with-docs</code>; everything else is ours.</sub>
</div>
