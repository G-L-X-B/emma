TEST_PATTERN = "*_tests.py"
TEST_OPIONS = -v

test:
	python -m unittest discover --pattern $(TEST_PATTERN) $(TEST_OPIONS)
