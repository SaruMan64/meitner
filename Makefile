# Makefile for Meitner

# Editable Installation
edit:
	pip install -e .

# Forced Reinstallation
install:
	pip install --force-reinstall .

# Installing Development Dependencies
install-dev:
	pip install -e .[dev]

# Upgrading

upgrade:
	pip install --upgrade .

# Uninstallation
uninstall:
	pip uninstall meitner

# Purge
purge:
	pip install pip-autoremove
	pip-autoremove meitner -y

# Cleaning the Development Environment
clean:
	rm -rf build
	rm -rf *egg-info
	rm -rf src/*egg-info
	find . -name "__pycache__" -type d -exec rm -rf {} \;
	find . -name ".mypy_cache" -type d -exec rm -rf {} \;

# Running Tests
test:
	pytest

# Running Pre-commit Hooks
pre-commit:
	pre-commit install
	pre-commit run --all-files
