from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(slots=True)
class PreparedBlock:
    block_id: str
    title: str
    prepared_kind: str
    summary: str
    signals: list[str]
    open_questions: list[str]
    uncertainty: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Sketch:
    block_id: str
    title: str
    sketch_notes: list[str]
    possible_directions: list[str]
    uncertainty: str
    not_runtime_truth: bool = True

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class CandidateSet:
    block_id: str
    candidate_classes: list[str]
    target_candidates: list[dict[str, Any]]
    review_required: bool
    not_runtime_truth: bool = True

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def sketch_from_block(block: PreparedBlock) -> Sketch:
    directions: list[str] = []
    notes: list[str] = []
    signals = set(block.signals)
    if 'discord' in signals:
        directions.append('discord_candidate')
        notes.append('Continue prepared structure into channel/role candidate framing.')
    if 'bot' in signals or 'slash' in signals or 'interaction' in signals:
        directions.append('bot_candidate')
        notes.append('Continue prepared interaction surface into command/module candidates.')
    if 'repo' in signals or 'services' in signals or 'postgres' in signals or 'redis' in signals:
        directions.append('repo_candidate')
        notes.append('Continue prepared runtime cluster into service candidate grouping.')
    if not directions or block.uncertainty == 'high' or 'open' in signals:
        directions.append('review_required')
        notes.append('Keep direction open and require explicit later review.')
    return Sketch(
        block_id=block.block_id,
        title=block.title,
        sketch_notes=notes,
        possible_directions=directions,
        uncertainty=block.uncertainty,
    )


def candidate_set_from_block(block: PreparedBlock, sketch: Sketch) -> CandidateSet:
    targets: list[dict[str, Any]] = []
    for direction in sketch.possible_directions:
        if direction == 'discord_candidate':
            targets.append({
                'candidate_id': f'{block.block_id}__discord',
                'candidate_class': 'discord_candidate',
                'candidate_title': f'{block.title} / Discord candidate',
                'status': 'planning_only',
            })
        elif direction == 'bot_candidate':
            targets.append({
                'candidate_id': f'{block.block_id}__bot',
                'candidate_class': 'bot_candidate',
                'candidate_title': f'{block.title} / Bot candidate',
                'status': 'planning_only',
            })
        elif direction == 'repo_candidate':
            targets.append({
                'candidate_id': f'{block.block_id}__repo',
                'candidate_class': 'repo_candidate',
                'candidate_title': f'{block.title} / Repo candidate',
                'status': 'planning_only',
            })
        elif direction == 'review_required':
            targets.append({
                'candidate_id': f'{block.block_id}__review',
                'candidate_class': 'review_required',
                'candidate_title': f'{block.title} / Open review candidate',
                'status': 'planning_only',
            })
    return CandidateSet(
        block_id=block.block_id,
        candidate_classes=sketch.possible_directions,
        target_candidates=targets,
        review_required='review_required' in sketch.possible_directions,
    )
