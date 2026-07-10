#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 {python|rust} YEAR DAY" >&2
  exit 2
}

[[ $# -eq 3 ]] || usage
language=$1
year=$2
day=$3
[[ $language == python || $language == rust ]] || usage
[[ $year =~ ^20(1[5-9]|2[0-5])$ ]] || usage
[[ $day =~ ^([1-9]|1[0-9]|2[0-5])$ ]] || usage

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
day_dir=$(printf '%s/%s/day%02d' "$repo_root" "$year" "$day")

if [[ $language == python ]]; then
  python3 "$day_dir/solution.py"
else
  cargo run --quiet --manifest-path "$day_dir/rust/Cargo.toml"
fi
