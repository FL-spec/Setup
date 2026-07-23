# Local and Codespaces setup

This template supports both Codex and Claude Code.

## GitHub Codespaces

1. Create a repository from `FL-spec/Setup`.
2. Open **Code → Codespaces → Create codespace on main**.
3. Wait for the dev container to install both CLIs.
4. Start either `codex` or `claude` and authenticate in the browser.
5. Describe the product or feature normally in chat.

The repository instructions handle PRD creation and the delivery loop. You do not invoke a workflow command.

## Local installation

Use the official installation method for the agent you choose:

```bash
npm install --global @openai/codex
npm install --global @anthropic-ai/claude-code
```

Authenticate interactively and open the repository root. Keep GitHub CLI authenticated when you want the agent to create branches, PRs, and promotions.

## Operating notes

- Stop idle Codespaces to avoid charges.
- Use a fresh feature conversation for a new PRD.
- The durable branch/spec state allows a later session or either supported agent to resume.
- Branch protection or required human review may pause automatic promotion; the agent must never bypass it.

