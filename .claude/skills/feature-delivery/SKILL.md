---
name: feature-delivery
description: Apply the repository's conversation-first PRD-to-main workflow whenever the user plans, approves, builds, resumes, reviews, or promotes a feature. Invoke automatically when relevant; no slash command is required.
user-invocable: false
---

# Feature delivery adapter

Read `AGENTS.md` and `WORKFLOW.md` completely and follow them as the canonical lifecycle.

Keep the user experience conversational:

- create the feature branch and spec workspace yourself;
- interview and recommend until the PRD is complete;
- wait for explicit PRD approval before product-code implementation;
- after approval, continue automatically through slices, TDD, commits, independent review, verification, and configured promotion;
- stop only on completion or a mandatory escalation condition.

Do not introduce a separate Claude-only workflow or ask the user to invoke a command.

