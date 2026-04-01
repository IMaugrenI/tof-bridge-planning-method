from __future__ import annotations

from pathlib import Path


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / 'MANIFEST.md').exists() and (candidate / '00_prepared_blocks').exists():
            return candidate
    raise FileNotFoundError('bridge planning repo root not found')
