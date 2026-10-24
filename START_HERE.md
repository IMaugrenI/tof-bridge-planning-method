# Start here

`tof-bridge-planning-method` is a small **planning method tool**, not a runtime deployment system.

> German version: [START_HERE_DE.md](START_HERE_DE.md)

## What it is for

It takes already-prepared building blocks and moves them through a controlled planning chain:

```text
00_prepared_blocks/
  → 01_sketches/
  → 02_candidate_sets/
  → 03_reports/
```

The output is planning material. A candidate is not automatically accepted, implemented, or released.

## Requirements

- Python 3.11+
- optionally Docker with Docker Compose

## First local run

```bash
git clone https://github.com/IMaugrenI/tof-bridge-planning-method.git
cd tof-bridge-planning-method

python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-bridge-plan run
```

On Windows, activate the virtual environment using the normal PowerShell/Command Prompt activation command before running `pip install -e .`.

## Docker alternative

```bash
docker compose up --build bridge_planning
```

## What to put into the input folder

Use `00_prepared_blocks/` only for material that is already prepared enough to enter planning.

Do not use this repository as the first place to dump mixed legacy material. For that, see [tof-legacy-recovery-workbench](https://github.com/IMaugrenI/tof-legacy-recovery-workbench).

## What success looks like

A successful run produces structured planning artifacts while keeping open questions and uncertainty visible.

You should be able to tell:

- what source block a candidate came from
- what alternatives were considered
- what is still uncertain
- that no candidate became runtime truth automatically

## Safety / public use

Do not commit secrets, private hostnames, production IDs, customer data, or internal service maps in prepared blocks.

See [SECURITY.md](SECURITY.md).

## More context

- [tof-showcase](https://github.com/IMaugrenI/tof-showcase) — broader public architecture
- [tof-v7-public-frame](https://github.com/IMaugrenI/tof-v7-public-frame) — stricter public boundary reading
