#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 YEAR DAY" >&2
  exit 2
}

[[ $# -eq 2 ]] || usage
year=$1
day=$2
[[ $year =~ ^20(1[5-9]|2[0-5])$ ]] || usage
[[ $day =~ ^([1-9]|1[0-9]|2[0-5])$ ]] || usage
[[ $year != 2025 || $day -le 12 ]] || usage

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
day_dir=$(printf '%s/years/%s/day%02d' "$repo_root" "$year" "$day")
test_path="$day_dir/test.py"

command -v uv >/dev/null 2>&1 || {
  echo "uv not found; install it before running Advent of Code tests." >&2
  exit 1
}

[[ -f $test_path ]] || {
  echo "Test file not found: $test_path" >&2
  exit 1
}

cd "$day_dir"
uv run --project "$repo_root" --locked pytest test.py -q
