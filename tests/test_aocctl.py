import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parents[1]


@pytest.fixture
def aocctl_repo(tmp_path: Path) -> tuple[Path, Path, dict[str, str]]:
    repo = tmp_path / 'repo'
    day_dir = repo / 'years/2024/day10'
    scripts_dir = repo / 'scripts'
    bin_dir = repo / 'bin'
    day_dir.mkdir(parents=True)
    scripts_dir.mkdir()
    bin_dir.mkdir()

    shutil.copy2(REPO_ROOT / 'aocctl', repo / 'aocctl')
    subprocess.run(['git', 'init', '-q'], cwd=repo, check=True)

    run_script = scripts_dir / 'run.sh'
    run_script.write_text(
        """\
#!/usr/bin/env bash
printf 'Part 1: 111\n'
printf 'Part 2: 222\n'
""",
    )
    run_script.chmod(0o755)

    download_script = scripts_dir / 'download.sh'
    download_script.write_text(
        """\
#!/usr/bin/env bash
repo_root=$(git rev-parse --show-toplevel)
printf 'download\n' >> "$repo_root/download.log"
""",
    )
    download_script.chmod(0o755)

    aoc = bin_dir / 'aoc'
    aoc.write_text(
        """\
#!/usr/bin/env bash
repo_root=$(git rev-parse --show-toplevel)
printf '%s\n' "$*" >> "$repo_root/aoc.log"
printf "%s\n" "That's the right answer"
""",
    )
    aoc.chmod(0o755)

    env = os.environ | {'PATH': f'{bin_dir}:{os.environ["PATH"]}'}
    return repo, day_dir, env


@pytest.mark.parametrize(
    ('puzzle', 'expected_part', 'expected_answer'),
    [
        ('\\--- Day 10 ---\n', 1, 111),
        ('\\--- Day 10 ---\n\\--- Part Two ---\n', 2, 222),
    ],
)
def test_submit_infers_part_and_refreshes_puzzle(
    aocctl_repo: tuple[Path, Path, dict[str, str]],
    puzzle: str,
    expected_part: int,
    expected_answer: int,
) -> None:
    repo, day_dir, env = aocctl_repo
    (day_dir / 'puzzle.md').write_text(puzzle)

    result = subprocess.run(
        [repo / 'aocctl', 'submit'],
        cwd=day_dir,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert (repo / 'aoc.log').read_text().strip() == (f'--year 2024 --day 10 submit {expected_part} {expected_answer}')
    assert (repo / 'download.log').read_text() == 'download\n'
    assert 'Refreshing puzzle...' in result.stdout


def test_submit_refuses_a_completed_puzzle(
    aocctl_repo: tuple[Path, Path, dict[str, str]],
) -> None:
    repo, day_dir, env = aocctl_repo
    (day_dir / 'puzzle.md').write_text(
        '\\--- Day 10 ---\n\\--- Part Two ---\nBoth parts of this puzzle are complete!\n',
    )

    result = subprocess.run(
        [repo / 'aocctl', 'submit'],
        cwd=day_dir,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert 'already complete' in result.stderr
    assert not (repo / 'aoc.log').exists()
    assert not (repo / 'download.log').exists()
