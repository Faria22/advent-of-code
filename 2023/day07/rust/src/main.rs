use std::{fs, path::PathBuf};

fn part_one(input: &str) {
    todo!()
}

fn part_two(input: &str) {
    todo!()
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
mod tests {}
