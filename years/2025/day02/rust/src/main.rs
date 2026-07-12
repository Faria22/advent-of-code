use std::ops::RangeInclusive;
use std::{fs, path::PathBuf};

fn part_one(input: &str) -> u64 {
    let mut total = 0;
    for range in parse_input(input) {
        for num in parse_range(range) {
            if is_invalid(num, Some(2)) {
                total += num;
            }
        }
    }

    total
}

fn part_two(input: &str) -> u64 {
    let mut total = 0;
    for range in parse_input(input) {
        for num in parse_range(range) {
            if is_invalid(num, None) {
                total += num
            }
        }
    }

    total
}

fn is_invalid(num: u64, count: Option<u8>) -> bool {
    let str_num: String = num.to_string();
    let mut pattern = "".to_string();

    // Only take half of the digits since the pattern cannot be longer than that
    let len_str = str_num.chars().count();
    if count.is_some() && len_str as u8 % count.unwrap() != 0 {
        return false;
    }
    for digit in str_num.chars().take(len_str / 2) {
        pattern += &digit.to_string();
        let trimmed_str = if count.is_some() {
            str_num.replacen(&pattern, "", count.unwrap().into())
        } else {
            str_num.replace(&pattern, "")
        };
        if trimmed_str == "" {
            return true;
        }
    }

    false
}

fn parse_input(input: &str) -> Vec<&str> {
    input.split(',').collect()
}

fn parse_range(range: &str) -> RangeInclusive<u64> {
    let end_points: Vec<&str> = range.split('-').collect();

    let end_points: Vec<u64> = end_points.iter().map(|&x| x.parse().unwrap()).collect();

    return end_points[0]..=end_points[1];
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
    fn test_parse_range() {
        assert_eq!(parse_range("11-22"), 11..=22);
    }

    #[test]
    fn test_is_invalid() {
        assert!(is_invalid(55, Some(2)));
        assert!(!is_invalid(555, Some(2)));
        assert!(is_invalid(555, None));
        assert!(is_invalid(123123, Some(2)));
        assert!(!is_invalid(123123123, Some(2)));
        assert!(is_invalid(123123123, None));
    }
}
