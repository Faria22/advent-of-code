# Advent of Code — Python & Rust

A long-term collection of my solutions to every [Advent of Code](https://adventofcode.com/) puzzle, implemented in both Python and Rust.

The project is an exercise in algorithmic problem-solving, data-structure selection, performance tradeoffs, and expressing the same ideas across two languages with very different strengths.

## Project goals

- Complete all 275 puzzles released from 2015 through 2025.
- Build each solution independently in Python and Rust.
- Favor readable, well-reasoned solutions before optimizing.
- Use the paired implementations to compare ergonomics, correctness, and performance.

## Technology

| Language | Focus |
| --- | --- |
| Python | Fast iteration, expressive solutions, and clear algorithm exploration |
| Rust | Type-driven design, predictable performance, and memory safety |

Puzzle input management and answer submission are automated with a small repository CLI backed by [`aoc-cli`](https://github.com/scarvalhojr/aoc-cli).

## Repository structure

```text
advent-of-code/
├── years/
│   ├── 2015/
│   │   ├── day01/
│   │   │   ├── python/
│   │   │   │   ├── solution.py
│   │   │   │   └── test.py
│   │   │   └── rust/
│   │   │       ├── Cargo.toml
│   │   │       └── src/main.rs
│   │   └── ...
│   ├── ...
│   └── 2025/
├── scripts/
└── aocctl
```

Personal inputs and downloaded puzzle descriptions are intentionally excluded from version control.

## Workflow

From any `years/YEAR/dayDD` directory (or its Rust subdirectory), the folder-aware CLI infers the correct puzzle:

```sh
aocctl download
aocctl run python
aocctl run rust
aocctl submit 1 YOUR_ANSWER
aocctl submit 2 YOUR_ANSWER
```

Each Python solution exposes `part_one` and `part_two`. Each Rust crate follows the same two-part shape, keeping the implementations easy to navigate and compare.

## Progress

Solutions will be committed as puzzles are completed. The year and day structure is already scaffolded so each session can stay focused on problem solving.

## Acknowledgements

Puzzle descriptions and inputs are created by [Eric Wastl](https://was.tl/) for [Advent of Code](https://adventofcode.com/). They are not redistributed in this repository.
