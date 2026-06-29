---
name: idea
description: Capture raw intent for a new feature into idea.md before any design or code. Use at the very start, when the idea is still fuzzy.
---

# idea

Capture intent **before** designing. Light touch — no architecture, no code, no
file paths. The goal is a clear problem statement you can later `/grill` into a spec.

## Steps

1. Ask the developer for the one-liner: _"I want to build [thing] for [who] so
   they can [outcome]."_ If they already gave it, use it.
2. Have a short, low-pressure conversation to draw out:
   - **Problem** — what's painful or missing today.
   - **Who it's for** — the user/persona.
   - **Rough shape** — the gist of the solution, not the design.
   - **Open questions** — what's genuinely undecided.
3. Write **`idea.md`** with exactly those four sections. Keep it to a page.
4. Do **not** propose architecture, schemas, or code.

## Handoff

End by printing:

> "Idea doc ready (`idea.md`). Next: `/grill`. Recommend `/clear` first."
