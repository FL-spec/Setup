---
name: grill
description: Interview the developer one question at a time to design a feature, pinning domain terms and decisions, then synthesize prd.md. Use after /idea (or directly) and before /autopilot.
---

# grill

Run a design interview, then write the PRD. This is the human-in-the-loop design
phase — take it seriously and do not rush to code.

> The interview method is adapted from Matt Pocock's `grill-with-docs`. If that
> skill is installed (`.claude/skills/grill-with-docs/`), use its engine; otherwise
> follow the procedure below, which is self-contained.

## The interview

1. Start from the developer's framing: _"I want to add [feature] so that [user]
   can [outcome]."_ Read `idea.md` if it exists.
2. **Read the code first.** Answer every question you can from the codebase so you
   only ask the developer what genuinely needs their judgment.
3. Walk the design tree **one question at a time**. For each question, **recommend
   an answer**. The developer responds **Yes / No / Almost**:
   - **Yes** → lock it, move on.
   - **No** → discard, adjust, re-ask.
   - **Almost** → refine the detail until it's a Yes.
4. Capture alignment **as you go**, inline:
   - **`CONTEXT.md`** — pin every fuzzy term the moment it appears
     (_"'account' → Customer or User?"_).
   - **`docs/adr/NNNN-*.md`** — only for decisions that are hard to reverse,
     surprising, and a real trade-off. Use `docs/adr/0000-template.md`.
5. Keep going until you and the developer share a **complete** design — no
   hand-wavy corners.

## Synthesize the PRD

When the design tree is fully walked, write **`prd.md`** with these sections:

- **Problem**
- **Solution**
- **User Stories**
- **Implementation Decisions**
- **Testing Decisions**
- **Out of Scope**

Favor deep modules. **No file paths, no code snippets.** Do **not** interview
again after the PRD is written.

## Handoff

End by printing:

> "PRD ready (`prd.md`). Next: `/autopilot`. Recommend `/clear` first."
