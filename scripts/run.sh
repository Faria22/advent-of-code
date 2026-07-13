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

python3 "$day_dir/solution.py"
