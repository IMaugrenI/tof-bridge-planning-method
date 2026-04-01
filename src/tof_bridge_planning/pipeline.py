from __future__ import annotations

from pathlib import Path

from .io_utils import read_json, write_json
from .planning import CandidateSet, PreparedBlock, candidate_set_from_block, sketch_from_block


def run_bridge_planning(repo_root: Path) -> dict:
    prepared_blocks = [PreparedBlock(**item) for item in read_json(repo_root / '00_prepared_blocks' / 'demo_blocks.json')]
    sketches: list[SketchPayload] = []
    candidate_sets: list[CandidatePayload] = []

    for block in prepared_blocks:
        sketch = sketch_from_block(block)
        candidate_set = candidate_set_from_block(block, sketch)
        write_json(repo_root / '01_sketches' / f'{block.block_id}.json', sketch.to_dict())
        write_json(repo_root / '02_candidate_sets' / f'{block.block_id}.json', candidate_set.to_dict())
        sketches.append(sketch.to_dict())
        candidate_sets.append(candidate_set.to_dict())

    acceptance = {
        'prepared_block_count': len(prepared_blocks),
        'sketch_count': len(sketches),
        'candidate_set_count': len(candidate_sets),
        'all_not_runtime_truth': all(item['not_runtime_truth'] for item in sketches + candidate_sets),
        'review_required_count': sum(1 for item in candidate_sets if item['review_required']),
        'default_run_materializes_runtime_code': False,
    }
    summary = {
        'prepared_blocks': len(prepared_blocks),
        'sketches': len(sketches),
        'candidate_sets': len(candidate_sets),
    }
    write_json(repo_root / '03_reports' / 'acceptance.json', acceptance)
    write_json(repo_root / '03_reports' / 'run_summary.json', summary)
    return summary


SketchPayload = dict
CandidatePayload = dict
