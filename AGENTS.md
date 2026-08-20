# AGENTS.md

Conventions every agent — and every human — follows in this repo.

**This file is a pointer, not the source.** It exists so tools that read `AGENTS.md` by
convention (Codex, Cursor, Copilot, and anything else that doesn't read `CLAUDE.md`) land on the
right material instead of guessing.

## Read these, in this order

1. **[CLAUDE.md](CLAUDE.md)** — how work flows through this repo, how to detect what step the
   project is on, and what to run next.
2. **[.sdlc/policies/coding-standards.md](.sdlc/policies/coding-standards.md)** — the stack,
   the per-module conventions, the non-negotiables, the testing rules, the known gaps, and the
   gotchas. **This is the source of truth for how code gets written here.**
3. **[.sdlc/sdlc-config.yml](.sdlc/sdlc-config.yml)** — every identifier, path template, and
   quality-gate command. Read values from here; never hardcode them.
4. **[wiki/CONTEXT.md](wiki/CONTEXT.md)** — the domain glossary. Use these words exactly.
5. **[specs/](specs/)** — the exact technical contracts, one file per module plus
   `specs/00-contracts.md` for anything crossing a module boundary. **Follow them blindly**;
   where a spec and the code disagree, the code wins and the divergence belongs in the spec's
   §7 Current State.

## The short version

- **Vertical slices only.** One narrow behavior, Domain → Infrastructure → Service → API/UI, at
  or under `implement.max_changed_loc` including tests.
- **TDD**: RED → GREEN → REFACTOR, one behavior at a time, through the public interface.
- **Never weaken, skip, or delete a test to make it pass.**
- **Every quality gate green before a commit**, per module touched.
- **A change to behaviour a spec describes updates that spec in the same PR.**
- **No secrets in code.** Env vars or gitignored config only.
- **Ask before adding a dependency.**
- **Never merge.** The PR is where automation stops.

## Commands

Every runnable command lives under `quality_gates` in
[.sdlc/sdlc-config.yml](.sdlc/sdlc-config.yml), per module. Take them **verbatim from that file**
rather than from memory — it is what CI runs and what the reviewer checks.
