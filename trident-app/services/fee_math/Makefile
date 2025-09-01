.PHONY: test run-fee-math

test:
	@cd trident-app/services/fee_math && . ../../../../.venv/bin/activate && pytest -q

run-fee-math:
	@cd trident-app/services/fee_math && \
	. ../../../../.venv/bin/activate && \
	python fee_math.py --rad=$(rad) --mpir=$(mpir)
