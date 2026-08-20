# Template contract gates. These check the workflow itself, not your project code —
# your project's gates live under `quality_gates` in .sdlc/sdlc-config.yml and run
# through the fl-* skills.

PYTHON ?= python3

.PHONY: test validate security check install-dev

install-dev:
	@$(PYTHON) -m pip install -r requirements-dev.txt

test:
	@$(PYTHON) -m unittest discover -s tests -p "test_*.py"

validate:
	@$(PYTHON) scripts/validate_workflow.py

security:
	@$(PYTHON) scripts/scan_secrets.py

check: validate security test
