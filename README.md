# Python Package Example

A small, executable reference for building, installing, testing, and consuming
a Python package with the current PyPA workflow. The example intentionally
keeps the package tiny so the packaging mechanics remain visible.

## Repository layout

- `package-project/src/` is the package project root. It contains
  `pyproject.toml`, the `boopackage` source, and package-specific documentation.
- `package-project/tests/` contains behavioral tests for the installed package.
- `package-consumer-project/` is a separate script that imports `boopackage`
  like a downstream application.
- The root shell scripts demonstrate build, editable-install, wheel-install,
  consumer-smoke, and uninstall operations.

Python 3.10 or newer is required.

## Set up a development environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip build
./install-devmode-package.sh
ruff check package-project/src/boopackage package-project/tests package-consumer-project
pytest package-project/tests
```

The editable install includes the development tools declared in
`pyproject.toml`, so changes under `boopackage/` are visible immediately
without reinstalling.

## Build distributions

```bash
python3 -m pip install build
./build-package.sh
```

The script uses the PEP 517 frontend (`python -m build`) and writes both a
wheel and source distribution under `package-project/src/dist/`. Calling
`setup.py` directly is intentionally not part of this example.

## Install and consume the wheel

```bash
./install-built-package.sh
./test-consume-package.sh
```

The consumer prints the same absolute-import and relative-import demonstration
used by the test suite, followed by `it worked!`.

## Why wheels instead of eggs?

Eggs are obsolete. Wheels are the standard built distribution format, while
source distributions provide a portable source archive. See the
[Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
for the complete publishing workflow.

## Quality and security

CI builds the distributions, installs the wheel, runs the behavioral tests,
and executes the downstream consumer on supported Python versions. See
[CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
