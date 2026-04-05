# tof-bridge-planning-method

> English is the primary text in this repository. A German clone is available in `README_DE.md`.

Public bridge_planning baseline for continuing prepared building blocks into sketches and target candidates without claiming runtime truth.

I use this repo to show how prepared material can move forward in a structured planning space without turning planning into implementation by accident.

## start_here

### local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-bridge-plan run
```

### docker

```bash
docker compose up --build bridge_planning
```

## what_this_repo_does

1. starts from prepared building blocks
2. produces sketches and candidate sets
3. keeps uncertainty visible
4. marks target candidates as planning objects, not implementation truth
5. prevents silent release from planning into runtime

## why_this_matters

1. planning and runtime truth are not the same thing
2. prepared material often needs multiple open directions
3. target candidates need review before implementation
4. planning discipline prevents hidden release paths

## planning_chain

1. `00_prepared_blocks/` = prepared building blocks
2. `01_sketches/` = rough sketches per block
3. `02_candidate_sets/` = target candidate bundles
4. `03_reports/` = summary and acceptance

## for_employers

This repo is useful if you want to see how I handle:

1. structured continuation from preparation into planning
2. visible uncertainty instead of false certainty
3. disciplined boundaries between planning and implementation
4. method design for later build_out work

## related_public_repos

- [`tof_legacy_recovery_workbench`](https://github.com/IMaugrenI/tof-legacy-recovery-workbench) — recovery and separation baseline
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — local builder stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on_prem local knowledge system
