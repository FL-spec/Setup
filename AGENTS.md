# AGENTS.md

Repo conventions every agent (and human) follows. Keep this current — it's loaded
into every slice subagent. Fill in the bracketed parts when you set up a project.

## Commands

> Replace with the real commands for this project's stack once chosen.

- Install: `[pnpm install]`
- Dev: `[pnpm dev]`
- Test (all): `[pnpm test]`
- Test one file: `[pnpm vitest run <path>]`
- Typecheck: `[pnpm typecheck]`
- Lint: `[pnpm lint]`
- Build: `[pnpm build]`
- E2E: `[pnpm playwright test]`

## Conventions

- [Domain naming — use the terms pinned in `CONTEXT.md`, nothing fuzzier.]
- [Folder structure / module boundaries.]
- [Patterns to follow; patterns to avoid.]
- Favor **deep modules**: simple interface, meaningful work behind it.

## PR / commit rules

- **One vertical slice per PR.** No unrelated changes.
- Tests + typecheck + lint + build must pass before commit.
- Conventional, descriptive commit messages.
- Never weaken or skip a test to make it green.

## Security

- **Never commit secrets.** Use env vars; validate them at startup.
- **Ask before adding a dependency.**
- Treat all external input as untrusted.

## Testing

- TDD: RED → GREEN → REFACTOR.
- Affected test file runs in-loop; full suite once before commit.
- E2E covers the critical path only.

## Gotchas

> Appended automatically during builds. Real, surprising things that bit us.

- _(none yet)_
