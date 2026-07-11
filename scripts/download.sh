#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 YEAR DAY" >&2
  echo "  YEAR: 2015-2025" >&2
  echo "  DAY:  1-25" >&2
  exit 2
}

[[ $# -eq 2 ]] || usage
year=$1
day=$2
[[ $year =~ ^20(1[5-9]|2[0-5])$ ]] || usage
[[ $day =~ ^([1-9]|1[0-9]|2[0-5])$ ]] || usage

command -v aoc >/dev/null 2>&1 || {
  echo "aoc not found; install it with: cargo install aoc-cli" >&2
  exit 1
}

session_file=${ADVENT_OF_CODE_SESSION_FILE:-"$HOME/.adventofcode.session"}
if [[ ! -s $session_file && -z ${ADVENT_OF_CODE_SESSION:-} ]]; then
  echo "No Advent of Code session found." >&2
  echo "See LOCAL_SETUP.md for secure login instructions." >&2
  exit 1
fi

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
day_dir=$(printf '%s/years/%s/day%02d' "$repo_root" "$year" "$day")

aoc --year "$year" \
  --day "$day" \
  --overwrite \
  --input-file "$day_dir/input.txt" \
  --puzzle-file "$day_dir/puzzle.md" \
  download
