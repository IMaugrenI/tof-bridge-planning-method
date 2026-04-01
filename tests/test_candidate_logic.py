from tof_bridge_planning.planning import PreparedBlock, sketch_from_block, candidate_set_from_block


def test_mixed_high_uncertainty_gets_review_required() -> None:
    block = PreparedBlock(
        block_id='x',
        title='mixed',
        prepared_kind='mixed_fragment',
        summary='test',
        signals=['discord', 'repo', 'open'],
        open_questions=['?'],
        uncertainty='high',
    )
    sketch = sketch_from_block(block)
    candidate_set = candidate_set_from_block(block, sketch)
    assert 'review_required' in sketch.possible_directions
    assert candidate_set.review_required is True
