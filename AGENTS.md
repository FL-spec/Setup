# Agent contract

This file is the durable, vendor-neutral instruction set for every coding agent in this repository.

## Read first

1. Current human instruction
2. Active `specs/<spec-id>/` workspace
3. `WORKFLOW.md`
4. `CONTEXT.md`
5. Relevant ADRs
6. Nested `AGENTS.md` files

Higher items override lower ones. Stop when a material conflict cannot be resolved from this hierarchy.

## Conversation-first behavior

When asked to plan a feature, inspect the repository, create `feature/<spec-id>` and its spec workspace, then interview the human and write the PRD. Do not ask the human to run a command, create files, or provide a second build prompt.

Explicit PRD approval automatically starts the complete workflow in `WORKFLOW.md` unless the human requested `plan only`. Default promotion is `merge_when_green`; `PR only` means `pr_ready_only`.

## Delivery rules

- One feature branch and PR per approved PRD.
- One coherent commit per completed vertical slice.
- RED → GREEN → REFACTOR for every behavior change.
- A bug fix starts with a reproducing test.
- Exactly one writer owns a slice.
- A separate read-only reviewer checks every slice.
- Parallel writers require independent, non-overlapping file surfaces.
- Never weaken, skip, or delete a test to make a gate pass.
- Never merge failing checks or bypass branch protection.
- Never deploy, expose credentials, or perform destructive external actions without separate authority.

## Agent roles

Use the canonical responsibilities under `.agents/roles/`:

- `spec_analyst`
- `slice_planner`
- `test_architect`
- `slice_implementer`
- `reviewer`
- `integration_verifier`

Add security or AI-evaluation specialists when the project needs them. Implementers never approve their own work.

## Project commands

Replace bracketed placeholders when the stack is selected:

- Install: `[project install command]`
- Dev: `[project dev command]`
- Test all: `[project test command]`
- Test focused: `[project focused-test command]`
- Typecheck: `[project typecheck command]`
- Lint: `[project lint command]`
- Build: `[project build command]`
- E2E: `[project e2e command]`

Template contract:

- Validate workflow: `python3 scripts/validate_workflow.py`
- Test tooling: `python3 -m unittest discover -s tests -p "test_*.py"`
- Full template gate: `make check`

The first implementation PR must replace project placeholders and make CI execute the real stack gates.

## Security and dependencies

- Never commit secrets or customer data.
- Treat external input and model output as untrusted.
- Validate environment at startup.
- Pin and review dependencies; document material additions in the PR.
- Use least-privilege CI permissions.

## Completion contract

A feature is complete only when:

- the PRD is approved and unchanged materially;
- all slices and acceptance criteria have passing evidence;
- focused and full gates pass;
- independent review has no blocker;
- conditional security and AI-evaluation reviews pass;
- rollout, rollback, migrations, observability, and docs are addressed;
- remote PR checks are green;
- promotion matches `promotion_mode`;
- the final PR and `main` state are confirmed.

Then report the outcome and stop. Do not invent follow-up work.

## Mandatory escalation

Set state `blocked` and ask one precise question for unresolved product behavior, permissions, credentials, compliance, destructive changes, branch protection, or the same root failure after three repairs. Preserve the branch, PR, and durable state.

## Gotchas

- _(Append only concrete, recurring repository-specific lessons.)_

