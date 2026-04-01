#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-bridge-plan clean || true
tof-bridge-plan run
