from __future__ import annotations

import unittest

from scripts.scan_secrets import scan_text
from scripts.validate_workflow import REPO_ROOT, validate


class WorkflowContractTests(unittest.TestCase):
    def test_repository_contract_is_valid(self) -> None:
        self.assertEqual([], validate(REPO_ROOT))

    def test_secret_scanner_detects_key_shapes(self) -> None:
        value = "OPENAI_API_KEY=" + "sk-" + ("a" * 32)
        self.assertEqual([(1, "OpenAI API key")], scan_text(value))

    def test_secret_scanner_allows_placeholders(self) -> None:
        self.assertEqual([], scan_text("OPENAI_API_KEY=\nTOKEN=<placeholder>"))


if __name__ == "__main__":
    unittest.main()

