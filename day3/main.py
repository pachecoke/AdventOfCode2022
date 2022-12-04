import sys


def get_compartments(rucksack):
    compartment_size = int(len(rucksack) / 2)
    compartment1 = rucksack[0:compartment_size]
    compartment2 = rucksack[compartment_size:len(rucksack)]
    return [compartment1, compartment2]


def get_common_item(compartments):
    common_item = set(compartments[0]).intersection(compartments[1])
    return list(common_item)[0]


def get_item_priority(item):
    priority = ord(item) % 32
    if item.isupper():
        priority += 26
    return priority


def read_input(input_file_name):
    with open(input_file_name) as f:
        text = f.read()
    return text


def create_rucksacks(input):
    return input.strip().split("\n")


def get_total_priority(rucksacks):
    total_priority = 0
    for rucksack in rucksacks:
        compartments = get_compartments(rucksack)
        common_item = get_common_item(compartments)
        total_priority += get_item_priority(common_item)
    return total_priority


def solve_puzzle_part_1(input_file_name):
    text = read_input(input_file_name)
    rucksacks = create_rucksacks(text)
    return get_total_priority(rucksacks)


def get_badge(group):
    badge = set(group[0]).intersection(group[1]).intersection(group[2])
    return list(badge)[0]


def get_badge_priority(group):
    badge = get_badge(group)
    priority = get_item_priority(badge)
    return priority


def get_total_badge_priority(groups):
    total_priority = 0
    for group in groups:
        total_priority += get_badge_priority(group)
    return total_priority


def create_groups(rucksacks):
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i:i+3])
    return groups


def solve_puzzle_part_2(input_file_name):
    text = read_input(input_file_name)
    rucksacks = create_rucksacks(text)
    groups = create_groups(rucksacks)
    return get_total_badge_priority(groups)


if __name__ == "__main__":
    file_input = sys.argv[1]
    total_priority = solve_puzzle_part_1(file_input)
    print(total_priority)
    total_badge_priority = solve_puzzle_part_2(file_input)
    print(total_badge_priority)
