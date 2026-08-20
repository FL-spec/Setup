# Template contract gates. These check the workflow itself, not your project code.
# Your project's gates live under `quality_gates` in .sdlc/sdlc-config.yml and run
# through the fl-* skills.

PYTHON ?= python3
VALE ?= vale

# The prose gate runs at warning level on purpose: the signs-of-ai-writing rules put
# their most useful checks at warning and suggestion, so an error-only gate would
# never catch what they exist to catch. See .sdlc/policies/writing-standards.md.
DOC_SOURCES = $(shell git ls-files '*.md' | grep -vE '^(\.claude|\.agents|\.codex|\.github)/')

.PHONY: test validate security docs docs-sync docs-suggestions check install-dev

install-dev:
	@$(PYTHON) -m pip install -r requirements-dev.txt

# Download the Vale rule packages named in .vale.ini. Run once per checkout.
docs-sync:
	@$(VALE) sync

# The prose gate. Fails on errors and warnings.
docs:
	@$(VALE) --minAlertLevel=warning $(DOC_SOURCES)

# Advisory: everything the gate lets through. Read it, act on what improves a sentence.
docs-suggestions:
	@$(VALE) --no-exit --minAlertLevel=suggestion $(DOC_SOURCES)

test:
	@$(PYTHON) -m unittest discover -s tests -p "test_*.py"

validate:
	@$(PYTHON) scripts/validate_workflow.py

security:
	@$(PYTHON) scripts/scan_secrets.py

check: validate security test
