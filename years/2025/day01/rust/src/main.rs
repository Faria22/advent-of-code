use std::{fs, path::PathBuf};

const INITIAL_DIAL_VALUE: u16 = 50;
const MAX_DIAL_VALUE: u16 = 100;

fn parse_input_line(line: &str) -> i16 {
    let movement: i16 = line[1..].parse().unwrap();

    if line.starts_with('L') {
        -movement
    } else {
        movement
    }
}

/// Return the final position
fn move_dial_part_one(initial: u16, movement: i16) -> u16 {
    let mut final_pos = initial as i16 + movement;

    final_pos %= MAX_DIAL_VALUE as i16;

    if final_pos < 0 {
        final_pos += MAX_DIAL_VALUE as i16;
    }

    final_pos
        .try_into()
        .expect("final_pos should always be positive.")
}

/// Return the final position and the how many times it crossed 0
fn move_dial_part_two(initial: u16, movement: i16) -> (u16, u16) {
    let mut final_pos = initial as i16 + movement;

    let mut zero_count = (final_pos / MAX_DIAL_VALUE as i16).abs() as u16;

    if final_pos <= 0 && initial > 0 {
        zero_count += 1;
    }

    final_pos %= MAX_DIAL_VALUE as i16;

    if final_pos < 0 {
        final_pos += MAX_DIAL_VALUE as i16;
    }

    (
        final_pos
            .try_into()
            .expect("final_pos should always be positive."),
        zero_count,
    )
}

fn part_one(input: &str) -> u16 {
    let mut initial = INITIAL_DIAL_VALUE;
    let mut zero_count = 0;
    for line in input.split('\n') {
        let motion = parse_input_line(line);
        initial = move_dial_part_one(initial, motion);
        if initial == 0 {
            zero_count += 1
        }
    }
    zero_count
}

fn part_two(input: &str) -> u16 {
    let mut initial = INITIAL_DIAL_VALUE;
    let mut total_zero_count = 0;
    let mut zero_count;
    for line in input.split('\n') {
        let motion = parse_input_line(line);
        (initial, zero_count) = move_dial_part_two(initial, motion);

        total_zero_count += zero_count;
    }
    total_zero_count
}

fn main() {
    let input_path = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../input.txt");
    let input = fs::read_to_string(&input_path)
        .unwrap_or_else(|error| panic!("failed to read {}: {error}", input_path.display()));
    let input = input.trim_end_matches('\n');

    println!("Part 1: {:?}", part_one(input));
    println!("Part 2: {:?}", part_two(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_move_dial_part_one() {
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, 10), 60);
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, -10), 40);
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, 60), 10);
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, -60), 90);
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, 160), 10);
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, -160), 90);
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, 50), 0);
        assert_eq!(move_dial_part_one(INITIAL_DIAL_VALUE, -50), 0);
    }

    #[test]
    fn test_move_dial_part_two() {
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, 10), (60, 0));
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, -10), (40, 0));
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, 60), (10, 1));
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, -60), (90, 1));
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, 160), (10, 2));
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, -160), (90, 2));
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, 50), (0, 1));
        assert_eq!(move_dial_part_two(INITIAL_DIAL_VALUE, -50), (0, 1));
        assert_eq!(move_dial_part_two(0, -10), (90, 0));
        assert_eq!(move_dial_part_two(0, 10), (10, 0));
    }
}
