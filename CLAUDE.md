# Claude adapter

`AGENTS.md` and `WORKFLOW.md` are the canonical contract. Read them before acting, together with the active spec, `CONTEXT.md`, and relevant ADRs.

Use `.claude/agents/` to invoke the vendor-neutral roles defined in `.agents/roles/`. Keep the main conversation focused on product decisions, orchestration, and final results; return summaries from subagents instead of raw logs.

Do not ask the human to invoke `/idea`, `/grill`, `/autopilot`, or any other workflow command. Do not print a “next command” handoff. A natural-language planning conversation creates the branch and PRD; explicit PRD approval automatically starts implementation, review, CI, and promotion according to `WORKFLOW.md`.

