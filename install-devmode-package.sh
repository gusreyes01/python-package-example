#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 -m pip install --editable "$repo_root/package-project/src[dev]"
python3 -m pip show boopackage
