#!/usr/bin/env python3
"""Validate the portable conversation-first development contract."""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "WORKFLOW.md",
    "CLAUDE.md",
    "HOW_WE_BUILD.md",
    "CONTEXT.md",
    ".codex/config.toml",
    ".claude/skills/feature-delivery/SKILL.md",
    "specs/_template/prd.md",
    "specs/_template/plan.md",
    "specs/_template/slices.md",
    "specs/_template/acceptance.md",
    "specs/_template/verification.md",
    "specs/_template/execution-state.json",
    "schemas/execution-state.schema.json",
)

ROLE_NAMES = {
    "spec-analyst",
    "slice-planner",
    "test-architect",
    "slice-implementer",
    "reviewer",
    "integration-verifier",
}

REQUIRED_CONTRACT_PHRASES = (
    "feature/<spec-id>",
    "explicit PRD approval",
    "merge_when_green",
    "RED → GREEN → REFACTOR",
    "read-only reviewer",
)


def validate(root: Path = REPO_ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in root.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {path.relative_to(root)}: {exc}")

    for path in root.rglob("*.toml"):
        try:
            tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid TOML {path.relative_to(root)}: {exc}")

    canonical_roles = {
        path.stem for path in (root / ".agents/roles").glob("*.md")
    }
    codex_roles = {
        path.stem for path in (root / ".codex/agents").glob("*.toml")
    }
    claude_roles = {
        path.stem for path in (root / ".claude/agents").glob("*.md")
    }
    if canonical_roles != ROLE_NAMES:
        errors.append("canonical role set does not match the required role contract")
    if codex_roles != ROLE_NAMES:
        errors.append("Codex role adapters do not match canonical roles")
    if claude_roles != ROLE_NAMES:
        errors.append("Claude role adapters do not match canonical roles")

    workflow_path = root / "WORKFLOW.md"
    if workflow_path.is_file():
        workflow = workflow_path.read_text(encoding="utf-8")
        for phrase in REQUIRED_CONTRACT_PHRASES:
            if phrase not in workflow:
                errors.append(f"WORKFLOW.md is missing contract phrase: {phrase!r}")

    for relative in ("README.md", "CLAUDE.md", "HOW_WE_BUILD.md"):
        path = root / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        if "Next: `/autopilot`" in content or "run `/autopilot`" in content.lower():
            errors.append(f"{relative} still requires the legacy command handoff")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Workflow contract OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

