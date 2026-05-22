.PHONY: check lint test

check:
	$(MAKE) -C exercise/dictionary check
	$(MAKE) -C exercise/spending_calculator check