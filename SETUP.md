# Working on Farmai from your phone (GitHub Codespaces)

This repo includes a dev container ([.devcontainer/devcontainer.json](.devcontainer/devcontainer.json))
that automatically installs **Claude Code** in every Codespace. No PC needs to stay running.

## First time

1. Open the repo on GitHub: https://github.com/FL-spec/Farmai
2. Tap the green **Code** button → **Codespaces** tab → **Create codespace on main**.
3. Wait for it to build (the dev container installs Claude Code automatically on first create).
4. In the Codespace terminal, run:

   ```bash
   claude
   ```

5. Follow the login prompt to authenticate Claude Code (one-time, opens in the browser).

## Day to day

- Reopen your existing Codespace from https://github.com/codespaces (faster than creating a new one).
- Run `claude` in the terminal and work as normal.
- Commit and push when done:

  ```bash
  git add .
  git commit -m "your message"
  git push
  ```

## Tips

- **Phone browser:** the Codespaces web editor works in mobile Safari/Chrome. Request the
  desktop site for a better terminal experience.
- **Stop when idle:** Codespaces bill by usage. Stop the Codespace from
  https://github.com/codespaces when you're done to avoid charges. Stopped Codespaces
  keep your files; they just don't run.
- **If Claude Code isn't found** after opening a Codespace, install it manually:

  ```bash
  npm install -g @anthropic-ai/claude-code
  ```
