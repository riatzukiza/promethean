# === Global Settings ===
PY_BUILD_DIR=shared/py
JS_BUILD_DIR=shared/js
HYPHON_SRC=shared/hy
SIBILANT_SRC=shared/sibilant
TS_SRC=shared/ts
TS_OUT=shared/js

# === High-Level Targets ===

.PHONY: all build clean lint format test

all: build

build: build-python build-js

clean: clean-python clean-js clean-ts

lint: lint-python lint-js

format: format-python format-js

test: test-python test-js

# === Python/HY ===

build-python:
	@echo "Transpiling Hy to Python..."
	# Add real transpilation if needed
	@echo "Done."

clean-python:
	find $(PY_BUILD_DIR) -name '*.pyc' -delete

lint-python:
	flake8 services/ shared/py/

format-python:
	black services/ shared/py/

test-python:
	pytest tests/python/

# === JS/TS/Sibilant ===

build-js: build-ts build-sibilant

build-sibilant:
	@echo "Transpiling Sibilant to JS..."
	npx sibilant $(SIBILANT_SRC)/common -o $(JS_BUILD_DIR)/common
	npx sibilant $(SIBILANT_SRC)/server -o $(JS_BUILD_DIR)/server
	npx sibilant $(SIBILANT_SRC)/client -o $(JS_BUILD_DIR)/client

build-ts:
	@echo "Transpiling TS to JS..."
	tsc -p $(TS_SRC)

clean-js:
	rm -rf $(JS_BUILD_DIR)/*

clean-ts:
	rm -rf $(TS_OUT)/*

lint-js:
	eslint shared/js/ services/**/ --ext .js,.ts

format-js:
	prettier --write shared/js/ services/**/

test-js:
	npm test
