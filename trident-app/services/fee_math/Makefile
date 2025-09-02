.PHONY: test path

# Use whatever python is on PATH; CI pins Python anyway
PY ?= python3

# Quick sanity so devs see where they are
path:
	@echo "pwd: $$(pwd)"; which $(PY) || true

# Run tests via the interpreter (no fragile activate paths)
test:
	@$(MAKE) path
	@$(PY) -m pytest -q
