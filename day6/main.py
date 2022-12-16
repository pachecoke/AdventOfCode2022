import sys


def check_has_duplicate(text):
    unique_letters = set(text)
    return len(unique_letters) != len(text)


def separate_by_interval(text, interval=4):
    separated = []
    j = 0
    for i in range(interval, len(text)+1):
        separated.append(text[j:i])
        j += 1
    return separated


def get_marker_index(separated, interval=4):
    for i in range(len(separated)):
        if not check_has_duplicate(separated[i]):
            return i + interval
    return -1


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def solve_puzzle_part_1(input_file_name):
    text = read_input(input_file_name)
    separated = separate_by_interval(text)
    return get_marker_index(separated)


def solve_puzzle_part_2(input_file_name):
    text = read_input(input_file_name)
    separated = separate_by_interval(text, 14)
    return get_marker_index(separated, 14)


if __name__ == "__main__":
    file_input = sys.argv[1]
    answer = solve_puzzle_part_1(file_input)
    print(answer)
    answer = solve_puzzle_part_2(file_input)
    print(answer)
