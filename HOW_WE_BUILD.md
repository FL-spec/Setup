# How We Build

The whole method, with prompts you can copy straight into Claude Code.

```
/idea (optional)  →  /grill  →  /autopilot
```

Three phases. You drive the first two; agents drive the third. `/clear` between
phases. That's it.

---

## Phase 1 · `/idea` — capture the intent (optional)

Use this when the idea is still fuzzy and you want to think before designing.
Light touch — no architecture, no code. Produces `idea.md`.

> **Copy this:**
>
> ```
> /idea
>
> I want to build [thing] for [who] so they can [outcome].
> Help me capture the problem, who it's for, the rough shape, and the open
> questions. Keep it light — no architecture yet.
> ```

**End:** Claude writes `idea.md` and says → `/grill`. Then `/clear`.

---

## Phase 2 · `/grill` — design it into a spec

An interview, one question at a time. You answer **Yes / No / Almost**. Claude
reads the code to answer what it can, pins fuzzy terms in `CONTEXT.md`, records
hard-to-reverse decisions as ADRs, and finally writes `prd.md`.

> **Copy this:**
>
> ```
> /grill
>
> I want to add [feature] so that [user] can [outcome].
> Interview me until we share a complete design. One question at a time, and
> recommend an answer for each. Read the code to answer questions you can.
> ```

How to answer:
- **Yes** — agreed, move on.
- **No** — wrong; Claude adjusts and re-asks.
- **Almost** — close; refine the detail.

When the design tree is fully walked, Claude synthesizes everything into `prd.md`
(Problem · Solution · User Stories · Implementation Decisions · Testing Decisions ·
Out of Scope) and stops interviewing.

**End:** PRD ready → `/autopilot`. Then `/clear`.

---

## Phase 3 · `/autopilot` — PRD to shipped, unattended

The orchestrator. It slices the PRD, dispatches one subagent per slice, reviews
each, and refactors before finishing. It runs to completion, pausing only for
HITL slices (auth, payments, security, big refactors, product judgment).

> **Copy this:**
>
> ```
> /autopilot
>
> Build everything in prd.md. Slice it into vertical, dependency-ordered slices,
> dispatch one subagent per slice, review each, and run /improve-code at the end.
> Park any HITL slice and ping me.
> ```

What happens under the hood:

1. **Slice** the PRD into vertical tracer-bullet slices (schema → API → UI →
   tests), each with observable acceptance criteria, tagged **AFK** (unattended)
   or **HITL** (needs you).
2. **Implement** each AFK slice in its own `slice-implementer` subagent via TDD:
   RED (one failing test) → GREEN (minimum code) → REFACTOR. Commit if green.
3. **Review** each slice with the read-only `reviewer` subagent.
4. **`/improve-code`** once the slice graph is done: deepen shallow modules,
   archive `prd.md`, mark superseded ADRs, keep `CONTEXT.md` current.

**End:** "Feature shipped." Next feature → `/idea` or `/grill`.

### When a HITL slice is parked

Claude stops and shows you a one-line summary. Pick it up yourself, or hand it
back once you've made the call:

> **Copy this:**
>
> ```
> Resume autopilot. I've handled the parked slice: [what you did].
> Continue with the next slice.
> ```

---

## Quick reference

| You want to… | Run |
| ------------ | --- |
| Jot down a raw idea | `/idea` |
| Turn an idea into a spec | `/grill` |
| Build the spec | `/autopilot` |
| Continue an interrupted build | `/autopilot` (it reads `progress.txt`) |
| Refactor + archive after shipping | happens inside `/autopilot`; or `/improve-code` alone |

## The rules that keep it safe

- `/clear` between phases. **Never `/compact`.**
- One model for the whole run — subagents inherit it.
- Vertical slices only. No half-wired layers.
- Tests are never weakened to pass. Full suite + typecheck + lint + build before every commit.
- HITL slices never go to a subagent.
- No `/autopilot` until CI is green and guardrails are in place.

Lost? Claude reads `CLAUDE.md` every session and will tell you which step you're on.
