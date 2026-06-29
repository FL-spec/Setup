# How We Build

```
/idea  →  /grill  →  /autopilot
```

You drive the first two. Agents drive the third. `/clear` between each.

---

## 1 · `/idea` — jot it down *(optional)*

For when the idea is still fuzzy. No design, no code.

```
/idea

I want to build [thing] for [who] so they can [outcome].
```

→ writes `idea.md`. Next: `/grill`.

---

## 2 · `/grill` — design it

An interview, one question at a time. You answer **Yes / No / Almost**.

```
/grill

I want to add [feature] so that [user] can [outcome].
Interview me one question at a time. Recommend an answer for each.
```

| You say | Means |
| ------- | ----- |
| **Yes** | locked, move on |
| **No** | wrong — adjust |
| **Almost** | close — refine |

→ writes `prd.md`. Next: `/autopilot`.

---

## 3 · `/autopilot` — build it

Hands-off. Slices the spec, builds each slice in its own subagent (tests first),
reviews, refactors. Stops only for risky slices (auth, payments, security).

```
/autopilot

Build everything in prd.md.
```

→ ships tested code. Next feature: `/idea` or `/grill`.

**If it parks a slice**, handle it, then:

```
Resume autopilot. I handled the parked slice: [what you did].
```

---

## Cheat sheet

| Want to… | Run |
| -------- | --- |
| Capture an idea | `/idea` |
| Design a feature | `/grill` |
| Build it | `/autopilot` |
| Resume a build | `/autopilot` |

**Rules:** `/clear` between phases · never `/compact` · vertical slices only ·
tests never weakened · CI green before `/autopilot`.

> Lost? Claude reads `CLAUDE.md` every session and tells you where you are.
