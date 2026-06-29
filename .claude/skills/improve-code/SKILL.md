---
name: improve-code
description: End-of-build refactor and archival pass. Deepen shallow modules, archive the shipped PRD, mark superseded ADRs, and keep CONTEXT.md current. Runs as the final step of /autopilot, or on its own.
---

# improve-code

The closing pass once a feature's slice graph is finished. Quality and tidy-up
only — no new features.

## Steps

1. **Deepen shallow modules.** Find thin wrappers and leaky interfaces; give them
   a simple interface over meaningful work. Remove duplication exposed across slices.
2. **Re-run the gates.** Full suite + typecheck + lint + build must be green.
   Never weaken a test to make this pass.
3. **Archive the PRD.** Move `prd.md` to `docs/archive/` (or delete if tracked in
   git history) and close completed issues — the feature is now described by code +
   tests.
4. **Reconcile ADRs.** Mark any superseded ADR `Superseded by [ADR-NNNN]`. **Never
   delete** an ADR.
5. **Keep `CONTEXT.md` current.** Add any domain terms that emerged during the build.
6. **Tidy `progress.txt`** and ensure real gotchas landed in `AGENTS.md`.

After this, the source of truth is **code + tests + `CONTEXT.md` + ADRs**.

## Handoff

If invoked as autopilot's final step, return control to the orchestrator. If run
standalone, print:

> "Refactor + archival done. Next feature: `/idea` or `/grill`."
