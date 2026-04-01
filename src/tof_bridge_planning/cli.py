from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from .pathing import find_repo_root
from .pipeline import run_bridge_planning
from .io_utils import read_json

GENERATED_DIRS = ['01_sketches', '02_candidate_sets', '03_reports']


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='tof-bridge-plan')
    sub = parser.add_subparsers(dest='command', required=True)

    run = sub.add_parser('run', help='Run the bridge-planning baseline')
    run.add_argument('--repo-root', default='.')

    acc = sub.add_parser('acceptance', help='Show acceptance payload')
    acc.add_argument('--repo-root', default='.')

    clean = sub.add_parser('clean', help='Remove generated stage directories')
    clean.add_argument('--repo-root', default='.')
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    repo_root = find_repo_root(Path(args.repo_root))

    if args.command == 'run':
        summary = run_bridge_planning(repo_root)
        print('Bridge planning run complete')
        print(summary)
    elif args.command == 'acceptance':
        payload = read_json(repo_root / '03_reports' / 'acceptance.json')
        print(payload)
    elif args.command == 'clean':
        for name in GENERATED_DIRS:
            path = repo_root / name
            if path.exists():
                shutil.rmtree(path)
        print('Generated planning outputs removed')


if __name__ == '__main__':
    main()
