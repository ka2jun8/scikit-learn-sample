.PHONY: build
build:
	poetry build

.PHONY: clean
clean:
	rm -f *.out

.PHONY: code
code:
	poetry shell && code .

.PHONY: run
run:
	poetry run python -m sample
