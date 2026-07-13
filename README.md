# Advent of Code — Python

A long-term collection of my Python solutions to every [Advent of Code](https://adventofcode.com/) puzzle.

The project is an exercise in algorithmic problem-solving, data-structure selection, performance tradeoffs, and writing clear, well-reasoned Python.

## Project goals

- Complete all 262 puzzles released from 2015 through 2025.
- Build each solution in Python.
- Favor readable, well-reasoned solutions before optimizing.

## Technology

Python provides fast iteration, expressive solutions, and clear algorithm exploration.

Puzzle input management and answer submission are automated with a small repository CLI backed by [`aoc-cli`](https://github.com/scarvalhojr/aoc-cli).

## Repository structure

```text
advent-of-code/
├── years/
│   ├── 2015/
│   │   ├── day01/
│   │   │   ├── solution.py
│   │   │   └── test.py
│   │   └── ...
│   ├── ...
│   └── 2025/
├── scripts/
└── aocctl
```

Personal inputs and downloaded puzzle descriptions are intentionally excluded from version control.

## Workflow

From any `years/YEAR/dayDD` directory, the folder-aware CLI infers the correct puzzle:

```sh
aocctl download
aocctl run
aocctl submit 1
aocctl submit 2
```

Each Python solution exposes `part_one` and `part_two`. The submit command runs the solution and submits the selected part's printed answer.

## Progress

Solutions will be committed as puzzles are completed. The year and day structure is already scaffolded so each session can stay focused on problem solving.

## Acknowledgements

Puzzle descriptions and inputs are created by [Eric Wastl](https://was.tl/) for [Advent of Code](https://adventofcode.com/). They are not redistributed in this repository.
