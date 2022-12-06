import sys


def parse_assignment(assignment_to_parse):
    start, end = assignment_to_parse.split('-')
    return set(range(int(start), int(end) + 1))


def parse_assignment_pair(assignment_pair_to_parse):
    assignment1_to_parse, assignment2_to_parse = assignment_pair_to_parse.split(',')
    assignment1 = parse_assignment(assignment1_to_parse)
    assignment2 = parse_assignment(assignment2_to_parse)
    return assignment1, assignment2


def get_overlap(assignment1, assignment2):
    return assignment1.intersection(assignment2)


def is_full_overlap(assignment1, assignment2):
    overlap = get_overlap(assignment1, assignment2)
    return overlap == assignment1 or overlap == assignment2


def is_overlap(assignment1, assignment2):
    overlap = get_overlap(assignment1, assignment2)
    return overlap != set()


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def create_raw_assignments_pairs(input):
    return input.strip().split("\n")


def get_full_overlap_count(raw_assignment_pairs):
    full_overlap_count = 0
    for raw_assignment_pair in raw_assignment_pairs:
        assignment1, assignment2 = parse_assignment_pair(raw_assignment_pair)
        if (is_full_overlap(assignment1, assignment2)):
            full_overlap_count += 1
    return full_overlap_count


def solve_puzzle_part_1(input_file_name):
    text = read_input(input_file_name)
    raw_assignment_pairs = create_raw_assignments_pairs(text)
    return get_full_overlap_count(raw_assignment_pairs)


def get_all_overlap_count(raw_assignment_pairs):
    overlap_count = 0
    for raw_assignment_pair in raw_assignment_pairs:
        assignment1, assignment2 = parse_assignment_pair(raw_assignment_pair)
        if (is_overlap(assignment1, assignment2)):
            overlap_count += 1
    return overlap_count


def solve_puzzle_part_2(input_file_name):
    text = read_input(input_file_name)
    raw_assignment_pairs = create_raw_assignments_pairs(text)
    return get_all_overlap_count(raw_assignment_pairs)


if __name__ == "__main__":
    file_input = sys.argv[1]
    full_overlap_count = solve_puzzle_part_1(file_input)
    print(full_overlap_count)
    overlap_count = solve_puzzle_part_2(file_input)
    print(overlap_count)
