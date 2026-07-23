PYTHON ?= python3

.PHONY: test validate security check

test:
	@$(PYTHON) -m unittest discover -s tests -p "test_*.py"

validate:
	@$(PYTHON) scripts/validate_workflow.py

security:
	@$(PYTHON) scripts/scan_secrets.py

check: test validate security

