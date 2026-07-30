#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
wheel="$(find "$repo_root/package-project/src/dist" -maxdepth 1 -name 'boopackage-*.whl' -print -quit)"

if [[ -z "$wheel" ]]; then
  echo "No wheel found. Run ./build-package.sh first." >&2
  exit 1
fi

python3 -m pip install --force-reinstall "$wheel"
