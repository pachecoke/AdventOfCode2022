import sys


def read_calories_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def group_items(input):
    return input.split("\n\n")


def create_list(groups):
    return [group.strip().split("\n") for group in groups]


def get_highest_calories(groups):
    calories_sum = get_calories_sum(groups)
    return max(calories_sum)


def get_calories_sum(groups):
    groups = [map(int, group) for group in groups]
    return [sum(group) for group in groups]


def solve_puzzle_part_1(input_file_name):
    text = read_calories_input(input_file_name)
    groups = group_items(text)
    calories = create_list(groups)
    highest_calories = get_highest_calories(calories)
    return highest_calories


def solve_puzzle_part_2(input_file_name):
    text = read_calories_input(input_file_name)
    groups = group_items(text)
    calories = create_list(groups)
    calories_sum = get_calories_sum(calories)
    sorted_sum = sorted(calories_sum, reverse=True)
    return sum(sorted_sum[:3])


if __name__ == "__main__":
    file_input = sys.argv[1]
    highest_calories = solve_puzzle_part_1(file_input)
    print(highest_calories)
    sum_calories = solve_puzzle_part_2(file_input)
    print(sum_calories)
