"""The template's own contract tests.

These guard the parts of the workflow that rot silently: vendor adapters drifting
from the canonical roles, a skill that can no longer be invoked, a broken link, a
config that stopped matching its schema.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from scripts.scan_secrets import scan_text
from scripts.validate_workflow import REPO_ROOT, ROLE_NAMES, SKILL_NAMES, validate


class WorkflowContractTests(unittest.TestCase):
    def test_repository_contract_is_valid(self) -> None:
        self.assertEqual([], validate(REPO_ROOT))

    def test_every_canonical_role_has_both_vendor_adapters(self) -> None:
        for role in ROLE_NAMES:
            with self.subTest(role=role):
                self.assertTrue((REPO_ROOT / f".agents/roles/{role}.md").is_file())
                self.assertTrue((REPO_ROOT / f".claude/agents/{role}.md").is_file())
                self.assertTrue((REPO_ROOT / f".codex/agents/{role}.toml").is_file())

    def test_every_skill_directory_has_a_skill_file(self) -> None:
        for skill in SKILL_NAMES:
            with self.subTest(skill=skill):
                self.assertTrue((REPO_ROOT / f".claude/skills/{skill}/SKILL.md").is_file())

    def test_the_router_skill_is_not_user_invocable(self) -> None:
        """fl-flow is the implicit entry point; a slash command for it would be a duplicate."""
        text = (REPO_ROOT / ".claude/skills/fl-flow/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("user-invocable: false", text)

    def test_guardrails_hook_is_executable_and_blocks_force_push(self) -> None:
        import json
        import subprocess

        hook = REPO_ROOT / ".claude/hooks/git-guardrails.sh"
        payload = json.dumps({"tool_input": {"command": "git push --force origin main"}})
        blocked = subprocess.run(
            ["bash", str(hook)], input=payload, capture_output=True, text=True
        )
        self.assertEqual(2, blocked.returncode, "force-push must be blocked with exit 2")

        payload = json.dumps({"tool_input": {"command": "git status"}})
        allowed = subprocess.run(
            ["bash", str(hook)], input=payload, capture_output=True, text=True
        )
        self.assertEqual(0, allowed.returncode, "a harmless command must be allowed")

    def test_wiki_flattens_without_page_name_collisions(self) -> None:
        """A GitHub wiki has no directories, so two files sharing a basename collide."""
        import subprocess
        import tempfile

        with tempfile.TemporaryDirectory() as out:
            result = subprocess.run(
                ["python3", ".github/scripts/flatten_wiki.py", "wiki", f"{out}/flat"],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertTrue(Path(f"{out}/flat/Home.md").is_file())

    def test_secret_scanner_detects_key_shapes(self) -> None:
        value = "OPENAI_API_KEY=" + "sk-" + ("a" * 32)
        self.assertEqual([(1, "OpenAI API key")], scan_text(value))

    def test_secret_scanner_allows_placeholders(self) -> None:
        self.assertEqual([], scan_text("OPENAI_API_KEY=\nTOKEN=<placeholder>"))


if __name__ == "__main__":
    unittest.main()
