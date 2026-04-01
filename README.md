# tof-bridge-planning-method

> English is the primary text in this repository. A German clone is available in `README_DE.md`.

Public bridge-planning baseline for continuing prepared building blocks into sketches and target candidates without claiming runtime truth.

## At a glance

- starts from prepared building blocks
- produces rough sketches and candidate sets
- keeps uncertainty visible
- marks target candidates as planning objects, not implementation truth
- avoids silent release from planning into runtime

## Why this repo exists

This repository is a public-safe baseline for a bridge-planning pattern:

- continue prepared building blocks
- keep multiple directions open where needed
- form rough sketches
- create target candidates
- preserve the boundary between planning and active runtime truth

## What this repo is

- a reduced technical method baseline
- a runnable demo pipeline
- a public-safe example of planning discipline between preparation and later implementation

## What this repo is not

- not runtime truth
- not the private internal planning space
- not an implementation generator
- not a hidden release path

## Planning chain

1. `00_prepared_blocks/` – prepared building blocks
2. `01_sketches/` – rough sketches per block
3. `02_candidate_sets/` – target candidate bundles
4. `03_reports/` – summary and acceptance

## Quick start

### Local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-bridge-plan run
```

### Docker

```bash
docker compose up --build bridge_planning
```

## Demo input

The repository contains only public-safe fictional building blocks.

They are intentionally small and show how prepared material can continue into:
- Discord structure candidates
- bot interaction candidates
- repo/runtime service candidates
- review-required open candidates

## Key rules

- planning is not runtime truth
- target candidates are not implementation
- uncertainty stays visible
- direction may stay open
- the default run does not materialize runtime code

## Related public repos

- [`tof-legacy-recovery-workbench`](https://github.com/IMaugrenI/tof-legacy-recovery-workbench) — recovery and separation baseline
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — local builder stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem local knowledge system
