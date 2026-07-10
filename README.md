# Advent of Code

I will solve all [Advent of Code](https://adventofcode.com/) puzzles with Python and Rust.

This repository contains starter solutions for every day from 2015 through 2025. Personal puzzle inputs and downloaded puzzle descriptions are kept out of Git.

## Prerequisites

- Python 3
- A recent Rust toolchain (`cargo`)
- [`aoc-cli`](https://github.com/scarvalhojr/aoc-cli) (installed as `aoc`)

## Authenticate `aoc-cli`

Advent of Code uses a browser session cookie rather than a separate CLI login:

1. Sign in at <https://adventofcode.com/>.
2. Open your browser's developer tools, select **Application** (Chrome/Edge) or **Storage** (Firefox), then open Cookies for `https://adventofcode.com`.
3. Copy only the value of the cookie named `session`.
4. Store it as one line in `~/.adventofcode.session` and restrict the file:

   ```sh
   printf '%s' 'PASTE_SESSION_VALUE_HERE' > ~/.adventofcode.session
   chmod 600 ~/.adventofcode.session
   ```

Never commit or share this value. To verify authentication without submitting anything, run:

```sh
aoc calendar --year 2025
```

## Workflow

Download a day's input and puzzle description:

```sh
./scripts/download.sh 2025 1
```

Run either starter:

```sh
./scripts/run.sh python 2025 1
./scripts/run.sh rust 2025 1
```

Submit an answer after reviewing it carefully:

```sh
aoc submit --year 2025 --day 1 1 YOUR_ANSWER
aoc submit --year 2025 --day 1 2 YOUR_ANSWER
```

`aoc submit` sends an answer to Advent of Code immediately, so double-check the year, day, part, and answer first.

Each puzzle lives in `YEAR/dayDD/`. Python code is in `solution.py`; the Rust solution is a standalone crate in `rust/`.
