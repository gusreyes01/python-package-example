# Contributing

Keep changes small and educational: every file should help explain a real
Python packaging concept.

Before opening a pull request:

1. Create and activate a Python 3.10+ virtual environment.
2. Run `./install-devmode-package.sh`.
3. Run `ruff check package-project/src/boopackage package-project/tests package-consumer-project`.
4. Run `pytest package-project/tests`.
5. Run `./build-package.sh`, `./install-built-package.sh`, and
   `./test-consume-package.sh`.

Update the README when a command, required Python version, or packaging
standard changes. Do not add legacy `setup.py` command examples.
