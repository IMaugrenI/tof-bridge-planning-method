# tof-bridge-planning-method

> English is the primary text in this repository. A German clone is available in `README_DE.md`.

Public bridge-planning baseline for continuing prepared building blocks into sketches and target candidates without claiming runtime truth.

I use this repo to show how prepared material can move forward in a structured planning space without turning planning into implementation by accident.

## Why this repo is public

I made this repo public because I believe there should be a disciplined bridge space between recovery and implementation.

I do not want to jump directly from old material into new runtime. I want a real intermediate planning layer where it becomes clear what is adopted, translated, or rejected.

This repo is not a main product repo. It is a method repo that shows how I think about architecture and transition discipline.

## Start here

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

## What this repo does

1. starts from prepared building blocks
2. produces sketches and candidate sets
3. keeps uncertainty visible
4. marks target candidates as planning objects, not implementation truth
5. prevents silent release from planning into runtime

## Why this matters

1. planning and runtime truth are not the same thing
2. prepared material often needs multiple open directions
3. target candidates need review before implementation
4. planning discipline prevents hidden release paths

## Planning chain

1. `00_prepared_blocks/` = prepared building blocks
2. `01_sketches/` = rough sketches per block
3. `02_candidate_sets/` = target candidate bundles
4. `03_reports/` = summary and acceptance

## For employers

This repo is useful if you want to see how I handle:

1. structured continuation from preparation into planning
2. visible uncertainty instead of false certainty
3. disciplined boundaries between planning and implementation
4. method design for later build-out work

## Related public repos

- [`tof-legacy-recovery-workbench`](https://github.com/IMaugrenI/tof-legacy-recovery-workbench) — recovery and separation baseline
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — local builder stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem local knowledge system
